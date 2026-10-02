#!/usr/bin/env python3
"""Build local reference files from the public Academic Phrasebank pages."""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


BASE_URL = "https://www.phrasebank.manchester.ac.uk"
SITEMAP_INDEX_URL = f"{BASE_URL}/sitemap.xml"
PAGE_SITEMAP_URL = f"{BASE_URL}/page-sitemap.xml"
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
REF_DIR = ROOT / "academic-phrasebank-skill" / "references"

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


def normalise_raw_html(text: str) -> str:
    # Keep checked-in snapshots stable across servers that use CRLF.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r'"token":"[^"]+"', '"token":"<token>"', text)
    text = re.sub(r'"et_frontend_nonce":"[^"]+"', '"et_frontend_nonce":"<nonce>"', text)
    text = re.sub(r'"et_ab_log_nonce":"[^"]+"', '"et_ab_log_nonce":"<nonce>"', text)
    text = re.sub(r"hid=[A-F0-9]+", "hid=<hid>", text)
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


def slug_from_url(url: str) -> str:
    path = re.sub(r"^https?://[^/]+", "", url).strip("/")
    return path


_BLOCK_TAG_RE = re.compile(r"</?(?:br|p|li|div|tr|td|th)\b[^>]*>", flags=re.I)
_TAG_RE = re.compile(r"<[^>]+>")
_HIDDEN_ELEMENT_RE = re.compile(
    r"<(?P<tag>span|div|p|td|th)\b(?=[^>]*(?:color\s*:\s*white|display\s*:\s*none|visibility\s*:\s*hidden))[^>]*>.*?</(?P=tag)\s*>",
    flags=re.I | re.S,
)


def strip_tags(text: str) -> str:
    """Convert an HTML fragment to lines without splitting inline words.

    Phrasebank uses inline ``em`` tags inside words (for example ``B`` +
    ``e`` + ``ing``) and white ``break`` spans as table layout markers.  A
    generic tag replacement with a space corrupts both cases, so only block
    boundaries become newlines and all other tags are removed in place.
    """
    text = _HIDDEN_ELEMENT_RE.sub("", text)

    def replace_block(match: re.Match[str]) -> str:
        return "\n"

    text = _BLOCK_TAG_RE.sub(replace_block, text)
    text = _TAG_RE.sub("", text)
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
        if not line or line == "&nbsp;" or line.casefold() == "break":
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


def collect_sitemap_urls(raw_dir: Path) -> tuple[list[str], list[str]]:
    index_text = fetch(SITEMAP_INDEX_URL)
    (raw_dir / "sitemap.xml").write_text(index_text, encoding="utf-8")
    index_root = ET.fromstring(index_text)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [loc.text.strip() for loc in index_root.findall(".//sm:loc", namespace) if loc.text]
    if PAGE_SITEMAP_URL not in sitemap_urls:
        sitemap_urls.append(PAGE_SITEMAP_URL)

    urls = []
    for sitemap_url in sitemap_urls:
        xml_text = fetch(sitemap_url)
        (raw_dir / sitemap_name(sitemap_url)).write_text(xml_text, encoding="utf-8")
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


def extract_page(url: str, raw_dir: Path) -> PageContent:
    slug = slug_from_url(url)
    page_html = fetch(url)
    (raw_dir / f"{slug.replace('/', '-') or 'home'}.html").write_text(normalise_raw_html(page_html), encoding="utf-8")
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
    text = text.replace("XXXXX", "X")
    text = re.sub(r"\bbook X\s*,", "book on X,", text)
    return text.replace("\n", " ").strip()


def write_catalog(
    pages: list[PageContent],
    excluded: list[str],
    sitemap_urls: list[str],
    refs_dir: Path = REF_DIR,
) -> None:
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
    (refs_dir / "source-coverage.md").write_text("\n".join(lines), encoding="utf-8")


def write_page_reference(page: PageContent, refs_dir: Path = REF_DIR) -> None:
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
    (refs_dir / f"{page.slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_manifest(
    pages: list[PageContent],
    excluded: list[str],
    sitemap_urls: list[str],
    processed_dir: Path = PROCESSED_DIR,
) -> None:
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
    (processed_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


def write_index(pages: list[PageContent], refs_dir: Path = REF_DIR) -> None:
    lines = [
        "# Phrasebank Reference Index",
        "",
        "Load only the file that matches the manuscript task. Use these references as phrase-pattern evidence, not as text to paste wholesale.",
        "",
        "## Revision Framework",
        "",
        "- `revision-framework.md`: Multi-level manuscript rewriting, polishing, restructuring, diagnosis, paragraph logic repair, sentence-level editing, and full-manuscript revision workflow.",
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
    (refs_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def order_pages(pages: Iterable[PageContent]) -> list[PageContent]:
    return sorted(pages, key=lambda page: SECTION_ORDER.index(page.slug) if page.slug in SECTION_ORDER else 999)


def stage_outputs(
    stage_root: Path,
    temp_raw_dir: Path,
    pages: list[PageContent],
    excluded_urls: list[str],
    sitemap_urls: list[str],
) -> None:
    """Materialise every generated output below ``stage_root``.

    Nothing under the repository's live data or reference directories is
    touched until this function and all validation of its inputs succeed.
    ``revision-framework.md`` is intentionally not generated here; it is a
    hand-maintained reference and is preserved during commit.
    """
    stage_raw_dir = stage_root / "raw"
    stage_processed_dir = stage_root / "processed"
    stage_refs_dir = stage_root / "references"
    for directory in (stage_raw_dir, stage_processed_dir, stage_refs_dir):
        directory.mkdir(parents=True, exist_ok=True)

    for source in temp_raw_dir.iterdir():
        if source.is_file():
            shutil.copy2(source, stage_raw_dir / source.name)

    write_index(pages, stage_refs_dir)
    write_catalog(pages, excluded_urls, sitemap_urls, stage_refs_dir)
    for page in pages:
        write_page_reference(page, stage_refs_dir)
    write_manifest(pages, excluded_urls, sitemap_urls, stage_processed_dir)


def _prepare_directory_replacement(
    staged_dir: Path,
    live_dir: Path,
    preserve: Optional[set[str]] = None,
) -> Path:
    """Build a complete replacement directory beside the live directory."""
    live_dir.parent.mkdir(parents=True, exist_ok=True)
    replacement = live_dir.parent / f".{live_dir.name}.next-{os.getpid()}"
    shutil.rmtree(replacement, ignore_errors=True)
    replacement.mkdir(parents=True)
    preserve = preserve or set()
    if live_dir.exists():
        for child in live_dir.iterdir():
            if child.name in preserve:
                target = replacement / child.name
                if child.is_dir():
                    shutil.copytree(child, target)
                else:
                    shutil.copy2(child, target)
            elif child.is_dir() and live_dir.name == "references":
                # Keep non-Markdown auxiliary assets in a skill reference tree.
                shutil.copytree(child, replacement / child.name)
            elif child.is_file() and live_dir.name != "references":
                # Keep non-generated files in data directories.
                if not (live_dir.name == "raw" and child.suffix.lower() in {".html", ".xml"}):
                    shutil.copy2(child, replacement / child.name)
    for child in staged_dir.iterdir():
        destination = replacement / child.name
        if child.is_dir():
            shutil.copytree(child, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(child, destination)
    return replacement


def _replace_directory(
    staged_dir: Path,
    live_dir: Path,
    preserve: Optional[set[str]] = None,
) -> None:
    """Replace one generated directory while preserving named files."""
    replacement = _prepare_directory_replacement(staged_dir, live_dir, preserve)
    backup = live_dir.parent / f".{live_dir.name}.old-{os.getpid()}"
    shutil.rmtree(backup, ignore_errors=True)
    try:
        if live_dir.exists():
            os.replace(live_dir, backup)
        os.replace(replacement, live_dir)
    except Exception:
        if not live_dir.exists() and backup.exists():
            os.replace(backup, live_dir)
        raise
    finally:
        shutil.rmtree(backup, ignore_errors=True)
        shutil.rmtree(replacement, ignore_errors=True)


def commit_staged_outputs(stage_root: Path) -> None:
    """Commit all generated trees as one rollback-capable filesystem transaction."""
    specs = [
        (stage_root / "raw", RAW_DIR, None),
        (stage_root / "processed", PROCESSED_DIR, None),
        (stage_root / "references", REF_DIR, {"revision-framework.md"}),
    ]
    entries = []
    swapped = []
    try:
        for staged_dir, live_dir, preserve in specs:
            entries.append(
                {
                    "live": live_dir,
                    "replacement": _prepare_directory_replacement(staged_dir, live_dir, preserve),
                    "backup": live_dir.parent / f".{live_dir.name}.old-{os.getpid()}",
                    "moved_live": False,
                }
            )
        for entry in entries:
            live_dir = entry["live"]
            backup = entry["backup"]
            replacement = entry["replacement"]
            shutil.rmtree(backup, ignore_errors=True)
            if live_dir.exists():
                os.replace(live_dir, backup)
                entry["moved_live"] = True
            try:
                os.replace(replacement, live_dir)
            except Exception:
                if entry["moved_live"] and backup.exists() and not live_dir.exists():
                    os.replace(backup, live_dir)
                    entry["moved_live"] = False
                raise
            swapped.append(entry)
    except Exception:
        for entry in reversed(swapped):
            live_dir = entry["live"]
            replacement = entry["replacement"]
            backup = entry["backup"]
            if live_dir.exists():
                os.replace(live_dir, replacement)
            if entry["moved_live"] and backup.exists():
                os.replace(backup, live_dir)
        raise
    finally:
        for entry in entries:
            shutil.rmtree(entry["backup"], ignore_errors=True)
            shutil.rmtree(entry["replacement"], ignore_errors=True)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="phrasebank-build-") as temp_dir_name:
        temp_root = Path(temp_dir_name)
        temp_raw_dir = temp_root / "raw"
        temp_raw_dir.mkdir()

        urls, sitemap_urls = collect_sitemap_urls(temp_raw_dir)
        included_urls = [url for url in urls if slug_from_url(url) in SECTION_ORDER]
        excluded_urls = sorted(url for url in urls if slug_from_url(url) in EXCLUDED_SLUGS)
        unknown_urls = [url for url in urls if slug_from_url(url) not in SECTION_ORDER and slug_from_url(url) not in EXCLUDED_SLUGS]
        if unknown_urls:
            print("Unknown sitemap URLs require classification:", file=sys.stderr)
            for url in unknown_urls:
                print(f"- {url}", file=sys.stderr)
            return 2

        pages = order_pages(extract_page(url, temp_raw_dir) for url in included_urls)
        missing_groups = [page.slug for page in pages if not page.groups]
        if missing_groups:
            print(f"Pages without phrase groups: {', '.join(missing_groups)}", file=sys.stderr)
            return 3

        stage_root = temp_root / "staged"
        stage_outputs(stage_root, temp_raw_dir, pages, excluded_urls, sitemap_urls)
        commit_staged_outputs(stage_root)
    print(f"Wrote {len(pages)} page references to {REF_DIR}")
    print(f"Total phrase lines: {sum(len(group.phrases) for page in pages for group in page.groups)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
