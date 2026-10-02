# Academic Phrasebank Assistant

`academic-phrasebank-assistant` is a Codex/Claude skill for evidence-preserving English editing of scientific manuscripts. It supports drafting, translation, rewriting, polishing, structural revision, paragraph repair, diagnosis, and style unification.

The skill uses a locally bundled subset of the public Manchester Academic Phrasebank as a rhetorical pattern library. It does not invent citations, statistics, methods, mechanisms, or scientific conclusions.

## Install

Run the installer from the project directory:

```bash
./install.sh
```

By default the skill is installed for both Codex and Claude Code:

- Codex: `${CODEX_SKILLS_DIR:-${CODEX_HOME:-$HOME/.codex}/skills}`
- Claude Code: `${CLAUDE_SKILLS_DIR:-${CLAUDE_HOME:-$HOME/.claude}/skills}`

For an isolated installation test:

```bash
CODEX_SKILLS_DIR=/tmp/phrasebank-codex \
CLAUDE_SKILLS_DIR=/tmp/phrasebank-claude \
./install.sh
```

Invoke the skill as `$academic-phrasebank-assistant`.

## What is included

- `academic-phrasebank-assistant/SKILL.md`: operating instructions and quality gate.
- `academic-phrasebank-assistant/references/`: section and language-function routing references.
- `academic-phrasebank-assistant/agents/openai.yaml`: Codex display metadata.
- `NOTICE.md`: project and upstream source attribution.
- `CHANGELOG.md`: public change history.

## Source attribution

The Phrasebank-derived references come from public Manchester Academic Phrasebank pages. The exact URLs, page list, group counts, and phrase counts are recorded in `academic-phrasebank-assistant/references/source-coverage.md`.

The repository's original files are licensed under Apache-2.0. Phrasebank-derived material remains identified as upstream material; see `NOTICE.md` and the official [Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/) page before redistributing it.

## User releases

User-facing releases contain the installer, the installable skill, user documentation, attribution, and the changelog. Development notes, tests, evaluation prompts, raw source snapshots, manifests, and build tools remain in the source repository and are not included in the user archive.

Release archives include a commit-derived identifier and a `SHA256SUMS` file. Verify an archive with:

```bash
tar -tzf academic-phrasebank-assistant-<commit>.tar.gz >/dev/null
unzip -t academic-phrasebank-assistant-<commit>.zip
```

## License

Original project files are provided under the Apache License, Version 2.0. See `LICENSE`. See `NOTICE.md` for the separate upstream Phrasebank attribution.

Repository maintenance, validation, evaluation, and release construction are documented separately in the source repository.
