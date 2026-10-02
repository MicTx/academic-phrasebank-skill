# Development Guide

This file describes repository maintenance. It is kept for contributors and is excluded from the user-facing release archives.

## Rebuild references

The builder uses the public Manchester Academic Phrasebank sitemap and requires network access:

```bash
python3 tools/build_phrasebank_refs.py
```

It stages raw data, generated references, and the manifest before committing them. `academic-phrasebank-assistant/references/revision-framework.md` is hand-maintained and must survive every rebuild.

## Validate

```bash
python3 /Users/dawud/.agents/skills/skill-creator/scripts/quick_validate.py academic-phrasebank-assistant
python3 tools/validate_skill_package.py
python3 -m unittest discover -s tests -v
python3 -m py_compile tools/build_phrasebank_refs.py tools/validate_skill_package.py tools/build_release.py
git diff --check
```

Use `SKILL_CREATOR_DIR` when `skill-creator` is installed elsewhere.

## Evaluate

Evaluation prompts live in `academic-phrasebank-assistant/evals/evals.json`. Keep evaluation workspaces outside this repository. Compare the current skill with a saved previous snapshot, grade preservation and boundary assertions, and generate the `skill-creator` review viewer before making another revision.

## Build a user release

```bash
python3 tools/build_release.py
```

The command validates the source, runs installation smoke tests, creates a user-facing source directory and deterministic `.tar.gz`/`.zip` archives, verifies archive contents and executable modes, and writes checksums under `dist/`. It intentionally excludes development notes, tests, evaluation prompts, raw source snapshots, manifests, and build tools from the user package.
