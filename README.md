# Academic Phrasebank Skill

`academic-phrasebank-skill` is an evidence-preserving scientific English editor for Codex and Claude Code.

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/MicTx/academic-phrasebank-skill)](https://github.com/MicTx/academic-phrasebank-skill/releases/latest)

It drafts, translates, restructures, diagnoses, and polishes scientific manuscripts while keeping the author's evidence, terminology, citations, and uncertainty visible.

The central rule is simple: **make the language as clear as the evidence, and no stronger.** The bundled Phrasebank supplies rhetorical patterns. It does not supply facts for a manuscript.

> [!WARNING]
> This skill improves wording and structure. It does not verify results, create references, or strengthen claims beyond the supplied evidence.

## Start here

1. Install the skill with `./install.sh`.
2. Invoke `$academic-phrasebank-skill` in a Codex or Claude Code session.
3. State the task, manuscript section, protected content, and required output.

```text
$academic-phrasebank-skill
Polish this Results paragraph. Preserve every number, citation, variable,
and uncertainty marker. Do not add interpretation or references.
```

If the problem is unclear, ask for a diagnosis first:

```text
$academic-phrasebank-skill
Diagnose this Discussion section at manuscript, section, paragraph,
sentence, and phrase levels. Do not rewrite it yet. Keep [REF] unchanged.
```

## What it protects

- Numbers, units, variables, statistical notation, sample sizes, and directions.
- Terminology, abbreviations, named methods, citations, and placeholders such as `[REF]`.
- The difference between an observation, an association, a possible mechanism, an implication, and a recommendation.
- The stated scope of the sample, design, and evidence.

The skill does not invent results, mechanisms, methods, references, or statistics. It does not turn `X`, `Smith`, or `Jones` from a Phrasebank example into a fact about a user's study.

## Choose the right guide

- [Introduction](academic-phrasebank-skill/docs/introduction.md) explains the skill's purpose and boundary.
- [Tutorial](academic-phrasebank-skill/docs/tutorial.md) walks through a constrained Results revision.
- [Skill contract](academic-phrasebank-skill/SKILL.md) is the execution contract used by the model.
- [Reference index](academic-phrasebank-skill/references/index.md) routes a task to the smallest useful reference file.
- [Revision framework](academic-phrasebank-skill/references/revision-framework.md) defines the multi-level revision passes.

## Installation

Run the installer from this repository or from a release archive:

```bash
./install.sh
```

By default it installs to both Codex and Claude Code. Use separate directories for a smoke test:

```bash
CODEX_SKILLS_DIR=/tmp/academic-phrasebank-codex \
CLAUDE_SKILLS_DIR=/tmp/academic-phrasebank-claude \
./install.sh
```

The installable skill keeps the name `academic-phrasebank-skill`.

## Reference source

The references are generated from the public [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/) published by the University of Manchester. [Source coverage](academic-phrasebank-skill/references/source-coverage.md) records the fetched pages, exclusions, counts, and source URLs.

Use a reference page as a pattern library for a rhetorical move. Adapt its frame to the user's claims; never treat its examples as evidence. See [NOTICE.md](NOTICE.md) before redistributing or modifying upstream-derived material.

## Help and contribution

- [Support](SUPPORT.md) explains what to include in a usage question or bug report.
- [Security policy](SECURITY.md) explains private vulnerability reporting.
- Contributors can read `CONTRIBUTING.md` for content rules and pull-request checks, and `DEVELOPMENT.md` for reference rebuilds, validation, and release builds in the source repository.
- [Changelog](CHANGELOG.md) records public changes.

## License

Original project code, installer, and project documentation are licensed under the Apache License, Version 2.0. Phrasebank-derived material remains upstream material; attribution and source information are in [NOTICE.md](NOTICE.md).
