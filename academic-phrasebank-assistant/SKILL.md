---
name: academic-phrasebank-assistant
description: SCI academic manuscript writing, rewriting, polishing, style-unifying, and multi-level revision support using a locally compiled Manchester Academic Phrasebank reference set. Use when drafting, rewriting, polishing, line-editing, unifying writing style, restructuring, translating, diagnosing, or peer-reviewing English research manuscripts at manuscript, section, paragraph, sentence, and phrase levels, especially introductions, literature reviews, methods, results, discussions, conclusions, definitions, cautious claims, critical comparison, trends, quantities, causality, examples, transitions, and past-tense reporting.
---

# Academic Phrasebank Assistant

Use this skill to write, rewrite, polish, or revise SCI-style academic English with phrase-pattern support from the Manchester Academic Phrasebank. Treat the bundled phrasebank as a rhetorical pattern library, not as text to paste mechanically.

## Workflow

1. Identify the manuscript task: draft, rewrite, polish, line-edit, unify style, restructure, translate, condense, expand, diagnose, or peer-review.
2. Identify the required granularity: whole manuscript, section, paragraph, sentence, phrase, or mixed-level revision.
3. Read `references/index.md`, then load only the relevant framework and phrasebank reference files.
4. For revision or polishing, apply the highest necessary level first: manuscript architecture, section function, paragraph logic, sentence expression, then word choice.
5. For full-text or multi-section work, build a style profile before rewriting and run a final consistency sweep after sentence-level edits.
6. Extract the rhetorical moves and phrase patterns needed for the task.
7. Produce fluent manuscript prose adapted to the user's claim, evidence, field, target journal style, requested intervention depth, and style profile.
8. Check that the output is not a stitched list of template phrases, claims remain appropriately cautious, and terminology, tense, citation stance, hedging, and sentence rhythm are consistent across the manuscript.

## Reference Routing

Start with `references/index.md` for the full map.

Load `references/revision-framework.md` whenever the user asks for rewriting, polishing, line editing, language editing, comprehensive revision, manuscript diagnosis, paragraph logic, sentence-level improvement, style unification, consistency checking, or multi-level work across structure, paragraphs, and expression.

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
- For comprehensive revision, do not jump straight to sentence polishing when structure, section function, paragraph logic, or evidence linkage is weak.
- Make the intervention level explicit when useful: structure, section, paragraph, sentence, or phrase.
- For full-text polishing, enforce consistency in terminology, abbreviations, tense, voice, citation stance, hedging strength, paragraph openings, and sentence rhythm.

## Output Modes

For drafting, return polished prose directly unless the user asks for alternatives.

For revision, preserve the original structure when it is sound; otherwise, briefly state the structural change and provide the revised version.

For comprehensive or whole-manuscript revision, work in passes: diagnose the document hierarchy, fix the highest-impact structural and logical issues first, then polish paragraph flow, sentence expression, and word choice.

For sentence-level polishing, improve clarity, grammar, concision, stance, cohesion, and academic register without changing the scientific meaning.

For full-text style unification, provide either a final unified version or a targeted consistency report plus edits, depending on the user's requested output.

For diagnostics, report the highest-impact writing issues first: claim strength, logic, section function, cohesion, citation stance, and phrase-level clarity.

For translation into academic English, translate meaning rather than word order, then adjust stance and rhetorical moves for SCI manuscript conventions.

## Provenance

The bundled references were generated from the public Manchester Academic Phrasebank sitemap and pages. They cover 17 writing pages across the six main manuscript sections and general academic language functions. See `references/source-coverage.md` for the exact traversed sitemaps, included pages, excluded non-writing pages, group counts, and phrase counts.
