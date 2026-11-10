# I'm a Chordata! Urochordata! — Quarto version

This is the blogdown/Hugo site (`jebyrnes/imachordata`) converted to a Quarto website.

## Use it

Open `imachordata.Rproj` in RStudio (or just open the folder in any editor), then:

```bash
quarto preview      # live preview while you work
quarto render       # builds the site into docs/
```

The site renders into `docs/` (commit it if you publish with GitHub Pages: Settings > Pages > "Deploy from a
branch" > `/docs`). If you use a custom domain, put a `CNAME` file in the project root and add it to
`resources:` in `_quarto.yml` so it is copied into `docs/`.

Requires Quarto >= 1.5 (built and tested with 1.11).

Five posts contain live R code (covid19R, covid19 mobility, simulating posteriors, tidyeval, modelbased).
Each full `quarto render` re-runs that code and regenerates their figures, so R and a few packages are needed:

```r
source("install-packages.R")
```

(The other 210 posts are plain Markdown; their code blocks are display-only, as they were on the old site.)

## First thing to do: localize the old WordPress images

About 170 pictures in old posts are hotlinked from `http://www.imachordata.com/wp-content/uploads/...`.
Those files were never in the repository, so the site depends on the old host staying up.
Run this once on a machine with internet access:

```bash
python3 tools/localize_wp_images.py
```

It downloads each file into `wp-content/uploads/` (falling back to the Internet Archive) and rewrites the
links. Re-run it any time; it only touches what's missing. `--dry-run` shows what it would do.

## Where things are

| Hugo / blogdown | Quarto |
|---|---|
| `config.toml` | `_quarto.yml` |
| `content/post/*.md` | `posts/YYYYMMDD_slug.qmd` |
| `about.md` | `about/index.qmd` |
| theme "hamburg" | `styles/chordata.scss`, `_header.html` |
| Disqus + Older/Newer buttons | `_post-footer.html` |
| `static/post/*_files`, post `images/` | `posts/files/<post name>/` |
| the 5 `.Rmd` posts | executable `posts/*.qmd` (chunk options converted to `#|` lines); originals in `_legacy/rmd-sources/` |

## Writing a new post

Create `posts/20261108_my-slug.qmd` (the date prefix keeps the folder sorted):

```yaml
---
title: "My post"
author: Jarrett Byrnes
date: 2026-11-08
categories: [R]
description: "Optional summary shown on the home page"
---
```

It appears on the home page, in the RSS feed (`/index.xml`), on the Categories page, and in the
Older/Newer navigation automatically. R chunks work normally if you want live code
(`posts/_metadata.yml` sets `freeze: auto` so they only re-run when the post changes).

## Linking within the site

Link to the `.qmd` file; Quarto writes the `.html` link for you:

```markdown
[my earlier post](20120203_prey-loss-in-different-food-web-structures-weve-been-here-before.qmd)
[from anywhere](/posts/20120203_prey-loss-in-different-food-web-structures-weve-been-here-before.qmd)
[with an anchor](20120203_some-post.qmd#a-heading)
[about page](/about/index.qmd)
```

Paths starting with `/` are relative to the project root. The converter already rewrote the links
between old posts this way.

## Things that changed (on purpose)

* **Post URLs moved** from `/YYYY/MM/DD/slug/` to `/posts/YYYYMMDD_slug.html`. Every old URL still works:
  each post has an `aliases:` entry that makes Quarto write a redirect page at the old address, and Disqus
  is told to use the old URL so existing comment threads keep matching. New posts don't need an alias.
* **R posts are live, not static.** They were converted from their `.Rmd` sources, so figures are regenerated on
  every render. To skip re-running unchanged posts and speed up builds, add `freeze: auto` to `posts/_metadata.yml`.
* **One code fix** so the simulation post runs with current ggplot2: `labs("...")` became `labs(title = "...")`
  (ggplot2 4.0 rejects unnamed labels; older versions ignored them).
* **Authors:** every post is credited to Jarrett Byrnes (set in each post and as the default in `posts/_metadata.yml`).
  This changes the credit on one guest post (`20170331_introducing-the-open-derby-guest-post.qmd`, originally
  Jillian Dunic) and one post that said "Package Build".
* **Captions fixed.** The old site printed the raw WordPress `[caption ...]` text; they're now real captions.
* **Tags** are kept as `keywords` (Quarto only has categories). `--merge-tags` on the converter merges them in.
* **Pagination** is client-side (5 posts per page); the old `/page/N/` and `/categories/<name>/` URLs
  don't exist. The Categories page filters by clicking a category.
* **Google Analytics:** the old config used a Universal Analytics ID, which Google shut down in 2023.
  Add `google-analytics: "G-XXXX"` to `_quarto.yml` for GA4.
* The `Twitter` button is still in the banner (as before). Edit `_header.html` to change it.
* `site-url` is `https://imachordata.com`; the header uses root-relative paths (`/images/bg.jpg`),
  so serve it from the domain root.
* A few links in the original posts were already broken (bare DOIs without `https://doi.org/`, `www.` links
  without a scheme, an old WordPress `?p=122` link). I left them as written.
* Disqus matches threads by page URL. If old comments don't show up, it's usually `http` vs `https`
  or `www.` — change `legacy` in `_post-footer.html` to the URL form the threads were created with (e.g. `http://www.imachordata.com`).

## Re-running the conversion

If you keep posting from the blogdown repo for a while:

```bash
python3 tools/convert_blogdown_to_quarto.py /path/to/imachordata .
```

Posts that already exist are left untouched (so your edits are safe); only missing ones are created.
`--overwrite-posts` regenerates everything, `--force-scaffold` also resets config, styles and includes.
