#!/bin/sh
set -eu

SKILL_NAME="academic-phrasebank-assistant"
LEGACY_SKILL_NAME="sci-academic-writing"
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
  stage_dir=""
  backup_dir=""

  if [ -z "$target_root" ] || [ "$target_root" = "/" ] || [ "$target_root" = "." ]; then
    echo "Refusing unsafe install root: $target_root" >&2
    exit 1
  fi

  mkdir -p "$target_root"
  stage_dir=$(mktemp -d "$target_root/.${SKILL_NAME}.stage.XXXXXX")
  backup_dir=$(mktemp -d "$target_root/.${SKILL_NAME}.backup.XXXXXX")
  rmdir "$backup_dir"
  trap 'rm -rf "$stage_dir" "$backup_dir"' EXIT HUP INT TERM

  # Stage and verify the complete copy before touching the installed skill.
  (cd "$SOURCE_DIR" && cp -R . "$stage_dir/")
  find "$stage_dir" -name '.DS_Store' -type f -delete
  test -f "$stage_dir/SKILL.md"
  test -f "$stage_dir/references/index.md"

  if [ -e "$target_dir" ]; then
    mv "$target_dir" "$backup_dir/previous"
  fi
  if ! mv "$stage_dir" "$target_dir"; then
    if [ -e "$backup_dir/previous" ]; then
      mv "$backup_dir/previous" "$target_dir"
    fi
    exit 1
  fi

  # The legacy name is removed only after the new copy is in place.
  rm -rf "$target_root/$LEGACY_SKILL_NAME"
  rm -rf "$backup_dir"
  trap - EXIT HUP INT TERM
  echo "Installed $SKILL_NAME -> $target_dir"
}

install_skill "$CODEX_SKILLS_DIR"
install_skill "$CLAUDE_SKILLS_DIR"

echo "Done. Invoke with \$$SKILL_NAME in Codex or Claude Code."
