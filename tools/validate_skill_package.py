#!/usr/bin/env python3
"""Validate the academic-phrasebank-assistant skill package without network access."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "academic-phrasebank-assistant"
REF_DIR = SKILL_DIR / "references"
MANIFEST_PATH = ROOT / "data" / "processed" / "manifest.json"

REQUIRED_SKILL_FILES = [
    ROOT / "README.md",
    ROOT / "install.sh",
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "agents" / "openai.yaml",
    REF_DIR / "index.md",
    REF_DIR / "revision-framework.md",
    REF_DIR / "source-coverage.md",
    MANIFEST_PATH,
    ROOT / "tools" / "build_phrasebank_refs.py",
]

REQUIRED_DESCRIPTION_TERMS = [
    "writing",
    "rewriting",
    "polishing",
    "style-unifying",
    "line-editing",
    "multi-level revision",
    "manuscript",
    "section",
    "paragraph",
    "sentence",
    "phrase",
]

REQUIRED_FRAMEWORK_HEADINGS = [
    "## Triage",
    "## Pass 1: Manuscript Architecture",
    "## Pass 2: Section Function",
    "## Pass 3: Paragraph Logic",
    "## Pass 4: Sentence Expression",
    "## Pass 5: Phrase And Register",
    "## Style Profile",
    "## Pass 6: Full-Text Consistency Sweep",
    "## Output Patterns",
    "## Quality Gate",
]

REQUIRED_STYLE_TERMS = [
    "terminology",
    "abbreviations",
    "tense",
    "voice",
    "citation stance",
    "hedging strength",
    "sentence rhythm",
    "contribution claims",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(ROOT)}")


def parse_frontmatter(skill_text: str) -> dict[str, str]:
    match = re.match(r"---\n(.*?)\n---\n", skill_text, flags=re.S)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")
    frontmatter = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def validate_skill_metadata() -> None:
    skill_text = read(SKILL_DIR / "SKILL.md")
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != "academic-phrasebank-assistant":
        fail("SKILL.md frontmatter name must be academic-phrasebank-assistant")
    description = frontmatter.get("description", "").lower()
    missing_terms = [term for term in REQUIRED_DESCRIPTION_TERMS if term not in description]
    if missing_terms:
        fail(f"description missing trigger terms: {', '.join(missing_terms)}")
    if "references/revision-framework.md" not in skill_text:
        fail("SKILL.md does not route comprehensive revision to revision-framework.md")


def validate_openai_metadata() -> None:
    metadata = read(SKILL_DIR / "agents" / "openai.yaml")
    if "$academic-phrasebank-assistant" not in metadata:
        fail("agents/openai.yaml default_prompt must mention $academic-phrasebank-assistant")
    match = re.search(r'short_description:\s*"([^"]+)"', metadata)
    if not match:
        fail("agents/openai.yaml missing quoted short_description")
    short_description = match.group(1)
    if not 25 <= len(short_description) <= 64:
        fail("agents/openai.yaml short_description must be 25-64 characters")
    for term in ["line-edit", "polish", "style", "paragraph", "sentence"]:
        if term not in metadata.lower():
            fail(f"agents/openai.yaml missing practical capability term: {term}")


def validate_repository_guidance() -> None:
    readme = read(ROOT / "README.md")
    for text in ["## Install", "./install.sh", "$academic-phrasebank-assistant", "tools/validate_skill_package.py"]:
        if text not in readme:
            fail(f"README.md missing guidance: {text}")
    builder = read(ROOT / "tools" / "build_phrasebank_refs.py")
    if 'REF_DIR.glob("*.md")' in builder:
        fail("builder must not delete every reference markdown file")


def validate_installer() -> None:
    installer = ROOT / "install.sh"
    if not installer.stat().st_mode & 0o111:
        fail("install.sh must be executable")
    installer_text = read(installer)
    for text in ["academic-phrasebank-assistant", "sci-academic-writing", "CODEX_SKILLS_DIR", "CLAUDE_SKILLS_DIR", "CODEX_HOME", "CLAUDE_HOME"]:
        if text not in installer_text:
            fail(f"install.sh missing installer term: {text}")


def validate_references() -> None:
    index_text = read(REF_DIR / "index.md")
    framework_text = read(REF_DIR / "revision-framework.md")
    if "revision-framework.md" not in index_text:
        fail("references/index.md does not include revision-framework.md")
    for heading in REQUIRED_FRAMEWORK_HEADINGS:
        if heading not in framework_text:
            fail(f"revision framework missing heading: {heading}")
    framework_lower = framework_text.lower()
    missing_style_terms = [term for term in REQUIRED_STYLE_TERMS if term not in framework_lower]
    if missing_style_terms:
        fail(f"revision framework missing style consistency terms: {', '.join(missing_style_terms)}")

    manifest = json.loads(read(MANIFEST_PATH))
    included = manifest.get("included", [])
    if len(included) != 17:
        fail(f"manifest should include 17 writing pages, found {len(included)}")
    slugs = {item.get("slug") for item in included}
    reference_slugs = {
        path.stem
        for path in REF_DIR.glob("*.md")
        if path.name not in {"index.md", "source-coverage.md", "revision-framework.md"}
    }
    if slugs != reference_slugs:
        fail(f"manifest/reference mismatch: manifest={sorted(slugs)} refs={sorted(reference_slugs)}")
    if any(item.get("group_count", 0) <= 0 or item.get("phrase_count", 0) <= 0 for item in included):
        fail("manifest contains an included page without phrase groups or phrase lines")


def validate_no_unresolved_markers() -> None:
    marker_pattern = re.compile(r"\b(TODO|FIXME|XXXXX|STUB)\b", flags=re.I)
    for path in [SKILL_DIR / "SKILL.md", *REF_DIR.glob("*.md")]:
        text = read(path)
        match = marker_pattern.search(text)
        if match:
            fail(f"unresolved marker {match.group(0)!r} in {path.relative_to(ROOT)}")


def main() -> int:
    for path in REQUIRED_SKILL_FILES:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")
    validate_skill_metadata()
    validate_openai_metadata()
    validate_repository_guidance()
    validate_installer()
    validate_references()
    validate_no_unresolved_markers()
    print("Skill package audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
