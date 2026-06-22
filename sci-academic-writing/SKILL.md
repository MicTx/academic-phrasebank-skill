---
name: sci-academic-writing
description: SCI academic manuscript writing and revision support using a locally compiled Manchester Academic Phrasebank reference set. Use when drafting, polishing, restructuring, translating, or peer-reviewing English research article sections, especially introductions, literature reviews, methods, results, discussions, conclusions, definitions, cautious claims, critical comparison, trends, quantities, causality, examples, transitions, and past-tense reporting.
---

# SCI Academic Writing

Use this skill to write or revise SCI-style academic English with phrase-pattern support from the Manchester Academic Phrasebank. Treat the bundled phrasebank as a rhetorical pattern library, not as text to paste mechanically.

## Workflow

1. Identify the manuscript task: draft, polish, restructure, translate, condense, expand, or diagnose.
2. Identify the target section or rhetorical function.
3. Read `references/index.md`, then load only the relevant reference files.
4. Extract the rhetorical moves and phrase patterns needed for the task.
5. Produce fluent manuscript prose adapted to the user's claim, evidence, field, and target journal style.
6. Check that the output is not a stitched list of template phrases and that claims remain appropriately cautious.

## Reference Routing

Start with `references/index.md` for the full map.

Load core section files when the user names a manuscript section:

- Introduction, research gap, aim, contribution, or paper structure: `references/introducing-work.md`
- Literature review, citation stance, author prominence, or source integration: `references/referring-to-sources.md`
- Study design, participants, materials, procedures, analysis, or limitations of method: `references/describing-methods.md`
- Findings, tables, figures, quantities, trends, or statistical outcomes: `references/reporting-results.md`
- Interpretation, comparison with literature, implications, limitations, or unexpected results: `references/discussing-findings.md`
- Conclusion, contribution, recommendations, future work, or thesis summary: `references/writing-conclusions.md`

Load language-function files when the task depends on a cross-section move:

- Critique, limitation, weakness, or nuanced disagreement: `references/being-critical.md`
- Classification, taxonomy, components, or listing: `references/classifying-and-listing.md`
- Similarity, difference, contrast, or comparative evaluation: `references/compare-and-contrast.md`
- Numbers, proportions, ranges, frequency, or magnitude: `references/describing-quantities.md`
- Increase, decrease, fluctuation, stability, or time-series description: `references/describing-trends.md`
- Cause, effect, explanation, mechanism, or consequence: `references/explaining-cause-and-effect.md`
- Examples, exemplification, or cases: `references/giving-examples.md`
- Paragraph transitions, topic shifts, or section flow: `references/signalling-transition.md`
- Hedging, uncertainty, probability, or cautious interpretation: `references/using-cautious-language.md`
- Historical development, previous events, or chronology: `references/writing-about-the-past-2.md`
- Definitions, terminology, abbreviations, or conceptual scope: `references/writing-definitions.md`

Use `references/source-coverage.md` only when verifying source coverage or provenance.

## Writing Rules

- Preserve the user's scientific meaning, variables, directionality, uncertainty, and evidence strength.
- Prefer precise claims over inflated novelty or unsupported causal language.
- Use cautious language for interpretation, mechanisms, implications, and generalisation unless evidence is definitive.
- Integrate citations naturally; do not invent references, author names, years, journals, or DOI details.
- Vary sentence structure. Do not repeat the same frame across consecutive sentences.
- Replace placeholders such as `X`, `Y`, and `Smith (2015)` with user-provided domain terms only when supported by context.
- Keep discipline-specific terminology intact unless the user asks for simplification.
- For non-native drafts, repair grammar and flow without erasing technical specificity.

## Output Modes

For drafting, return polished prose directly unless the user asks for alternatives.

For revision, preserve the original structure when it is sound; otherwise, briefly state the structural change and provide the revised version.

For diagnostics, report the highest-impact writing issues first: claim strength, logic, section function, cohesion, citation stance, and phrase-level clarity.

For translation into academic English, translate meaning rather than word order, then adjust stance and rhetorical moves for SCI manuscript conventions.

## Provenance

The bundled references were generated from the public Manchester Academic Phrasebank sitemap and pages. They cover 17 writing pages across the six main manuscript sections and general academic language functions. See `references/source-coverage.md` for the exact traversed sitemaps, included pages, excluded non-writing pages, group counts, and phrase counts.
