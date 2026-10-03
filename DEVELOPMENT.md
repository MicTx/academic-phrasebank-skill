# Development Guide

This guide is for maintaining the repository, rebuilding Phrasebank references, and producing a user archive. It does not change how the installed skill edits manuscripts.

## Requirements

- Python 3.9 or newer.
- Git.
- A local `skill-creator` installation for the standard frontmatter validator.
- Network access only when rebuilding the upstream reference snapshot.

## Reference data

Run:

```bash
python3 tools/build_phrasebank_refs.py
```

The builder fetches sitemap pages, checks URL classification and phrase-group completeness before staging raw HTML and normalized references, then replaces the generated trees as one rollback-capable operation. It preserves the hand-maintained `academic-phrasebank-skill/references/revision-framework.md`.

Do not hand-edit generated Phrasebank phrase pages. If their structure needs to change, update the builder and rebuild so the source, generated output, and manifest stay aligned.

## Validate a change

```bash
python3 /Users/dawud/.agents/skills/skill-creator/scripts/quick_validate.py academic-phrasebank-skill
python3 tools/validate_skill_package.py
python3 -m unittest discover -s tests -v
python3 -m py_compile tools/build_phrasebank_refs.py tools/validate_skill_package.py tools/build_release.py
git diff --check
```

Set `SKILL_CREATOR_DIR` when the local skill-creator installation is elsewhere.

The validator checks package shape and release boundaries. The tests cover extraction and staging behavior. The compiler check catches Python syntax errors; it does not replace the tests.

## Evaluate the skill

Evaluation prompts live in `academic-phrasebank-skill/evals/evals.json`. Keep evaluation workspaces outside the repository. Compare preservation of numbers, citations, scope, and evidence strength before changing the skill again.

## User package

```bash
python3 tools/build_release.py
```

The builder validates the source, runs installation smoke tests, creates deterministic `.tar.gz` and `.zip` archives, verifies archive contents and executable modes, and writes `SHA256SUMS` plus a release manifest under `dist/`.

Release archives contain the installer, public project documents, attribution, changelog, and installable skill. They exclude `Agent.md`, development-only tools, tests, evaluation prompts, raw source snapshots, and processed manifests.

## Generated files

- `data/raw/`: normalized upstream HTML and sitemap snapshots.
- `data/processed/manifest.json`: source coverage metadata.
- `academic-phrasebank-skill/references/*.md`: generated page references plus the preserved hand-maintained workflow reference.

When a rebuild fails, the previous successful outputs must remain intact. Inspect `git diff` before accepting any generated change.
