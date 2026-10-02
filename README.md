# Academic Phrasebank Skill

`academic-phrasebank-skill` is a Codex and Claude Code skill for editing English scientific manuscripts. It helps with drafting, translation, rewriting, polishing, structural revision, paragraph repair, diagnosis, and style unification while preserving the author's evidence and scientific meaning.

## Features

- Routes work to manuscript, section, paragraph, sentence, and phrase levels.
- Preserves numbers, variables, terminology, citations, uncertainty, and evidence strength.
- Provides section-specific and rhetorical-move-specific Phrasebank references.
- Keeps user-facing releases free of development-only files and source snapshots.

## Installation

Run the installer from the repository or a release archive:

```bash
./install.sh
```

The installer targets both Codex and Claude Code by default. Use environment variables for an isolated installation:

```bash
CODEX_SKILLS_DIR=/tmp/academic-phrasebank-codex \
CLAUDE_SKILLS_DIR=/tmp/academic-phrasebank-claude \
./install.sh
```

Invoke the skill as `$academic-phrasebank-skill`.

## Usage

Give the skill the manuscript text and describe the requested intervention. Examples:

```text
$academic-phrasebank-skill Polish this Results paragraph. Preserve every number and citation, and avoid adding interpretation.
```

```text
$academic-phrasebank-skill Rewrite this Discussion section. Separate observed results, interpretation, limitations, and implications.
```

The skill treats the bundled Phrasebank as a rhetorical pattern library. It does not create references, results, methods, mechanisms, or scientific claims that are absent from the input.

## Reference source

The bundled references are generated from the public [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/) published by the University of Manchester. The included pages and source URLs are listed in [`academic-phrasebank-skill/references/source-coverage.md`](academic-phrasebank-skill/references/source-coverage.md).

Phrasebank-derived material remains upstream material. See [`NOTICE.md`](NOTICE.md) before redistributing or modifying it.

## Help and contribution

- [`SUPPORT.md`](SUPPORT.md): usage questions and issue reporting.
- [`SECURITY.md`](SECURITY.md): private vulnerability reporting.
- [`CHANGELOG.md`](CHANGELOG.md): versioned changes.

Contributors can find `CONTRIBUTING.md` and `DEVELOPMENT.md` in the source repository.

## License

Original project code and documentation are licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md).
