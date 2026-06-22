#!/usr/bin/env python3
"""Build local reference files from the public Academic Phrasebank pages."""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


BASE_URL = "https://www.phrasebank.manchester.ac.uk"
SITEMAP_INDEX_URL = f"{BASE_URL}/sitemap.xml"
PAGE_SITEMAP_URL = f"{BASE_URL}/page-sitemap.xml"
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
REF_DIR = ROOT / "sci-academic-writing" / "references"

EXCLUDED_SLUGS = {
    "",
    "2021/08/26/testing",
    "about-academic-phrasebank",
    "amazon",
    "author/humwebteam",
    "author/mtfssjes",
    "category/uncategorised",
    "dr-john-morley",
    "useful-links",
}

CORE_SLUGS = {
    "introducing-work",
    "referring-to-sources",
    "describing-methods",
    "reporting-results",
    "discussing-findings",
    "writing-conclusions",
}

SECTION_ORDER = [
    "introducing-work",
    "referring-to-sources",
    "describing-methods",
    "reporting-results",
    "discussing-findings",
    "writing-conclusions",
    "being-critical",
    "classifying-and-listing",
    "compare-and-contrast",
    "describing-quantities",
    "describing-trends",
    "explaining-cause-and-effect",
    "giving-examples",
    "signalling-transition",
    "using-cautious-language",
    "writing-about-the-past-2",
    "writing-definitions",
]


@dataclass
class PhraseGroup:
    title: str
    phrases: list[str]


@dataclass
class PageContent:
    title: str
    slug: str
    url: str
    summary: list[str]
    groups: list[PhraseGroup]


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; CodexPhrasebankBuilder/1.0)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"failed to fetch {url}: {exc}") from exc


def slug_from_url(url: str) -> str:
    path = re.sub(r"^https?://[^/]+", "", url).strip("/")
    return path


def strip_tags(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p\s*>", "\n", text, flags=re.I)
    text = re.sub(r"</li\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    lines = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if line and line != "...":
            lines.append(line)
    return "\n".join(lines)


def split_phrases(fragment: str) -> list[str]:
    text = strip_tags(fragment)
    phrases = []
    for line in text.splitlines():
        line = line.strip(" -*\t")
        if not line or line == "&nbsp;":
            continue
        if line.startswith("(") and len(line) < 100:
            continue
        if line.startswith("*") and len(line) < 140:
            continue
        phrases.append(line)
    return phrases


def sitemap_name(url: str) -> str:
    name = slug_from_url(url).replace("/", "-") or "sitemap.xml"
    return name if name.endswith(".xml") else f"{name}.xml"


def collect_sitemap_urls() -> tuple[list[str], list[str]]:
    index_text = fetch(SITEMAP_INDEX_URL)
    (RAW_DIR / "sitemap.xml").write_text(index_text, encoding="utf-8")
    index_root = ET.fromstring(index_text)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [loc.text.strip() for loc in index_root.findall(".//sm:loc", namespace) if loc.text]
    if PAGE_SITEMAP_URL not in sitemap_urls:
        sitemap_urls.append(PAGE_SITEMAP_URL)

    urls = []
    for sitemap_url in sitemap_urls:
        xml_text = fetch(sitemap_url)
        (RAW_DIR / sitemap_name(sitemap_url)).write_text(xml_text, encoding="utf-8")
        root = ET.fromstring(xml_text)
        for loc in root.findall(".//sm:loc", namespace):
            if loc.text and loc.text.startswith(BASE_URL):
                urls.append(loc.text.strip())
    ordered_urls = sorted(
        set(urls),
        key=lambda value: SECTION_ORDER.index(slug_from_url(value))
        if slug_from_url(value) in SECTION_ORDER
        else 999,
    )
    return ordered_urls, sitemap_urls


def extract_summary(main_html: str) -> list[str]:
    before_toggles = main_html.split('class="et_pb_toggle', 1)[0]
    h1_matches = list(re.finditer(r"<h1[^>]*>.*?</h1>", before_toggles, flags=re.I | re.S))
    if h1_matches:
        before_toggles = before_toggles[h1_matches[-1].end() :]
    paragraphs = re.findall(r"<(p|li)\b[^>]*>(.*?)</\1>", before_toggles, flags=re.I | re.S)
    summary = []
    for _tag, fragment in paragraphs:
        text = strip_tags(fragment)
        if not text or text == "&nbsp;":
            continue
        if any(skip in text for skip in ["Contact Us", "+44 (0)", "Oxford Road"]):
            continue
        summary.extend(text.splitlines())
    return summary[:18]


def extract_groups(main_html: str) -> list[PhraseGroup]:
    pattern = re.compile(
        r'<h5 class="et_pb_toggle_title">(.*?)</h5>\s*'
        r'<div class="et_pb_toggle_content clearfix">(.*?)</div>',
        flags=re.I | re.S,
    )
    groups = []
    for title_html, body_html in pattern.findall(main_html):
        title = strip_tags(title_html).replace("\n", " ")
        phrases = split_phrases(body_html)
        if title and phrases:
            groups.append(PhraseGroup(title=title, phrases=phrases))
    return groups


def extract_title(page_html: str, slug: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", page_html, flags=re.I | re.S)
    if match:
        return strip_tags(match.group(1)).replace("\n", " ")
    return slug.replace("-", " ").title()


def extract_page(url: str) -> PageContent:
    slug = slug_from_url(url)
    page_html = fetch(url)
    (RAW_DIR / f"{slug.replace('/', '-') or 'home'}.html").write_text(page_html, encoding="utf-8")
    main_match = re.search(r'<div class="entry-content">(.*?)</article>', page_html, flags=re.I | re.S)
    main_html = main_match.group(1) if main_match else page_html
    return PageContent(
        title=extract_title(main_html, slug),
        slug=slug,
        url=url,
        summary=extract_summary(main_html),
        groups=extract_groups(main_html),
    )


def md_escape(text: str) -> str:
    return text.replace("\n", " ").strip()


def write_catalog(pages: list[PageContent], excluded: list[str], sitemap_urls: list[str]) -> None:
    lines = [
        "# Source Coverage",
        "",
        f"Source sitemap index: {SITEMAP_INDEX_URL}",
        "",
        "## Traversed Sitemaps",
        "",
    ]
    for sitemap_url in sitemap_urls:
        lines.append(f"- {sitemap_url}")
    lines.extend([
        "",
        f"Fetched pages: {len(pages)} writing pages",
        "",
        "## Included Writing Pages",
        "",
    ])
    for page in pages:
        label = "core section" if page.slug in CORE_SLUGS else "language function"
        phrase_count = sum(len(group.phrases) for group in page.groups)
        lines.append(
            f"- `{page.slug}` ({label}): {page.title}; "
            f"{len(page.groups)} groups; {phrase_count} phrase lines; {page.url}"
        )
    lines.extend(["", "## Excluded Non-Writing Pages", ""])
    for url in excluded:
        lines.append(f"- `{slug_from_url(url) or 'home'}`: {url}")
    lines.append("")
    (REF_DIR / "source-coverage.md").write_text("\n".join(lines), encoding="utf-8")


def write_page_reference(page: PageContent) -> None:
    lines = [
        f"# {page.title}",
        "",
        f"Source: {page.url}",
        "",
    ]
    if page.summary:
        lines.extend(["## Role in a Manuscript", ""])
        for item in page.summary:
            lines.append(f"- {md_escape(item)}")
        lines.append("")
    lines.extend(["## Phrase Groups", ""])
    for group in page.groups:
        lines.append(f"### {md_escape(group.title)}")
        for phrase in group.phrases:
            lines.append(f"- {md_escape(phrase)}")
        lines.append("")
    (REF_DIR / f"{page.slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_manifest(pages: list[PageContent], excluded: list[str], sitemap_urls: list[str]) -> None:
    manifest = {
        "source_sitemap_index": SITEMAP_INDEX_URL,
        "sitemaps": sitemap_urls,
        "included": [
            {
                "slug": page.slug,
                "title": page.title,
                "url": page.url,
                "group_count": len(page.groups),
                "phrase_count": sum(len(group.phrases) for group in page.groups),
            }
            for page in pages
        ],
        "excluded": [{"slug": slug_from_url(url), "url": url} for url in excluded],
    }
    (PROCESSED_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def write_index(pages: list[PageContent]) -> None:
    lines = [
        "# Phrasebank Reference Index",
        "",
        "Load only the file that matches the manuscript task. Use these references as phrase-pattern evidence, not as text to paste wholesale.",
        "",
        "## Core Manuscript Sections",
        "",
    ]
    for page in pages:
        if page.slug in CORE_SLUGS:
            lines.append(f"- `{page.slug}.md`: {page.title}")
    lines.extend(["", "## Cross-Section Language Functions", ""])
    for page in pages:
        if page.slug not in CORE_SLUGS:
            lines.append(f"- `{page.slug}.md`: {page.title}")
    lines.append("")
    (REF_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def order_pages(pages: Iterable[PageContent]) -> list[PageContent]:
    return sorted(pages, key=lambda page: SECTION_ORDER.index(page.slug) if page.slug in SECTION_ORDER else 999)


def main() -> int:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REF_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in [*RAW_DIR.glob("*.html"), *RAW_DIR.glob("*.xml")]:
        old_file.unlink()
    urls, sitemap_urls = collect_sitemap_urls()
    included_urls = [url for url in urls if slug_from_url(url) in SECTION_ORDER]
    excluded_urls = [url for url in urls if slug_from_url(url) in EXCLUDED_SLUGS]
    unknown_urls = [url for url in urls if slug_from_url(url) not in SECTION_ORDER and slug_from_url(url) not in EXCLUDED_SLUGS]
    if unknown_urls:
        print("Unknown sitemap URLs require classification:", file=sys.stderr)
        for url in unknown_urls:
            print(f"- {url}", file=sys.stderr)
        return 2

    pages = order_pages(extract_page(url) for url in included_urls)
    missing_groups = [page.slug for page in pages if not page.groups]
    if missing_groups:
        print(f"Pages without phrase groups: {', '.join(missing_groups)}", file=sys.stderr)
        return 3

    for old_file in REF_DIR.glob("*.md"):
        old_file.unlink()
    write_index(pages)
    write_catalog(pages, excluded_urls, sitemap_urls)
    for page in pages:
        write_page_reference(page)
    write_manifest(pages, excluded_urls, sitemap_urls)
    print(f"Wrote {len(pages)} page references to {REF_DIR}")
    print(f"Total phrase lines: {sum(len(group.phrases) for page in pages for group in page.groups)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
