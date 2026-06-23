# Multi-Level Manuscript Revision Framework

Use this framework when the task is rewriting, polishing, language editing, paragraph repair, structural revision, or full manuscript diagnosis. Apply the highest level that the user's material requires before polishing lower levels.

## Triage

First classify the requested intervention.

- `write`: create new prose from notes, claims, results, or an outline.
- `rewrite`: recast existing prose while preserving scientific meaning.
- `polish`: improve clarity, grammar, style, concision, and academic register.
- `line-edit`: revise sentence by sentence with a reason for each change when requested.
- `style-unify`: harmonise terminology, stance, tense, voice, sentence rhythm, and academic register across the full text.
- `restructure`: change order, section function, paragraph sequence, or argument architecture.
- `diagnose`: identify problems without fully rewriting unless requested.
- `mixed`: combine structural, paragraph, sentence, and phrase-level operations.

If the user asks for comprehensive, carpet-style, exhaustive, full-manuscript, or multi-level work, run all passes below in order. For full-text polishing or style unification, create a style profile before editing and use it as the standard for the final sweep.

## Style Profile

Build this profile from the user's target journal, field, style sample, or the strongest existing parts of the manuscript. If no sample is available, infer a conservative SCI style and keep the profile explicit.

- `register`: concise, formal, field-specific, and non-promotional.
- `stance`: cautious for interpretation and implications; direct for methods and observed results.
- `terminology`: choose one term for each concept and use it consistently, including abbreviations and plural forms.
- `tense`: present tense for established knowledge and paper structure; past tense for completed methods and results; cautious modals for interpretation.
- `voice`: prefer clear agent-action phrasing when it improves readability; keep passive voice when the method, result, or object is more important than the actor.
- `citation stance`: keep author-prominent and information-prominent citation patterns consistent within each section.
- `sentence rhythm`: vary length and opening patterns, but avoid abrupt shifts between dense technical prose and informal short claims.
- `hedging strength`: keep uncertainty markers aligned with the evidence type, avoiding both overclaiming and excessive weakening.

Use the profile as a manuscript-wide constraint. Do not optimise individual sentences in a way that makes them stylistically inconsistent with surrounding paragraphs.

## Pass 1: Manuscript Architecture

Check whether the whole text has a coherent research story.

- Confirm the central problem, research gap, objective, approach, key findings, and contribution are all visible.
- Check whether each major section performs its expected role rather than repeating another section's job.
- Detect missing logical links between literature gap, method choice, result interpretation, and contribution.
- Remove or relocate content that interrupts the argument's progression.
- Flag unsupported novelty, overclaimed significance, or causal claims not warranted by the evidence.

Common operations: reorder sections, split overloaded sections, merge duplicated content, add missing transition logic, narrow claims, and align title/abstract/conclusion with the actual evidence.

## Pass 2: Section Function

Check each section against its rhetorical job.

- Introduction: move from broad context to specific gap, objective, contribution, and paper structure.
- Literature review: synthesize sources by theme and stance; do not list studies mechanically.
- Methods: describe design, data, procedures, variables, analysis, and reproducibility conditions in a defensible order.
- Results: report findings without premature interpretation; align text with tables, figures, and statistics.
- Discussion: interpret findings through comparison, mechanism, implication, limitation, and uncertainty.
- Conclusion: consolidate contribution, practical or theoretical value, limitations, and future work without introducing new evidence.

Common operations: restore section purpose, remove misplaced interpretation, add missing citation stance, separate result reporting from discussion, and align subsection headings with content.

## Pass 3: Paragraph Logic

Check every paragraph as a local argument unit.

- Ensure the first sentence signals the paragraph's controlling idea.
- Keep one dominant function per paragraph: context, gap, method, result, interpretation, limitation, or implication.
- Arrange sentences in a traceable order: claim, evidence, explanation, qualification, consequence, or transition.
- Add bridges where the reader must infer why one sentence follows another.
- Split paragraphs that contain multiple competing claims or mixed section functions.
- Merge short fragments that repeat the same move or lack independent purpose.

Common operations: rewrite topic sentences, reorder evidence, add linking phrases, remove circular restatement, split overloaded paragraphs, and strengthen paragraph-final takeaways.

## Pass 4: Sentence Expression

Polish sentence-level academic English after the higher-level logic is sound.

- Preserve variables, directionality, scope, magnitude, uncertainty, and methodological constraints.
- Prefer concrete subjects and active analytical verbs when they improve clarity.
- Reduce nominalisations and stacked modifiers when they obscure the scientific action.
- Keep old-to-new information flow so each sentence starts from known context and advances the claim.
- Vary sentence openings and lengths without sacrificing precision.
- Replace vague connectors with logical relations such as contrast, cause, consequence, example, concession, or sequence.
- Use cautious wording for mechanisms, interpretation, implications, and generalisation unless the evidence is decisive.

Common operations: shorten overloaded sentences, repair grammar, clarify referents, improve transitions, change passive to active where appropriate, and remove inflated or redundant wording.

## Pass 5: Phrase And Register

Apply phrasebank patterns only after selecting the intended rhetorical move.

- Use phrase patterns as scaffolds for academic stance, not as reusable boilerplate.
- Replace placeholders with the user's actual concepts only when the source text supports them.
- Avoid repeating the same phrase frame across adjacent sentences or paragraphs.
- Keep discipline-specific terminology, statistical wording, and citation details intact.
- Do not invent references, datasets, results, effect sizes, journal names, or mechanisms.

Common operations: improve hedging, citation stance, comparison, trend description, quantity description, causality, definition, exemplification, and transitions.

## Pass 6: Full-Text Consistency Sweep

Run this pass after paragraph and sentence edits whenever the user provides multiple paragraphs, a section, or a full manuscript.

- Check whether the same concept is named consistently across the text.
- Standardise abbreviations, units, statistical expressions, table and figure references, and section labels.
- Align tense and voice with section function: methods and results should not drift into speculative discussion, and discussion should not report new results as if first observed there.
- Make hedging consistent: association, mechanism, implication, recommendation, and generalisation should use different strength levels.
- Smooth paragraph-to-paragraph transitions so the manuscript reads as one argument rather than separately polished fragments.
- Remove repeated sentence templates introduced during line editing.
- Harmonise citation stance, especially when moving between author-prominent literature review and information-prominent result interpretation.
- Check that the abstract, introduction, discussion, and conclusion describe the contribution at the same strength and scope.

Common operations: build a terminology map, normalise abbreviations, standardise tense and voice, adjust hedging strength, vary repeated sentence frames, align contribution claims, and rewrite transitions between edited units.

## Output Patterns

Choose the smallest output format that satisfies the request.

- Full rewrite: provide the revised text, then a concise note on the main structural or logic changes.
- Diagnostic review: list the highest-impact issues first, grouped by manuscript, section, paragraph, and sentence level.
- Line edit: provide revised prose and, when useful, a compact table with `Original`, `Revised`, and `Reason`.
- Style unification: provide a style profile, the unified prose or targeted edits, and a concise consistency note.
- Multi-pass revision: show the pass order, then deliver the revised version or targeted edits for each pass.
- Alternatives: offer two or three versions only when the user asks for tone, concision, or journal-style choices.

## Quality Gate

Before returning the result, verify these points.

- Scientific meaning, evidence strength, and uncertainty are preserved.
- The highest-level problem visible in the text has been addressed before lower-level polishing.
- Each paragraph has a clear function and internal logic.
- Sentence revisions improve clarity without making unsupported claims.
- Phrasebank patterns are adapted naturally rather than pasted mechanically.
- Terminology, abbreviations, tense, citation stance, hedging strength, and contribution claims are consistent across the revised text.
