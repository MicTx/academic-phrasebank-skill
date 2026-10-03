from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import build_phrasebank_refs as builder


class PhrasebankExtractionTests(unittest.TestCase):
    def test_raw_snapshot_removes_promotion_but_keeps_academic_book_usage(self) -> None:
        fragment = (
            '<div>An enhanced and expanded version of PHRASEBANK is available in PDF or Kindle format:</div>\n'
            '<div><a href="https://www.phrasebank.manchester.ac.uk/amazon/">Kindle</a></div>\n'
            '<p>Consult a good English grammar book.</p>'
        )
        normalized = builder.normalise_raw_html(fragment)
        self.assertNotIn("enhanced and expanded version", normalized.lower())
        self.assertNotIn("/amazon/", normalized.lower())
        self.assertIn("grammar book", normalized)

    def test_inline_tags_do_not_split_words(self) -> None:
        fragment = '<p><em>B</em>e<em>ing cautious</em></p>'
        self.assertEqual(builder.strip_tags(fragment), "Being cautious")
        self.assertEqual(builder.split_phrases(fragment), ["Being cautious"])

    def test_hidden_break_marker_is_removed_but_real_break_is_kept(self) -> None:
        fragment = (
            '<p>Alpha<br /><span style="color: white">break</span><br />Beta</p>'
            '<p>Break down the results and report the break point.</p>'
        )
        self.assertEqual(
            builder.split_phrases(fragment),
            ["Alpha", "Beta", "Break down the results and report the break point."],
        )

    def test_group_extraction_handles_inline_word_and_hidden_break(self) -> None:
        page = (
            '<h5 class="et_pb_toggle_title"><em>B</em>e<em>ing cautious</em></h5>'
            '<div class="et_pb_toggle_content clearfix">'
            "<p>Alpha<br /><span style=\"color: white\">break</span><br />Beta</p>"
            "</div>"
        )
        groups = builder.extract_groups(page)
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0].title, "Being cautious")
        self.assertEqual(groups[0].phrases, ["Alpha", "Beta"])


class PhrasebankStagingTests(unittest.TestCase):
    def test_commit_preserves_manual_framework_and_removes_stale_generated_md(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            staged = root / "staged"
            live = root / "references"
            (staged / "references").mkdir(parents=True)
            live.mkdir()
            (live / "revision-framework.md").write_text("manual", encoding="utf-8")
            (live / "stale.md").write_text("old", encoding="utf-8")
            (staged / "references" / "index.md").write_text("new", encoding="utf-8")

            builder._replace_directory(
                staged / "references", live, preserve={"revision-framework.md"}
            )

            self.assertEqual(
                (live / "revision-framework.md").read_text(encoding="utf-8"), "manual"
            )
            self.assertEqual((live / "index.md").read_text(encoding="utf-8"), "new")
            self.assertFalse((live / "stale.md").exists())

    def test_stage_outputs_does_not_touch_live_directories(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_raw = root / "source-raw"
            stage = root / "stage"
            source_raw.mkdir()
            (source_raw / "example.html").write_text("<html />", encoding="utf-8")
            page = builder.PageContent(
                title="Example",
                slug="example",
                url="https://example.invalid/example/",
                summary=[],
                groups=[builder.PhraseGroup(title="Group", phrases=["Phrase"])],
            )

            builder.stage_outputs(stage, source_raw, [page], [], [])

            self.assertEqual((source_raw / "example.html").read_text(encoding="utf-8"), "<html />")
            self.assertTrue((stage / "raw" / "example.html").exists())
            self.assertTrue((stage / "references" / "example.md").exists())
            self.assertTrue((stage / "processed" / "manifest.json").exists())
            rendered = (stage / "references" / "example.md").read_text(encoding="utf-8")
            self.assertIn("## Use This Page", rendered)
            self.assertIn("## Source", rendered)
            self.assertIn("Do not invent facts", rendered)

    def test_commit_staged_outputs_preserves_all_live_trees_on_swap_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = (root / "raw", root / "processed", root / "references")
            staged = root / "staged"
            for live in original:
                live.mkdir(parents=True)
                (live / "sentinel.txt").write_text(f"old-{live.name}", encoding="utf-8")
            (root / "references" / "revision-framework.md").write_text("manual", encoding="utf-8")
            for name in ("raw", "processed", "references"):
                (staged / name).mkdir(parents=True)
                (staged / name / "generated.txt").write_text(f"new-{name}", encoding="utf-8")

            old_raw, old_processed, old_refs = builder.RAW_DIR, builder.PROCESSED_DIR, builder.REF_DIR
            builder.RAW_DIR, builder.PROCESSED_DIR, builder.REF_DIR = original
            real_replace = builder.os.replace
            calls = {"count": 0}

            def fail_on_second_swap(source: str | bytes | Path, target: str | bytes | Path) -> None:
                calls["count"] += 1
                if calls["count"] == 4:
                    raise OSError("injected swap failure")
                real_replace(source, target)

            try:
                builder.os.replace = fail_on_second_swap
                with self.assertRaises(OSError):
                    builder.commit_staged_outputs(staged)
            finally:
                builder.os.replace = real_replace
                builder.RAW_DIR, builder.PROCESSED_DIR, builder.REF_DIR = old_raw, old_processed, old_refs

            for live in original:
                self.assertEqual(
                    (live / "sentinel.txt").read_text(encoding="utf-8"),
                    f"old-{live.name}",
                )
            self.assertEqual(
                (root / "references" / "revision-framework.md").read_text(encoding="utf-8"),
                "manual",
            )


if __name__ == "__main__":
    unittest.main()
