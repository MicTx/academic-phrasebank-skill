# Contributing

Contributions should make the skill more useful, more accurate, or easier to install and maintain. Start by identifying which user decision the change improves.

## Before editing

Read [README.en.md](README.en.md) (or [README.md](README.md) for Simplified Chinese), [DEVELOPMENT.md](DEVELOPMENT.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Open an issue for a substantial behavior change so the intended user outcome is recorded before implementation. Create a topic branch from `main`, and keep unrelated work on separate branches.

## Repository map

- `academic-phrasebank-skill/` contains the installable skill, its instructions, guides, and references.
- `academic-phrasebank-skill/references/*.md` contains generated Phrasebank pages plus the hand-maintained revision framework.
- `tools/` contains the reference builder, package validator, and release builder.
- `tests/` contains offline regression tests for extraction and staging behavior.
- `data/raw/` and `data/processed/` are generated source snapshots and coverage metadata.

## Content rules

- Keep the public skill name `academic-phrasebank-skill` and its installation contract.
- Preserve scientific meaning, citations, statistics, terminology, and uncertainty. A clearer sentence must not become a stronger claim.
- Treat Phrasebank examples as rhetorical patterns, not facts or ready-made conclusions.
- Add source URLs and attribution when changing upstream-derived references.
- Keep `revision-framework.md` separate from generated references; the builder must preserve it.
- Do not add credentials, personal data, confidential manuscripts, or unrelated artifacts.

## Local checks

Run the checks that match the changed area:

```bash
python3 /Users/dawud/.agents/skills/skill-creator/scripts/quick_validate.py academic-phrasebank-skill
python3 tools/validate_skill_package.py
python3 -m unittest discover -s tests -v
python3 -m py_compile tools/build_phrasebank_refs.py tools/validate_skill_package.py tools/build_release.py
git diff --check
```

If generated references change, run `python3 tools/build_phrasebank_refs.py` and inspect the source coverage and diff. If the installable package changes, run `python3 tools/build_release.py` and inspect the archive checksums.

## Pull requests

Describe the user problem and resulting behavior first. Then identify the affected files or source pages, checks run, and any compatibility or attribution considerations. Update [CHANGELOG.md](CHANGELOG.md) when the change affects users.
