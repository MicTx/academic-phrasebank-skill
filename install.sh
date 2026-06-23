#!/bin/sh
set -eu

SKILL_NAME="sci-academic-writing"
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SOURCE_DIR="$SCRIPT_DIR/$SKILL_NAME"

if [ ! -f "$SOURCE_DIR/SKILL.md" ]; then
  echo "Missing skill source: $SOURCE_DIR" >&2
  exit 1
fi

CODEX_SKILLS_DIR="${CODEX_SKILLS_DIR:-${CODEX_HOME:-$HOME/.codex}/skills}"
CLAUDE_SKILLS_DIR="${CLAUDE_SKILLS_DIR:-${CLAUDE_HOME:-$HOME/.claude}/skills}"

install_skill() {
  target_root=$1
  target_dir="$target_root/$SKILL_NAME"

  mkdir -p "$target_root"
  rm -rf "$target_dir"
  mkdir -p "$target_dir"

  # Copy contents rather than the parent folder so repeated installs are stable.
  (cd "$SOURCE_DIR" && tar --exclude='.DS_Store' -cf - .) | (cd "$target_dir" && tar -xf -)
  echo "Installed $SKILL_NAME -> $target_dir"
}

install_skill "$CODEX_SKILLS_DIR"
install_skill "$CLAUDE_SKILLS_DIR"

echo "Done. Invoke with \$$SKILL_NAME in Codex or Claude Code."
