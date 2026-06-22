# Academic Phrasebank Skill

This repository contains the `sci-academic-writing` Codex skill, built from the public Manchester Academic Phrasebank pages.

## Contents

- `sci-academic-writing/`: installable skill folder with `SKILL.md`, UI metadata, and phrasebank references.
- `tools/build_phrasebank_refs.py`: reproducible builder that traverses the Phrasebank sitemap index and regenerates local references.
- `data/raw/`: fetched source HTML/XML used for auditability.
- `data/processed/manifest.json`: machine-readable source coverage summary.

## Rebuild

```bash
python3 tools/build_phrasebank_refs.py
python3 /Users/dawud/.codex/skills/.system/skill-creator/scripts/quick_validate.py sci-academic-writing
```

The builder fails if the sitemap contains an unclassified URL, which keeps coverage drift visible.
