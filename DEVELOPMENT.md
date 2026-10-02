# Development Guide

This guide covers repository maintenance for contributors.

## Requirements

- Python 3.9 or newer.
- Git.
- The local `skill-creator` installation for the standard skill validator.
- Network access only when rebuilding the upstream reference snapshot.

## Reference data

Rebuild the local Phrasebank references with:

```bash
python3 tools/build_phrasebank_refs.py
```

The builder stages raw pages, generated references, and the coverage manifest before replacing the existing generated trees. The hand-maintained `academic-phrasebank-skill/references/revision-framework.md` is preserved across rebuilds.

## Validation

```bash
python3 /Users/dawud/.agents/skills/skill-creator/scripts/quick_validate.py academic-phrasebank-skill
python3 tools/validate_skill_package.py
python3 -m unittest discover -s tests -v
python3 -m py_compile tools/build_phrasebank_refs.py tools/validate_skill_package.py tools/build_release.py
git diff --check
```

Set `SKILL_CREATOR_DIR` when the local skill-creator installation is elsewhere.

## Evaluation

Evaluation prompts live in `academic-phrasebank-skill/evals/evals.json`. Keep evaluation workspaces outside the repository. Compare the current skill with a saved baseline, grade preservation and boundary assertions, and review the generated outputs before changing the skill again.

## User package

Build the user package with:

```bash
python3 tools/build_release.py
```

The builder validates the source, runs installation smoke tests, creates deterministic `.tar.gz` and `.zip` archives, checks archive contents and executable modes, and writes `SHA256SUMS` plus a manifest under `dist/`. User packages contain the installer, public documentation, attribution, changelog, and installable skill. Tests, evaluation prompts, raw source snapshots, manifests, and build tools stay in the source repository.

## Generated files

- `data/raw/`: normalized upstream snapshots used to rebuild references.
- `data/processed/manifest.json`: source coverage metadata.
- `academic-phrasebank-skill/references/*.md`: generated page references plus hand-maintained workflow references.
