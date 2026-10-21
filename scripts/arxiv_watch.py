#!/usr/bin/env python3
"""Weekly arXiv watch for the Awesome-OCR list.

Queries the arXiv API for recent OCR / document-parsing papers and rewrites
resources/arxiv-watch.md. The output file is a candidate inbox, not part of
the curated tables; promotion into README.md stays manual (see Update Policy).

Stdlib only, so the GitHub Action needs no dependency install.
"""

import datetime as dt
import pathlib
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "resources" / "arxiv-watch.md"

WINDOW_DAYS = 30
MAX_RESULTS = 200

# Title-level terms keep precision high; abstract-level terms drown the list.
TITLE_TERMS = [
    "OCR",
    "optical character recognition",
    "text recognition",
    "text spotting",
    "scene text",
    "handwritten text",
    "handwriting recognition",
    "document parsing",
    "document image",
    "layout analysis",
    "reading order",
    "table recognition",
    "table structure recognition",
    "formula recognition",
    "chart parsing",
    "key information extraction",
]

CATEGORIES = ["cs.CV", "cs.CL", "cs.IR", "cs.MM"]

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}


def build_query() -> str:
    terms = " OR ".join(f'ti:"{t}"' if " " in t else f"ti:{t}" for t in TITLE_TERMS)
    cats = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    return f"({terms}) AND ({cats})"


def fetch(query: str) -> bytes:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": 0,
            "max_results": MAX_RESULTS,
        }
    )
    req = urllib.request.Request(
        f"{API}?{params}",
        headers={"User-Agent": "awesome-ocr-arxiv-watch/1.0"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(30 * (attempt + 1))
    raise RuntimeError("unreachable")


def parse(feed: bytes, since: dt.date):
    rows = []
    for entry in ET.fromstring(feed).findall("a:entry", NS):
        published = entry.findtext("a:published", default="", namespaces=NS)[:10]
        if not published or dt.date.fromisoformat(published) < since:
            continue
        title = re.sub(r"\s+", " ", entry.findtext("a:title", default="", namespaces=NS)).strip()
        link = entry.findtext("a:id", default="", namespaces=NS).strip()
        arxiv_id = link.rsplit("/abs/", 1)[-1]
        cats = ", ".join(
            c.get("term", "") for c in entry.findall("a:category", NS)[:3]
        )
        authors = [
            a.findtext("a:name", default="", namespaces=NS)
            for a in entry.findall("a:author", NS)
        ]
        first_author = authors[0] if authors else ""
        if len(authors) > 1:
            first_author += " et al."
        rows.append((published, title, first_author, cats, arxiv_id, link))
    return rows


def write(rows) -> None:
    today = dt.date.today().isoformat()
    lines = [
        "# arXiv Watch (auto-generated)",
        "",
        f"Last refresh: {today}. Window: last {WINDOW_DAYS} days. "
        f"Matched by title terms in {', '.join(CATEGORIES)}; newest first.",
        "",
        "This file is rewritten weekly by `.github/workflows/arxiv-watch.yml` "
        "running `scripts/arxiv_watch.py`. Entries are **unreviewed candidates**; "
        "they enter the curated README tables only after the source checks in the "
        "Update Policy.",
        "",
        "| Submitted | Title | First author | Categories | Link |",
        "|:---:|:---|:---|:---:|:---:|",
    ]
    for published, title, author, cats, arxiv_id, link in rows:
        title_md = title.replace("|", "\\|")
        lines.append(
            f"| {published} | {title_md} | {author} | {cats} | [{arxiv_id}]({link}) |"
        )
    if not rows:
        lines.append("| - | no matches in window | - | - | - |")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(rows)} entries")


def main() -> None:
    since = dt.date.today() - dt.timedelta(days=WINDOW_DAYS)
    rows = parse(fetch(build_query()), since)
    write(rows)


if __name__ == "__main__":
    main()
