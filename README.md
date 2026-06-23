# Academic Phrasebank Skill

This repository contains the `sci-academic-writing` Codex skill, built from the public Manchester Academic Phrasebank pages.

## Contents

- `sci-academic-writing/`: installable skill folder with `SKILL.md`, UI metadata, and phrasebank references.
- `tools/build_phrasebank_refs.py`: reproducible builder that traverses the Phrasebank sitemap index and regenerates local references.
- `tools/validate_skill_package.py`: offline audit for skill completeness, routing, metadata, and reference consistency.
- `data/raw/`: normalized fetched source HTML/XML used for auditability.
- `data/processed/manifest.json`: machine-readable source coverage summary.

## Install

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R sci-academic-writing "${CODEX_HOME:-$HOME/.codex}/skills/"
```

After installation, invoke it with `$sci-academic-writing` for SCI manuscript drafting, rewriting, polishing, structural revision, paragraph logic repair, and sentence-level editing.

## Rebuild

```bash
python3 tools/build_phrasebank_refs.py
python3 /Users/dawud/.codex/skills/.system/skill-creator/scripts/quick_validate.py sci-academic-writing
python3 tools/validate_skill_package.py
```

`tools/validate_skill_package.py` is the offline completion audit for the packaged skill: it checks trigger metadata, UI metadata, reference routing, the multi-level revision framework, manifest/reference consistency, and unresolved markers. The builder performs a live Phrasebank fetch and fails if the sitemap contains an unclassified URL, which keeps coverage drift visible.
