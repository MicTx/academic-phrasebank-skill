# Contributing

## Scope

Contributions should improve the skill, its reference routing, source attribution, or the reliability of the build and validation tools.

## Before opening a change

1. Read `README.md` and `DEVELOPMENT.md`.
2. Keep user-facing behavior and the internal skill name `academic-phrasebank-assistant` compatible.
3. Do not add Phrasebank text without recording its upstream URL and provenance.
4. Do not add invented citations, examples, statistics, or scientific claims to the skill instructions.

## Required checks

Run the checks documented in `DEVELOPMENT.md`, including the standard skill validator, the project validator, the unit tests, and `git diff --check`.

If the Phrasebank extractor or generated references change, run a complete rebuild and inspect the resulting manifest and source coverage. Keep `revision-framework.md` hand-maintained.

## Pull requests

Describe the user-facing effect, the affected reference or build path, and the validation performed. Keep generated-source updates separate from unrelated formatting changes when practical.
