from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import build_release


ROOT = Path(__file__).resolve().parents[1]


class RepositoryDocumentationTests(unittest.TestCase):
    def test_readmes_have_language_switch_and_shared_routes(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("[English](README.md) | [简体中文](README.zh-CN.md)", english)
        self.assertIn("[English](README.md) | [简体中文](README.zh-CN.md)", chinese)
        for text in (english, chinese):
            for route in (
                "./install.sh",
                "$academic-phrasebank-skill",
                "academic-phrasebank-skill/SKILL.md",
                "academic-phrasebank-skill/references/index.md",
                "NOTICE.md",
                "CHANGELOG.md",
            ):
                self.assertIn(route, text)

    def test_release_source_contains_both_readmes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "release"
            build_release.copy_source(destination)
            self.assertTrue((destination / "README.md").is_file())
            self.assertTrue((destination / "README.zh-CN.md").is_file())


if __name__ == "__main__":
    unittest.main()
