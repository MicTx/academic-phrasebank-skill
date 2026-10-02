# Agent Notes

These notes record facts specific to this repository. General skill-authoring or release-process advice belongs in the relevant skill documentation, not here.

## Phrasebank source and extraction

- The public source is the WordPress Yoast sitemap index at `https://www.phrasebank.manchester.ac.uk/sitemap.xml`.
- The builder traverses the four listed sitemaps (`post`, `page`, `category`, and `author`) and classifies every URL. The reusable writing content is 17 page-sitemap pages; home, about, archive, author, useful-links, test-post, and other non-writing pages are excluded.
- Phrase groups are extracted from `h5.et_pb_toggle_title` followed by `div.et_pb_toggle_content.clearfix`. Page summaries stop after the last `h1` before the first toggle so navigation labels do not enter the references.
- Inline HTML tags must be removed without inserting spaces inside words. Hidden layout markers such as `break` are not phrase content. Preserve intentional examples such as `X`, `Smith`, and `Jones`; the skill must prevent them from leaking into user-specific claims.

## Generated and hand-maintained files

- Generated references are the page-slug files plus `references/index.md` and `references/source-coverage.md`.
- `academic-phrasebank-assistant/references/revision-framework.md` is hand-maintained and must survive every rebuild.
- `data/raw/` and `data/processed/manifest.json` are generated audit data. A failed network rebuild must not delete the previous successful outputs.
- `academic-phrasebank-assistant/evals/evals.json` is a hand-maintained development input. Evaluation workspaces and viewer output stay outside the skill directory and are excluded from user releases.

## Build and release facts

- `tools/build_phrasebank_refs.py` stages fetched raw data and generated references, then commits raw, processed, and reference trees with rollback across the three directory swaps; a complete successful run is required before any live output changes.
- `tools/validate_skill_package.py` is the project-specific offline audit. The standard skill frontmatter check remains `quick_validate.py` from the installed `skill-creator` package.
- `tools/build_release.py` runs validation and install smoke checks, creates a commit-derived source snapshot, writes deterministic `.tar.gz` and `.zip` archives, verifies their contents, and writes `SHA256SUMS` plus a release manifest under `dist/`.
- User release snapshots contain only the installer, public project documents, attribution/changelog, and the installable skill. They exclude `Agent.md`, `DEVELOPMENT.md`, tests, evals, raw source snapshots, manifests, and build tools.
- The release identifier is derived from the current Git commit and is not a semantic version.
- ZIP and TAR release archives preserve `install.sh` mode `0755`; archive checks fail if the executable bit is lost.

## Installation acceptance

- `install.sh` installs to both `${CODEX_HOME:-$HOME/.codex}/skills` and `${CLAUDE_HOME:-$HOME/.claude}/skills`, with `CODEX_SKILLS_DIR` and `CLAUDE_SKILLS_DIR` overrides for temporary smoke tests.
- Install verification must exercise two separate temporary target directories and confirm that a failed or empty source copy does not replace an existing destination.
- After a skill edit, the installed copy must be refreshed before forward-testing; otherwise tests may exercise stale metadata or references.
