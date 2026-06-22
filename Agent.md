# Agent Notes

- 2026-06-22: Manchester Academic Phrasebank is a WordPress site with a Yoast sitemap index at `https://www.phrasebank.manchester.ac.uk/sitemap.xml`. For this skill, traverse all four listed sitemaps (`post`, `page`, `category`, `author`) and classify every URL; do not rely only on top navigation.
- 2026-06-22: The reusable writing content is 17 page-sitemap pages. Non-writing pages include home, about, Amazon, author archives, category archive, useful links, author bio, and the test post.
- 2026-06-22: Phrase groups are reliably extracted from `h5.et_pb_toggle_title` followed by `div.et_pb_toggle_content.clearfix`. For page summaries, cut the HTML after the last `h1` before the first toggle to avoid accidentally capturing navigation labels.
- 2026-06-22: Keep the skill body lean and route to reference files. Store source coverage in `references/source-coverage.md` and fail the builder when a new sitemap URL is unclassified.
