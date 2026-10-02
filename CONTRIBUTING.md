# Contributing

Thank you for improving Academic Phrasebank Skill. Contributions should make the skill more useful, more accurate, or easier to install and maintain.

## Before you start

1. Read the [README](README.md), [Development Guide](DEVELOPMENT.md), and [Code of Conduct](CODE_OF_CONDUCT.md).
2. Open an issue for substantial behavior changes so the intended user outcome is clear.
3. Create a topic branch from `main`. Keep unrelated changes in separate branches.

## Repository areas

- `academic-phrasebank-skill/`: installable skill, metadata, and reference material.
- `tools/`: reference builder, package validator, and release builder.
- `tests/`: offline regression tests for extraction and staging behavior.
- `data/raw/` and `data/processed/`: generated source snapshots and coverage metadata.

## Content rules

- Preserve the skill name `academic-phrasebank-skill` and its installation contract.
- Keep scientific claims, citations, statistics, and uncertainty evidence-preserving.
- Add source URLs and attribution when changing upstream-derived references.
- Keep the hand-maintained `academic-phrasebank-skill/references/revision-framework.md` separate from generated files.
- Do not add credentials, personal data, or unrelated artifacts to the repository or release package.

## Local checks

Run the relevant checks before opening a pull request:

```bash
python3 /Users/dawud/.agents/skills/skill-creator/scripts/quick_validate.py academic-phrasebank-skill
python3 tools/validate_skill_package.py
python3 -m unittest discover -s tests -v
python3 -m py_compile tools/build_phrasebank_refs.py tools/validate_skill_package.py tools/build_release.py
git diff --check
```

If generated references change, run `python3 tools/build_phrasebank_refs.py` and inspect the manifest and source coverage. If the user package changes, run `python3 tools/build_release.py` and verify the archive checksums.

## Pull requests

Use a clear title and explain:

- the user problem and resulting behavior;
- the files or reference sources affected;
- the checks you ran; and
- any compatibility or attribution considerations.

Keep the pull request focused. Update the changelog when the change affects users.
