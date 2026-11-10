#!/usr/bin/env python3
"""
convert_blogdown_to_quarto.py SRC_REPO DEST_DIR [--force-scaffold]

Convert the imachordata blogdown/Hugo repository into a Quarto website project.

What it does
  * every post in content/post  ->  DEST/posts/YYYYMMDD_<slug>.qmd
    (the old Hugo URL /YYYY/MM/DD/<slug>/ is kept as a redirect via `aliases`)
  * links between posts are rewritten to .qmd links (Quarto renders them as .html)
  * Hugo front matter -> Quarto front matter (tags become `keywords`, `summary` becomes `description`)
  * WordPress [caption] shortcodes, Hugo `tweet` / `blogdown/postref` shortcodes are rewritten
  * figure folders that blogdown kept in static/post/ are copied to DEST/posts/files/<post>/
  * the five R Markdown posts are converted from their .Rmd sources into executable .qmd files
    (live R chunks, figures regenerated when rendered); the old rendered output is not used.
    The .Rmd originals are also archived in DEST/_legacy/rmd-sources/
  * every post is credited to Jarrett Byrnes
  * about.md -> about/index.qmd
  * site scaffolding (_quarto.yml, theme, header, Disqus/pager include, listing pages, ...) is written
    only if it does not exist yet (or with --force-scaffold), so your own tweaks are not overwritten

Re-running is safe: existing posts and scaffolding are left alone (use --overwrite-posts / --force-scaffold to regenerate).
Requires: Python 3.8+, PyYAML.
"""
import argparse
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

import yaml

HERE = Path(__file__).resolve().parent
AUTHOR = "Jarrett Byrnes"  # every post is credited to this author

# --------------------------------------------------------------------------------------
# front matter
# --------------------------------------------------------------------------------------
FM_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.S)


def split_front_matter(text):
    text = text.lstrip("\ufeff").replace("\r\n", "\n")
    m = FM_RE.match(text)
    if not m:
        raise ValueError("no YAML front matter")
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def as_list(v):
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return [str(x).strip() for x in v if str(x).strip()]
    return [str(v).strip()] if str(v).strip() else []


# --------------------------------------------------------------------------------------
# body conversion
# --------------------------------------------------------------------------------------
# the attributes always end with a quoted value directly followed by "]"
CAP_OPEN = re.compile(r'\[caption\s+(?P<attrs>.*?")\]\s*', re.S)
IMG_AT_START = re.compile(
    r"^(\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)|!\[[^\]]*\]\([^)]*\)|<a[^>]*>\s*<img[^>]*>\s*</a>|<img[^>]*>)\s*(.*)$",
    re.S,
)


def convert_captions(text):
    """WordPress [caption ...]<img>[/caption] -> pandoc fenced div with the image + caption text."""
    out, pos = [], 0
    while True:
        m = CAP_OPEN.search(text, pos)
        if not m:
            out.append(text[pos:])
            break
        end = text.find("[/caption]", m.end())
        if end == -1:
            out.append(text[pos:])
            break
        out.append(text[pos:m.start()])
        attrs = m.group("attrs")
        inner = text[m.end():end].strip()

        align = (re.search(r'align="([^"]*)"', attrs) or [None, "alignnone"])[1]
        width = (re.search(r'width="(\d+)"', attrs) or [None, ""])[1]
        cm = re.search(r'caption="(.*)"\s*$', attrs, re.S)
        caption = cm.group(1) if cm else ""

        im = IMG_AT_START.match(inner)
        if im:
            img, trailing = im.group(1), im.group(2).strip()
            if not caption:
                caption = trailing
        else:
            img = inner

        caption = re.sub(r"\s+", " ", caption).strip()
        cls = align if align in ("aligncenter", "alignleft", "alignright", "alignnone") else "alignnone"
        style = f' style="width: {width}px;"' if width else ""
        block = f"\n\n::: {{.wp-caption .{cls}{style}}}\n{img}\n"
        if caption:
            block += f"\n{caption}\n"
        block += ":::\n\n"
        out.append(block)
        pos = end + len("[/caption]")
    return "".join(out)


TWEET_RE = re.compile(r'\{\{<\s*tweet\s+(?:id=)?"?(\d+)"?\s*>\}\}')


def convert_tweets(text):
    def repl(m):
        tid = m.group(1)
        return (
            "\n\n```{=html}\n"
            f'<blockquote class="twitter-tweet"><a href="https://twitter.com/x/status/{tid}">'
            "View this post</a></blockquote>\n"
            '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n'
            "```\n\n"
        )

    return TWEET_RE.sub(repl, text)


FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
ATX_RE = re.compile(r"^ {0,3}#{1,6}(?:[ \t]|$)")
BQ_RE = re.compile(r"^ {0,3}>")
BULLET_START_RE = re.compile(r"^ {0,3}(?:[-*+]|1[.)])[ \t]+\S")
LISTITEM_RE = re.compile(r"^ {0,3}(?:[-*+]|\d{1,9}[.)])[ \t]+")
HR_RE = re.compile(r"^ {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$")
EXEC_FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*\{([A-Za-z][\w+-]*)(?:[ ,][^}]*)?\}\s*$", re.M)


def normalize_blocks(text):
    """Hugo (CommonMark) lets headings, blockquotes, bullet lists and code fences interrupt a paragraph.
    Pandoc wants a blank line first. Insert one where CommonMark would have started a new block."""
    out, in_fence = [], None
    for line in text.split("\n"):
        fm = FENCE_RE.match(line)
        if in_fence:
            out.append(line)
            if (
                fm
                and fm.group(2)[0] == in_fence[0]
                and len(fm.group(2)) >= len(in_fence)
                and not fm.group(3).strip()
            ):
                in_fence = None
            continue
        prev = out[-1] if out else ""
        prev_blank = prev.strip() == ""
        prev_indented = prev.startswith((" ", "\t"))
        if fm:
            if not prev_blank and not prev_indented and not LISTITEM_RE.match(prev):
                out.append("")
            in_fence = fm.group(2)
            out.append(line)
            continue
        if not prev_blank:
            if ATX_RE.match(line):
                out.append("")
            elif BQ_RE.match(line) and not BQ_RE.match(prev):
                out.append("")
            elif (
                BULLET_START_RE.match(line)
                and not HR_RE.match(line)
                and not LISTITEM_RE.match(prev)
                and not prev_indented
                and not BQ_RE.match(prev)
                and not ATX_RE.match(prev)
            ):
                out.append("")
        out.append(line)
    return "\n".join(out)


# links to other posts, in the old permalink form (/2020/05/07/slug/ or http://www.imachordata.com/2020/05/07/slug/)
# become links to the .qmd file; Quarto turns those into .html links when it renders
OLD_LINK_RE = re.compile(
    r"""(?P<pre>[(\"'])(?:https?://(?:www\.)?imachordata\.com)?/(\d{4})/(\d{2})/(\d{2})/(?P<slug>[^/\s)"'#?]+)/?(?P<post>[)\"'#?])"""
)


def rewrite_internal_links(body, link_map):
    def repl(m):
        stem = link_map.get((m.group(2), m.group(3), m.group(4), m.group("slug")))
        if not stem:
            return m.group(0)
        return f"{m.group('pre')}/posts/{stem}.qmd{m.group('post')}"

    return OLD_LINK_RE.sub(repl, body)


# --------------------------------------------------------------------------------------
# R Markdown -> executable Quarto
# --------------------------------------------------------------------------------------
CODE_BLOCK_RE = re.compile(r"^(`{3,}|~{3,}).*?^\1[ \t]*$", re.M | re.S)
CHUNK_HEADER_RE = re.compile(r"^(?P<fence>`{3,})\{(?P<engine>[A-Za-z][A-Za-z0-9_]*)(?P<opts>[^\n]*)\}[ \t]*$", re.M)


def outside_code(text, fn):
    """Apply fn to the parts of text that are not inside fenced code blocks."""
    out, pos = [], 0
    for m in CODE_BLOCK_RE.finditer(text):
        out.append(fn(text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(fn(text[pos:]))
    return "".join(out)


def split_top_level(s):
    parts, cur, depth, quote = [], "", 0, None
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            cur += ch
        elif ch in "([{":
            depth += 1
            cur += ch
        elif ch in ")]}":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def chunk_value(v):
    v = v.strip()
    if v in ("TRUE", "T", "true"):
        return "true"
    if v in ("FALSE", "F", "false"):
        return "false"
    if re.fullmatch(r"-?\d+(\.\d+)?", v) or re.fullmatch(r'"[^"]*"|\'[^\']*\'', v):
        return v
    return "!expr " + v


def convert_chunk_header(m):
    """```{r name, echo=FALSE, fig.width=5}  ->  ```{r} + #| label / echo / fig-width lines"""
    engine = m.group("engine")
    parts = split_top_level(m.group("opts").strip().lstrip(",").strip())
    lines = [f"{m.group('fence')}{{{engine}}}"]
    opts = []
    for i, part in enumerate(parts):
        if "=" not in part and i == 0:
            opts.append(("label", part))
        elif "=" in part:
            k, v = part.split("=", 1)
            opts.append((k.strip().replace(".", "-").replace("_", "-") if k.strip() != "label" else "label", chunk_value(v)))
    for k, v in opts:
        lines.append(f"#| {k}: {v}")
    return "\n".join(lines)


def convert_chunks(text):
    return CHUNK_HEADER_RE.sub(convert_chunk_header, text)


def strip_html_comments(text):
    return outside_code(text, lambda t: re.sub(r"<!--.*?-->", "", t, flags=re.S))


# Small code fixes so the R posts still run with current package versions.
# (regex, replacement, why)
CODE_FIXES = [
    (
        r'labs\(\s*("(?:[^"\\]|\\.)*")\s*\)',
        r"labs(title = \1)",
        "ggplot2 >= 4.0 errors on an unnamed labs() argument (older versions silently ignored it)",
    ),
]

STATIC_POST_RE = re.compile(r"""(?<=[("'=])/post/([^/\s)"']+)/([^\s)"']+)""")


def convert_body(body, ctx, executable=False):
    body = body.replace("\r\n", "\n")
    if executable:
        body = strip_html_comments(body)
    body = re.sub(r"<!--\s*more\s*-->", "", body)
    body = body.replace("{{< blogdown/postref >}}", "")
    body = re.sub(r"\]\(\((https?://[^)\s]+)\)", r"](\1)", body)  # typo "[text]((url)" in one post
    body = convert_tweets(body)
    body = convert_captions(body)

    stem = ctx.get("stem")
    if stem:
        def static_repl(m):
            ctx["assets"].append((m.group(1), m.group(2)))
            return f"files/{stem}/{m.group(1)}/{m.group(2)}"

        body = STATIC_POST_RE.sub(static_repl, body)
        # files that sat next to a bundle post (index.en_files/, images/, ...) now live in posts/files/<stem>/
        for name in ctx.get("bundle_names", []):
            body = re.sub(r"""(?<=[("'=])""" + re.escape(name) + "/", f"files/{stem}/{name}/", body)
    if "/rmarkdown-libs/" in body:
        ctx["needs_rmarkdown_libs"] = True
        body = body.replace("/rmarkdown-libs/", "../rmarkdown-libs/")
    body = rewrite_internal_links(body, ctx.get("link_map", {}))
    # ```{r ...} would make Quarto try to *run* the chunk; show it as plain code instead
    if executable:
        body = convert_chunks(body)  # keep the R chunks live
    else:
        body = EXEC_FENCE_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}{m.group(3)}", body)
    body = normalize_blocks(body)
    return body.strip("\n") + "\n"


def fix_about(body):
    """about.md has a mangled image link: `[caption](full.jpg)](full.jpg)`.
    The old built site rendered it as the 300x225 thumbnail linking to the full image."""
    def repl(m):
        alt, url = m.group(1), m.group(2)
        thumb = re.sub(r"(\.\w+)$", r"-300x225\1", url)
        return f"[![{alt}]({thumb})]({url})"

    return re.sub(r"^\[([^\]\n]+)\]\((https?://[^)\s]+)\)\]\(\2\)[ \t]*$", repl, body, flags=re.M)


def dump_front_matter(fm):
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100000) + "---\n\n"


# --------------------------------------------------------------------------------------
# posts
# --------------------------------------------------------------------------------------
def find_posts(src):
    root = src / "content" / "post"
    for p in sorted(root.iterdir()):
        if p.is_file() and p.suffix == ".md":
            yield p, None
        elif p.is_dir():
            idx = [c for c in p.iterdir() if re.fullmatch(r"index(\.\w+)?\.md", c.name)]
            if idx:
                yield idx[0], p


def collect_posts(src):
    posts, seen, warnings = [], {}, []
    for md, bundle in find_posts(src):
        twin = md.with_name(re.sub(r"\.md$", ".Rmd", md.name))
        is_rmd = twin.exists()
        fm, body = split_front_matter((twin if is_rmd else md).read_text(encoding="utf8"))
        title = str(fm.get("title", md.stem)).strip()
        date = str(fm.get("date", ""))[:10]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            m = re.match(r"(\d{4}-\d{2}-\d{2})", md.parent.name if bundle else md.name)
            date = m.group(1) if m else ""
        if not date:
            warnings.append(f"skipped (no date): {md}")
            continue
        slug = str(fm.get("slug") or "").strip()
        if slug and not re.fullmatch(r"[A-Za-z0-9_.-]+", slug):
            # e.g. "%e2%89%a0" (an encoded "≠"): Hugo dropped such characters from the URL
            slug = slugify(unquote(slug))
        if not slug:
            stem0 = bundle.name if bundle else md.name.split(".")[0]
            slug = slugify(re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem0))
        y, mth, d = date.split("-")
        stem = f"{y}{mth}{d}_{slug}"
        if stem in seen:
            warnings.append(f"duplicate post {stem}: {md} vs {seen[stem]}")
            continue
        seen[stem] = md
        posts.append(dict(md=md, rmd=is_rmd, bundle=bundle, fm=fm, body=body, title=title, date=date,
                          slug=slug, stem=stem, y=y, m=mth, d=d))
    return posts, warnings


def convert_posts(src, dst, merge_tags=False, overwrite=False):
    posts, warnings = collect_posts(src)
    link_map = {(p["y"], p["m"], p["d"], p["slug"]): p["stem"] for p in posts}
    out_dir = dst / "posts"
    files_dir = out_dir / "files"
    out_dir.mkdir(parents=True, exist_ok=True)
    uses_rmd_libs = False

    skipped = 0
    for p in posts:
        stem, bundle, fm = p["stem"], p["bundle"], p["fm"]
        if (out_dir / f"{stem}.qmd").exists() and not overwrite:
            skipped += 1  # never clobber a post that already exists (it may have been edited)
            continue
        bundle_names = []
        if bundle:
            bundle_names = [i.name for i in bundle.iterdir()
                            if not re.fullmatch(r"index(\.\w+)?\.(md|Rmd|html)", i.name)
                            and not (p["rmd"] and i.name.endswith("_files"))]  # knitr output: regenerated
        ctx = {"assets": [], "needs_rmarkdown_libs": False, "stem": stem,
               "link_map": link_map, "bundle_names": bundle_names}
        qbody = convert_body(p["body"], ctx, executable=p["rmd"])
        if p["rmd"]:
            for pat, repl, why in CODE_FIXES:
                qbody, n_fixed = re.subn(pat, repl, qbody)
                if n_fixed:
                    print(f"fixed {n_fixed} code spot(s) in {p['stem']}: {why}")
        uses_rmd_libs |= ctx["needs_rmarkdown_libs"]

        cats = as_list(fm.get("categories"))
        tags = as_list(fm.get("tags"))
        qfm = {"title": p["title"], "author": AUTHOR, "date": p["date"]}
        if merge_tags:
            cats = cats + [t for t in tags if t not in cats]
            tags = []
        if cats:
            qfm["categories"] = cats
        if tags:
            qfm["keywords"] = tags
        if fm.get("summary"):
            qfm["description"] = re.sub(r"\s+", " ", str(fm["summary"])).strip()
        # keeps the old Hugo URL (/YYYY/MM/DD/slug/) alive as a redirect
        qfm["aliases"] = [f"/{p['y']}/{p['m']}/{p['d']}/{p['slug']}/"]

        (out_dir / f"{stem}.qmd").write_text(dump_front_matter(qfm) + qbody, encoding="utf8")

        shutil.rmtree(files_dir / stem, ignore_errors=True)
        if bundle:
            for name in bundle_names:
                item = bundle / name
                target = files_dir / stem / name
                target.parent.mkdir(parents=True, exist_ok=True)
                if item.is_dir():
                    shutil.copytree(item, target)
                else:
                    shutil.copy2(item, target)
        for folder, rest in ctx["assets"]:
            s_ = src / "static" / "post" / folder / rest
            if s_.exists():
                t = files_dir / stem / folder / rest
                t.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(s_, t)
            else:
                warnings.append(f"missing asset for {p['md'].name}: static/post/{folder}/{rest}")

    if uses_rmd_libs and (src / "static" / "rmarkdown-libs").exists():
        shutil.copytree(src / "static" / "rmarkdown-libs", dst / "rmarkdown-libs", dirs_exist_ok=True)

    # keep the R Markdown sources for reference (underscore folders are ignored by Quarto)
    legacy = dst / "_legacy" / "rmd-sources"
    for rmd in (src / "content" / "post").rglob("*.Rmd"):
        legacy.mkdir(parents=True, exist_ok=True)
        shutil.copy2(rmd, legacy / (rmd.parent.name + "__" + rmd.name if rmd.parent.name != "post" else rmd.name))
    if skipped:
        warnings.append(f"{skipped} posts already exist and were left untouched (use --overwrite-posts to regenerate them)")
    return len(posts) - skipped, warnings


def convert_about(src, dst):
    about = src / "about.md"
    if not about.exists():
        return
    fm, body = split_front_matter(about.read_text(encoding="utf8"))
    ctx = {"assets": [], "needs_rmarkdown_libs": False}
    body = convert_body(fix_about(body.replace("\r\n", "\n")), ctx)
    qfm = {"title": "About"}
    out = dst / "about"
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.qmd").write_text(dump_front_matter(qfm) + body, encoding="utf8")


def copy_site_images(src, dst):
    img = dst / "images"
    img.mkdir(exist_ok=True)
    for name in ("bg.jpg", "favicon.ico", "apple-touch-icon.png", "logo.png"):
        s = src / "public" / "images" / name
        if s.exists():
            shutil.copy2(s, img / name)


# --------------------------------------------------------------------------------------
# scaffolding (written only if missing, unless --force-scaffold)
# --------------------------------------------------------------------------------------
def write_scaffold(dst, force):
    # `scaffold/` in the source tree, `_scaffold/` once copied into a project (Quarto ignores _folders)
    scaffold_dir = next((d for d in (HERE / "scaffold", HERE / "_scaffold") if d.exists()), None)
    if scaffold_dir is None:
        print("note: no scaffold folder next to this script; skipping site scaffolding", file=sys.stderr)
        return []
    written = []
    for f in sorted(scaffold_dir.rglob("*")):
        if f.is_dir():
            continue
        rel = f.relative_to(scaffold_dir)
        target = dst / rel
        if target.exists() and not force:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)
        written.append(str(rel))
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path, help="path to the blogdown repo")
    ap.add_argument("dst", type=Path, help="where to write the Quarto project")
    ap.add_argument("--force-scaffold", action="store_true", help="overwrite existing _quarto.yml, styles, includes ...")
    ap.add_argument("--overwrite-posts", action="store_true", help="regenerate posts that already exist (discards edits)")
    ap.add_argument("--merge-tags", action="store_true", help="add Hugo tags to Quarto categories (default: keep as keywords)")
    a = ap.parse_args()

    a.dst.mkdir(parents=True, exist_ok=True)
    n, warnings = convert_posts(a.src, a.dst, merge_tags=a.merge_tags, overwrite=a.overwrite_posts)
    convert_about(a.src, a.dst)
    copy_site_images(a.src, a.dst)
    written = write_scaffold(a.dst, a.force_scaffold)
    tools = a.dst / "tools"
    tools.mkdir(exist_ok=True)
    if HERE.resolve() != tools.resolve():
        shutil.copy2(__file__, tools / Path(__file__).name)
        if (HERE / "scaffold").exists():
            shutil.copytree(HERE / "scaffold", tools / "_scaffold", dirs_exist_ok=True)
    print(f"converted {n} posts")
    if written:
        print("scaffold files written:", ", ".join(written))
    for w in warnings:
        print("WARNING:", w, file=sys.stderr)


if __name__ == "__main__":
    main()
