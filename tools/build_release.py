#!/usr/bin/env python3
"""Build a deterministic source release for the Academic Phrasebank skill."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "academic-phrasebank-skill"
SKILL_NAME = "academic-phrasebank-skill"
DEFAULT_OUTPUT_DIR = ROOT / "dist"
PUBLIC_ROOT_FILES = {"README.md", "LICENSE", "NOTICE.md", "CHANGELOG.md", "SUPPORT.md", "SECURITY.md", "install.sh"}


def run(command: list[str], *, cwd: Path = ROOT, env: Optional[dict[str, str]] = None) -> None:
    print(f"$ {' '.join(command)}")
    subprocess.run(command, cwd=cwd, env=env, check=True)


def git_output(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def find_skill_creator() -> Path:
    candidates = []
    configured = os.environ.get("SKILL_CREATOR_HOME") or os.environ.get("SKILL_CREATOR_DIR")
    if configured:
        candidates.append(Path(configured))
    candidates.extend(
        [
            Path.home() / ".agents/skills/skill-creator",
            Path.home() / ".codex/skills/.system/skill-creator",
        ]
    )
    for candidate in candidates:
        if (candidate / "scripts/quick_validate.py").is_file():
            return candidate
    searched = ", ".join(str(path) for path in candidates)
    raise RuntimeError(f"skill-creator quick validator not found; searched: {searched}")


def validate_source() -> None:
    skill_creator = find_skill_creator()
    run([sys.executable, str(skill_creator / "scripts/quick_validate.py"), str(SKILL_DIR)])
    run([sys.executable, str(ROOT / "tools/validate_skill_package.py")])
    tests_dir = ROOT / "tests"
    if tests_dir.is_dir():
        run([sys.executable, "-m", "unittest", "discover", "-s", str(tests_dir), "-v"])


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    parts = set(relative.parts)
    if ".git" in parts or "__pycache__" in parts or ".pytest_cache" in parts:
        return True
    if relative.parts and relative.parts[0] in {"dist", "academic-phrasebank-skill-workspace"}:
        return True
    if path.name == ".DS_Store" or "evals" in parts:
        return True
    return False


def copy_source(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for relative in sorted(PUBLIC_ROOT_FILES):
        source = ROOT / relative
        if not source.is_file():
            raise RuntimeError(f"missing public release file: {relative}")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    for source in sorted(SKILL_DIR.rglob("*")):
        if not source.is_file() or should_skip(source):
            continue
        relative = source.relative_to(ROOT)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_digest(source_root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(path for path in source_root.rglob("*") if path.is_file()):
        relative = path.relative_to(source_root).as_posix().encode()
        digest.update(relative)
        digest.update(b"\0")
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        digest.update(b"\0")
    return digest.hexdigest()


def archive_files(source_root: Path) -> list[Path]:
    return sorted(path for path in source_root.rglob("*") if path.is_file())


def build_tar(source_root: Path, archive_path: Path, root_name: str) -> None:
    with archive_path.open("wb") as stream:
        with gzip.GzipFile(fileobj=stream, mode="wb", compresslevel=9, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as archive:
                for path in archive_files(source_root):
                    relative = path.relative_to(source_root).as_posix()
                    info = archive.gettarinfo(str(path), arcname=f"{root_name}/{relative}")
                    info.mtime = 0
                    info.uid = 0
                    info.gid = 0
                    info.uname = ""
                    info.gname = ""
                    with path.open("rb") as stream_in:
                        archive.addfile(info, stream_in)


def build_zip(source_root: Path, archive_path: Path, root_name: str) -> None:
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in archive_files(source_root):
            relative = path.relative_to(source_root).as_posix()
            info = zipfile.ZipInfo(f"{root_name}/{relative}")
            info.date_time = (1980, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = path.stat().st_mode & 0o777
            info.external_attr = (0o100000 | mode) << 16
            archive.writestr(info, path.read_bytes())


def verify_archive(path: Path, root_name: str) -> None:
    required = {
        f"{root_name}/README.md",
        f"{root_name}/LICENSE",
        f"{root_name}/NOTICE.md",
        f"{root_name}/CHANGELOG.md",
        f"{root_name}/SUPPORT.md",
        f"{root_name}/SECURITY.md",
        f"{root_name}/install.sh",
        f"{root_name}/academic-phrasebank-skill/SKILL.md",
        f"{root_name}/academic-phrasebank-skill/references/index.md",
    }
    if path.suffix == ".zip":
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            bad = [
                name for name in names
                if name.startswith(f"{root_name}/.git/")
                or "/dist/" in name
                or name.startswith(f"{root_name}/tests/")
                or name.startswith(f"{root_name}/tools/")
                or name.startswith(f"{root_name}/data/")
                or name.endswith("/Agent.md")
                or "/evals/" in name
            ]
            install_name = f"{root_name}/install.sh"
            install_info = archive.getinfo(install_name)
            install_mode = (install_info.external_attr >> 16) & 0o777
            if install_mode != 0o755:
                raise RuntimeError(f"ZIP lost install.sh executable mode: {oct(install_mode)}")
    else:
        with tarfile.open(path, "r:gz") as archive:
            names = set(archive.getnames())
            bad = [
                name for name in names
                if name.startswith(f"{root_name}/.git/")
                or "/dist/" in name
                or name.startswith(f"{root_name}/tests/")
                or name.startswith(f"{root_name}/tools/")
                or name.startswith(f"{root_name}/data/")
                or name.endswith("/Agent.md")
                or "/evals/" in name
            ]
            install_member = archive.getmember(f"{root_name}/install.sh")
            install_mode = install_member.mode & 0o777
            if install_mode != 0o755:
                raise RuntimeError(f"TAR lost install.sh executable mode: {oct(install_mode)}")
    missing = required - names
    if missing or bad:
        raise RuntimeError(f"invalid archive {path}: missing={sorted(missing)} forbidden={sorted(bad)}")


def install_smoke() -> None:
    with tempfile.TemporaryDirectory(prefix="academic-phrasebank-install-") as temp_dir:
        temp_root = Path(temp_dir)
        env = os.environ.copy()
        env["CODEX_SKILLS_DIR"] = str(temp_root / "codex")
        env["CLAUDE_SKILLS_DIR"] = str(temp_root / "claude")
        run(["sh", str(ROOT / "install.sh")], env=env)
        for target in [temp_root / "codex" / SKILL_NAME, temp_root / "claude" / SKILL_NAME]:
            for required in ["SKILL.md", "references/index.md", "references/revision-framework.md"]:
                if not (target / required).is_file():
                    raise RuntimeError(f"install smoke missing {target / required}")


def write_checksums(paths: list[Path], destination: Path) -> None:
    lines = [f"{sha256(path)}  {path.name}" for path in paths]
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_release(output_dir: Path) -> dict[str, object]:
    validate_source()
    install_smoke()

    commit = git_output("rev-parse", "--short", "HEAD")
    status = git_output("status", "--porcelain")
    release_id = f"{commit}{'-dirty' if status else ''}"
    root_name = f"{SKILL_NAME}-{release_id}"
    output_dir.mkdir(parents=True, exist_ok=True)
    release_root = output_dir / root_name
    if release_root.exists():
        shutil.rmtree(release_root)

    with tempfile.TemporaryDirectory(prefix="academic-phrasebank-release-") as temp_dir:
        staged_root = Path(temp_dir) / root_name
        copy_source(staged_root)
        (staged_root / "RELEASE.json").write_text(
            json.dumps(
                {
                    "release_schema": 1,
                    "skill_name": SKILL_NAME,
                    "git_commit": commit,
                    "git_dirty": bool(status),
                    "source_digest_before_release_metadata": source_digest(staged_root),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        shutil.copytree(staged_root, release_root)

    tar_path = output_dir / f"{root_name}.tar.gz"
    zip_path = output_dir / f"{root_name}.zip"
    build_tar(release_root, tar_path, root_name)
    build_zip(release_root, zip_path, root_name)
    verify_archive(tar_path, root_name)
    verify_archive(zip_path, root_name)

    manifest = {
        "release_schema": 1,
        "skill_name": SKILL_NAME,
        "release_id": release_id,
        "git_commit": commit,
        "git_dirty": bool(status),
        "source_directory": release_root.name,
        "source_digest": source_digest(release_root),
        "archives": {
            tar_path.name: sha256(tar_path),
            zip_path.name: sha256(zip_path),
        },
        "validation": {
            "quick_validate": "passed",
            "package_validator": "passed",
            "install_smoke": "passed",
            "archive_integrity": "passed",
        },
    }
    manifest_path = output_dir / f"{root_name}.manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    checksums_path = output_dir / "SHA256SUMS"
    write_checksums([tar_path, zip_path, manifest_path], checksums_path)
    print(f"Release directory: {release_root}")
    print(f"Tar archive: {tar_path}")
    print(f"Zip archive: {zip_path}")
    print(f"Manifest: {manifest_path}")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    build_release(args.output_dir.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
