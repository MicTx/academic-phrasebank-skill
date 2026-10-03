# Agent Notes

This file records facts specific to this repository. It is an internal map for agents and maintainers, not a substitute for the public README, Development Guide, or installed skill contract.

## Source and extraction

- The public source is the WordPress Yoast sitemap index at https://www.phrasebank.manchester.ac.uk/sitemap.xml.
- The builder traverses the listed `post`, `page`, `category`, and `author` sitemaps, then orders the writing pages using `SECTION_ORDER`.
- The reusable writing content is currently 17 page-sitemap pages. Home, about, archive, author, useful-links, test-post, and other non-writing pages are excluded.
- Phrase groups come from `h5.et_pb_toggle_title` followed by `div.et_pb_toggle_content.clearfix`.
- Page summaries stop after the last `h1` before the first toggle, so navigation labels do not enter the references.
- Inline tags are removed without inserting spaces inside words. Hidden layout markers such as `break` are not phrase content.
- Intentional examples such as `X`, `Smith`, and `Jones` remain in the source references. The skill must keep them generic and prevent them from leaking into user-specific claims.

## Generated versus hand-maintained files

- Generated references are the page-slug files, `references/index.md`, and `references/source-coverage.md`.
- `references/revision-framework.md` is hand-maintained and must survive every rebuild.
- `data/raw/` and `data/processed/manifest.json` are generated audit data. A failed network rebuild must not delete the previous successful outputs.
- `academic-phrasebank-skill/evals/evals.json` is a hand-maintained development input. Evaluation workspaces and viewer output stay outside the skill directory and are excluded from user releases.
- Public introduction and tutorial live under `academic-phrasebank-skill/docs/`; the release builder copies the complete skill directory into user archives.

## Build and release facts

- `tools/build_phrasebank_refs.py` stages fetched raw data, generated references, and processed metadata, then commits the three directory swaps with rollback. It preserves `revision-framework.md`.
- `tools/validate_skill_package.py` is the project-specific offline audit. The standard frontmatter check is the `skill-creator` quick validator.
- `tools/build_release.py` runs validation and install smoke checks, creates a commit-derived source snapshot, writes deterministic `.tar.gz` and `.zip` archives, verifies their contents, and writes `SHA256SUMS` plus a release manifest under `dist/`.
- User release snapshots contain the installer, public project documents, attribution/changelog, and the installable skill. They exclude `Agent.md`, `DEVELOPMENT.md`, tests, evals, raw source snapshots, manifests, and build tools.
- The release identifier comes from the current Git commit and is not a semantic version.
- ZIP and TAR archives must preserve `install.sh` mode `0755`.

## Installation acceptance

- `install.sh` installs to both the default Codex and Claude Code skill directories.
- The environment variables `CODEX_SKILLS_DIR` and `CLAUDE_SKILLS_DIR` override those destinations for isolated smoke tests.
- Installation verification must use two separate temporary target directories and confirm that a failed or empty source copy does not replace an existing destination.
- After editing the skill, refresh the installed copy before forward-testing; otherwise tests can exercise stale metadata or references.

## Reading order for future agents

1. Read the README to identify the user path.
2. Read the skill contract before changing behavior or examples.
3. Read the reference index and revision framework before changing routing or revision logic.
4. Read the reference builder before editing any generated reference.
5. Run the narrow validator first, then the full test and release commands named in the Development Guide.
