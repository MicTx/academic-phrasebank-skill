# Academic Phrasebank Skill

This repository contains the `academic-phrasebank-assistant` Codex skill, built from the public Manchester Academic Phrasebank pages.

## Contents

- `academic-phrasebank-assistant/`: installable skill folder with `SKILL.md`, UI metadata, and phrasebank references.
- `tools/build_phrasebank_refs.py`: reproducible builder that traverses the Phrasebank sitemap index and regenerates local references.
- `tools/validate_skill_package.py`: offline audit for skill completeness, routing, metadata, and reference consistency.
- `data/raw/`: normalized fetched source HTML/XML used for auditability.
- `data/processed/manifest.json`: machine-readable source coverage summary.

## Install

```bash
./install.sh
```

The installer copies the skill to both Codex and Claude Code by default:

- Codex: `${CODEX_SKILLS_DIR:-${CODEX_HOME:-$HOME/.codex}/skills}`
- Claude Code: `${CLAUDE_SKILLS_DIR:-${CLAUDE_HOME:-$HOME/.claude}/skills}`

After installation, invoke it with `$academic-phrasebank-assistant` for SCI manuscript drafting, rewriting, polishing, line editing, full-text style unification, structural revision, paragraph logic repair, and sentence-level editing.

## Rebuild

```bash
python3 tools/build_phrasebank_refs.py
python3 /Users/dawud/.codex/skills/.system/skill-creator/scripts/quick_validate.py academic-phrasebank-assistant
python3 tools/validate_skill_package.py
```

`tools/validate_skill_package.py` is the offline completion audit for the packaged skill: it checks trigger metadata, UI metadata, reference routing, the multi-level revision framework, manifest/reference consistency, and unresolved markers. The builder performs a live Phrasebank fetch and fails if the sitemap contains an unclassified URL, which keeps coverage drift visible.
