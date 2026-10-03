---
name: academic-phrasebank-skill
description: Expert English-language editing for scientific and SCI research manuscripts, grounded in the bundled Manchester Academic Phrasebank. Use this skill whenever a user asks to draft, translate, rewrite, polish, line-edit, restructure, diagnose, peer-review the English or argumentation of a manuscript, or unify the style of research writing, including introductions, literature reviews, methods, results, discussions, conclusions, abstracts, definitions, cautious claims, comparisons, trends, quantities, causality, citations, and transitions. Apply it even when the user does not mention Phrasebank or SCI explicitly but needs publication-ready academic English.
---

# Academic Phrasebank Skill

## Purpose

Edit scientific English without changing what the research supports. Use the bundled Manchester Academic Phrasebank as a library of rhetorical patterns. Adapt a pattern to the user's claims; never paste a pattern as if it were evidence.

The skill can:

- **Draft** prose from supplied claims, results, notes, or an outline.
- **Translate** into academic English while preserving meaning and stance.
- **Revise** existing prose without changing scientific scope.
- **Polish** grammar, clarity, concision, flow, and register.
- **Restructure** manuscript, section, or paragraph logic before line editing.
- **Diagnose** problems without rewriting when requested.

A broad rewrite or peer-review-style diagnosis combines these modes. Language editing does not authorise fact checking, new analysis, or literature searching.

## Input contract

Before editing, identify four things:

1. **Task and level**: draft, translate, revise, polish, restructure, diagnose, or a combination; manuscript, section, paragraph, sentence, or phrase level.
2. **Section and audience**: Introduction, Methods, Results, Discussion, Conclusion, abstract, or another target; journal or field style if supplied.
3. **Protected content**: numbers, units, variables, statistics, terms, abbreviations, named methods, citations, placeholders, and uncertainty markers that must remain.
4. **Output shape**: revised prose, diagnosis, alternatives, a change note, or a specific format.

If the user does not specify a style, use concise, formal, field-aware SCI English. If the source is ambiguous, preserve the ambiguity or ask one targeted question. Do not silently choose a scientific interpretation.

## Definition of success

A successful output is fluent and readable while all of these remain true:

- Numbers, units, variables, directionality, sample size, effect sizes, intervals, p-values, and other quantitative details are unchanged unless correction is explicitly requested.
- Association is not upgraded to causation. A possible mechanism is not presented as demonstrated. A local result is not generalised beyond its design.
- Citations, authors, years, DOI details, datasets, methods, results, and placeholders are not invented.
- Terminology, abbreviations, tense, voice, citation stance, hedging, and contribution claims are consistent with the target section and surrounding text.
- Phrasebank patterns support a connected argument rather than a chain of interchangeable templates.
- Structural changes are visible in the output or concise change note.

## Editing workflow

Follow this order. Stop at the smallest level that fully solves the request.

1. **Classify the request.** Record mode, target section, depth, audience, and output.
2. **Inventory constraints.** Copy the protected facts and evidence limits into a private checklist. Keep unresolved placeholders visible.
3. **Route references.** Read `references/index.md`, then load `references/revision-framework.md` for any rewrite, polish, diagnosis, style-unification, or multi-level task. Load only the section and language-function files needed for the rhetorical moves.
4. **Repair the highest-level problem first.** Check manuscript architecture, section function, and paragraph logic before sentence and phrase edits. Do not polish a sentence whose paragraph function is still unclear.
5. **Build a style profile for broad work.** Set register, stance, terminology, tense, voice, citation stance, sentence rhythm, and hedging strength from the user's instructions or strongest supplied sample.
6. **Name the rhetorical move.** Decide whether the passage introduces a gap, describes a method, reports an observation, compares findings, qualifies a claim, offers a possible explanation, states an implication, or performs another move.
7. **Draft or revise.** Use the smallest suitable Phrasebank pattern, adapt it to the user's field, and keep technical terms intact unless simplification is requested.
8. **Run the final gate.** Compare the result with the protected-content checklist and the checks below. Return the requested artifact first, then only the concise rationale or issue list requested.

## Reference routing

Start with [`references/index.md`](references/index.md). Use the smallest relevant set.

### Manuscript sections

- Introduction, gap, aim, contribution, paper structure: `introducing-work.md`
- Literature review, citation stance, author prominence, source integration: `referring-to-sources.md`
- Study design, participants, materials, procedures, analysis, method limitations: `describing-methods.md`
- Findings, tables, figures, quantities, trends, statistical outcomes: `reporting-results.md`
- Interpretation, comparison, implications, limitations, unexpected results: `discussing-findings.md`
- Conclusion, recommendations, future work, thesis summary: `writing-conclusions.md`

### Language functions

- Critique or nuanced disagreement: `being-critical.md`
- Classification, taxonomy, or listing: `classifying-and-listing.md`
- Similarity, difference, contrast, or comparative evaluation: `compare-and-contrast.md`
- Numbers, proportions, ranges, frequency, or magnitude: `describing-quantities.md`
- Increase, decrease, fluctuation, stability, or time series: `describing-trends.md`
- Cause, effect, mechanism, or consequence: `explaining-cause-and-effect.md`
- Examples or cases: `giving-examples.md`
- Paragraph transitions or section flow: `signalling-transition.md`
- Uncertainty, probability, or cautious interpretation: `using-cautious-language.md`
- Historical development or chronology: `writing-about-the-past-2.md`
- Definitions, terminology, abbreviations, or conceptual scope: `writing-definitions.md`

Use `source-coverage.md` only for provenance or coverage questions. It is metadata, not a source of scientific claims.

## Mode rules

- **Draft:** use only supplied facts, notes, results, and outline. Mark missing evidence instead of filling it.
- **Translate:** translate rhetorical function and evidence strength, not word order. Keep terms, abbreviations, numbers, citations, placeholders, and uncertainty markers.
- **Revise:** preserve the author's meaning and scope; state any necessary structural change.
- **Polish:** keep order and content unless a local reorder is required for clarity.
- **Restructure:** repair section and paragraph sequence before sentence polishing; separate observation, interpretation, limitation, and implication.
- **Diagnose:** identify the highest-impact problems with locations and brief examples; do not rewrite unless requested.
- **Full-text work:** create a style profile, apply the revision framework in order, then run a consistency sweep across all supplied sections.

For Results and Methods, report procedures and observations directly without inserting interpretation. For Discussion and Conclusion, distinguish findings from explanation, implication, recommendation, limitation, and generalisation.

## Hard boundaries

Never:

- invent or silently correct scientific facts, statistics, citations, authors, years, journals, DOI details, datasets, methods, mechanisms, or results;
- strengthen an association into causation, a hypothesis into a finding, or a limited sample into a universal claim;
- use Phrasebank examples such as `X`, `Smith`, or `Jones` as facts about the user's study;
- remove uncertainty, limitations, negative results, or scope conditions to sound more confident;
- replace a technical term with a generic synonym that changes its meaning;
- hide a major structural rewrite behind a proofreading request;
- claim that the prose is scientifically validated, fact-checked, or journal-compliant unless that work was actually performed.

When an edit requires a scientific decision, preserve the source wording and state the decision point. When material is missing, keep a visible marker such as `[REF]` rather than guessing.

## Anti-patterns

Check specifically for:

- **Template stitching:** several Phrasebank frames joined without a clear argument.
- **Overclaiming:** stronger causal, novelty, or generalisation language than the evidence supports.
- **Example leakage:** `X`, `Smith`, `Jones`, or a source example left where a user-specific term is required.
- **Placeholder invention:** guessed authors, years, values, methods, or references.
- **Level mismatch:** phrase polishing while a section, paragraph, or evidence-link problem remains.
- **Register drift:** promotional or informal wording inside technical prose.
- **Consistency drift:** incompatible terms, abbreviations, tense, citation stance, or contribution claims.
- **Translation drift:** changed direction, scope, certainty, sample, comparison, or statistical interpretation.

## Final quality gate

Before returning a substantial output:

1. Compare all numbers, symbols, variables, units, groups, directions, and statistical expressions with the source.
2. Confirm that observation, association, causation, mechanism, implication, recommendation, and generalisation use the appropriate evidence strength.
3. Check terminology, abbreviations, table/figure references, section labels, and named methods.
4. Check tense and voice against section function: completed Methods/Results actions normally use past forms; established knowledge and paper structure may use present forms; interpretation is appropriately qualified.
5. Check citation stance and confirm that no unsupported citation detail was added.
6. Check transitions, sentence openings, paragraph boundaries, and repeated frames for natural flow.
7. Search for unresolved or leaked placeholders, including `X`, `Y`, `Smith`, `Jones`, task markers, and bracketed notes. Preserve deliberate placeholders or flag them.
8. Confirm that the response format matches the request.

## Provenance

The bundled references are generated from the public Manchester Academic Phrasebank sitemap and pages. They cover 17 writing pages across the main manuscript sections and general academic language functions. Exact sources, exclusions, groups, and counts are recorded in `source-coverage.md`. The references provide rhetorical patterns; they are not evidence for a user's scientific claims.
