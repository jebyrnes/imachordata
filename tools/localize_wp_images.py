#!/usr/bin/env python3
"""
localize_wp_images.py [--dry-run] [--no-rewrite]

Most old posts hotlink their pictures from the WordPress-era uploads folder
(http://www.imachordata.com/wp-content/uploads/...). Those files are NOT in the repository.
Run this once, from a machine that can reach the internet, to:

  1. download every referenced file into ./wp-content/uploads/... (falling back to the
     Internet Archive if the live site no longer has it),
  2. rewrite the links in the .qmd files to /wp-content/uploads/... so the site no longer
     depends on the old host.

Safe to re-run: files that already exist are skipped, only successfully-available files are rewritten.
Standard library only.
"""
import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"https?://(?:www\.)?imachordata\.com/(wp-content/uploads/[^\s\"'<>()\]]+)", re.I)
UA = {"User-Agent": "Mozilla/5.0 (imachordata-migration)"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-rewrite", action="store_true")
    a = ap.parse_args()

    qmds = [p for p in ROOT.rglob("*.qmd") if not any(s in p.parts for s in ("_site", "_legacy", ".quarto"))]
    texts = {p: p.read_text(encoding="utf8") for p in qmds}
    rels = sorted({m.group(1) for t in texts.values() for m in URL_RE.finditer(t)})
    print(f"{len(rels)} distinct files referenced in {len(qmds)} documents")

    ok, failed = set(), []
    for i, rel in enumerate(rels, 1):
        target = ROOT / rel
        if target.exists() and target.stat().st_size > 0:
            ok.add(rel)
            continue
        if a.dry_run:
            print(f"[{i}/{len(rels)}] would download {rel}")
            continue
        data = None
        for url in (f"http://www.imachordata.com/{rel}", f"https://web.archive.org/web/0id_/http://www.imachordata.com/{rel}"):
            try:
                data = fetch(url)
                break
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                err = e
        if data:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            ok.add(rel)
            print(f"[{i}/{len(rels)}] ok   {rel}")
        else:
            failed.append(rel)
            print(f"[{i}/{len(rels)}] FAIL {rel} ({err})")
        time.sleep(0.2)

    if not a.dry_run and not a.no_rewrite:
        changed = 0
        for p, t in texts.items():
            new = URL_RE.sub(lambda m: "/" + m.group(1) if m.group(1) in ok else m.group(0), t)
            if new != t:
                p.write_text(new, encoding="utf8")
                changed += 1
        print(f"rewrote links in {changed} documents")
    if failed:
        print(f"\n{len(failed)} files could not be downloaded (their links were left pointing at the old URL):")
        print("\n".join("  " + f for f in failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
