# 2026-06-17 Template Risk Read-Only Audit

Mode: read-only audit. No active Skill, Agent, Script, config, or template file was changed.

Purpose: identify rules that may push the system toward formulaic, repetitive, or checklist-looking output, even when the article technically passes validation.

This audit focuses on template risk, not basic correctness.

## Executive Verdict

The project has a strong anti-generic instinct, but some instructions turn that instinct into fixed patterns.

The biggest risk is not that the system lacks standards. The risk is that it has too many fixed standards in places where the article should respond dynamically to the benchmark, search intent, evidence, and reader journey.

The highest-risk template forces are:

1. Fixed AIO and bold-answer rules.
2. Per-H2 evidence and section-contract rules.
3. Fixed rhythm and format alternation rules.
4. Numeric scoring systems that pretend subjective strategy can be reduced to exact percentages.
5. Example content that is too domain-specific and may leak into future outputs as a default style.

Correction after operator review: `article-enrich`, `image-strategy`, and `internal-linking` should not be treated as first-priority template risks. They are primarily material-enrichment layers. Their rules matter, but they are less likely to damage the article's core expression as long as they do not rewrite prose or force the same visual/link furniture into every article.

The solution is not to remove discipline. The solution is to separate:

- **Hard operational rules**: facts, source traceability, locked profile, real asset availability, state transitions.
- **Dynamic editorial rules**: rhythm, AIO capture, bolding, visuals, links, evidence placement, narrative pacing.

## Template Risk Taxonomy

### Type A: Fixed Count Risk

The system tells the agent to produce a fixed number, range, percentage, or density.

Examples:

- One bold sentence per H2.
- Maximum 2 bold sentences per H2.
- 5-8 inline links.
- 2-3 resource blocks.
- 1-2 accordion blocks.
- 5-8 visual opportunities for a 3,000-word article.
- At least one generated chart or diagram per article.
- 5 candidate benchmarks, 3 selected benchmarks.
- 14-field topic card, 5-dimension scoring model.

Product risk:

The agent may optimize for satisfying the count rather than asking whether the article actually needs the element.

### Type B: Per-Section Uniformity Risk

The system applies the same requirement to every H2.

Examples:

- Every H2 must have a Tier 1 source.
- Every section should have an extractable judgment.
- Every heading must map cleanly to a narrative node.
- Every image placeholder must include a full option block by default.

Product risk:

Articles lose breathing room. Setup, transition, hesitation, contrast, and rhythm sections become overburdened.

### Type C: Format Lock Risk

The system hardcodes a reusable format that may become visible to readers.

Examples:

- Resource block with bold arrow link plus supporting bullets.
- FAQ accordion shortcode format.
- Image A/B/C/D option blocks.
- Six-node arc.
- Section contracts with the same fields for every H2.

Product risk:

The article may feel assembled from modules rather than written.

### Type D: Fake Precision Risk

The system uses scores or percentages where the underlying judgment is subjective.

Examples:

- Benchmark alignment score.
- Opportunity score.
- Structural similarity threshold.
- Weighted topic scoring.

Product risk:

The operator may trust a number instead of reading the actual reasoning.

### Type E: Example Contamination Risk

The system includes highly specific sample outputs that can become default style.

Examples:

- Repeated Metal Divider / Riyadh / Rose Gold / PVD examples.
- Legacy examples from another product category.
- Repeated hotel / restaurant / villa scenario patterns.

Product risk:

Future outputs may imitate the example rather than the current project profile or selected benchmark.

## High-Severity Findings

### Finding 1: AIO Capture Is Important, But Current Rules Make It Too Fixed

Files:

- `.claude/skills/voice-and-humanization/SKILL.md`
- `.claude/skills/article-draft/SKILL.md`
- `.claude/skills/article-reader-qa/SKILL.md`
- `scripts/run_qa_verifier.py`

Observed risk:

The system currently treats AIO readiness through bold-answer rules:

- Default target: one bold sentence per H2.
- Question H2s must have a bold answer early.
- Bold answer should be objective, standalone, and within a narrow word-count window.
- The QA verifier warns if question headings lack bold answers or if bold answers fall outside the preferred range.

Product meaning:

AIO is a valid strategic target. The issue is not AIO itself.

The issue is that the rules can make every question-style section behave the same way. That is not how strong benchmark-led articles work.

Correct direction:

AIO capture should be dynamic and opportunistic.

- Capture as many AIO opportunities as the article naturally supports.
- Do not set a fixed target number.
- Do not force every H2 to become an AIO unit.
- Do not let snippet syntax override benchmark rhythm.
- Let evidence strength and reader intent decide where answerable sentences belong.

The better rule is:

Every strong answer opportunity should be made extractable, but only where extractability improves the article rather than interrupting it.

### Finding 2: Per-H2 Tier 1 Requirements Can Flatten Article Rhythm

Files:

- `.claude/skills/evidence-policy/SKILL.md`
- `.claude/skills/article-skeleton/SKILL.md`
- `.claude/skills/article-information-gain-qa/SKILL.md`
- `.claude/skills/quality-gates/SKILL.md`
- `templates/section-contracts.md`
- `templates/information-gain-qa.md`

Observed risk:

Several surfaces push the same logic:

- Every H2 section should have a Tier 1 anchor.
- Information Gain QA blocks any H2 with zero Tier 1.
- Section contracts ask for required evidence and unique expertise contribution for each H2.

Product meaning:

This protects against generic content, but it can also create overstuffed sections.

Not every section has the same job. Some sections exist to set up tension, move the reader, contrast ideas, or let a previous point land.

Correct direction:

Evidence should be mandatory at the article level and in decision-critical sections. It should not be spread evenly like seasoning.

High-impact evidence should appear where it changes the reader's decision.

### Finding 3: Benchmark Extraction And Structure Rules Still Fight Each Other

Files:

- `.claude/skills/article-benchmark-extract/SKILL.md`
- `.claude/skills/benchmark-transmutation/SKILL.md`
- `.claude/skills/article-skeleton/SKILL.md`
- `.claude/skills/structure-variation/SKILL.md`

Observed risk:

The system says to copy benchmark structure, but extraction warns against section templates, H2 sequence, and format prescriptions. Then structure variation blocks consecutive same-format sections.

Product meaning:

The system is trying to avoid copying badly, but it may prevent copying well.

Correct direction:

Benchmark extraction should produce a Structural Blueprint:

- Reader movement.
- Section job sequence.
- Pacing shifts.
- Repetition that is intentional.
- Repetition that is just brand habit.
- Where the article becomes answerable.
- Where the article slows down or speeds up.

Skeleton should then transform that blueprint for the current project.

### Finding 4: Reader QA Is Not Yet A Strong Anti-Template Gate

Files:

- `.claude/skills/article-reader-qa/SKILL.md`
- `templates/reader-qa.md`
- `.claude/skills/quality-gates/SKILL.md`

Observed risk:

Reader QA checks natural lead, transitions, rhythm, repetitive definitions, machine-answer tone, and brand credibility.

These are useful, but too light for the real failure mode: an article can pass all of them and still feel safe, flat, and assembled.

Correct direction:

Reader QA should explicitly block template-feeling articles:

- If sections are individually correct but collectively lifeless.
- If the reader has no reason to continue after a section.
- If every section opens, proves, and closes in the same emotional pattern.
- If AIO answers interrupt the article's pull.
- If enrichment blocks make the article feel like a product page.

## Medium-Severity Findings

### Finding 5: Enrichment Is A Lower-Priority Template Risk

Severity: low to medium after operator review.

Files:

- `.claude/skills/article-enrich/SKILL.md`
- `.claude/skills/image-strategy/SKILL.md`
- `.claude/skills/internal-linking/SKILL.md`
- `templates/image-plan.md`

Observed risk:

The draft is intentionally pure prose, but enrichment then adds:

- Image placeholders.
- A/B/C/D option blocks.
- Resource cards.
- Accordions.
- Reader-stage routing.
- Fixed link and visual density guidance.

Product meaning:

This is useful operationally and usually enriches the article through material, proof, navigation, and visuals. It becomes risky only if it forces identical visual/link furniture into every article or changes the prose logic.

Specific risks:

- `article-enrich` says roughly 5-8 visual opportunities for a 3,000-word article.
- `internal-linking` gives fixed density for inline links, resource blocks, and accordions.
- `image-strategy` says every article should have at least one generated chart or diagram.
- `image-plan` template shows total visual opportunities as 7 and density as about 1 image per 400-500 words.

Correct direction:

Visuals and links should be dynamic:

- Add them where they improve comprehension, trust, or action.
- Skip them where they interrupt the argument.
- Prefer fewer stronger elements over meeting density ranges.
- Let benchmark visual rhythm influence the enrichment layer.

### Finding 6: Internal Linking Has Format Contradictions And Visible Pattern Risk

Files:

- `.claude/skills/internal-linking/SKILL.md`
- `.claude/skills/article-enrich/SKILL.md`

Observed risk:

`internal-linking` says FAQ accordions should use `[su_accordion]` and `[su_spoiler]`. `article-enrich` later says add `<details><summary>...</summary>...</details>`.

It also standardizes resource blocks with bold arrow links and bullets.

Product meaning:

The contradiction can create inconsistent outputs. The repeated resource-block format can also become visually recognizable across articles.

Correct direction:

There should be one platform-specific shortcode policy, but the editorial decision to use an accordion/resource block should remain dynamic.

### Finding 7: Image Strategy Is Strong, But Too Much Example Gravity Exists

Files:

- `.claude/skills/image-strategy/SKILL.md`
- `templates/image-plan.md`
- `.claude/skills/image-strategy/references/html-infographic-patterns.md`

Observed risk:

The strategy correctly says images should be placed by cognitive decision point, not per H2. But the later instructions include dense option mechanics, fixed visual counts, fixed dimensions, and many specific examples.

Product meaning:

The system may start producing the same visual architecture repeatedly:

- hero image,
- application photo,
- detail image,
- comparison visual,
- process diagram,
- proof image,
- CTA visual.

Correct direction:

Keep the cognitive-decision principle. Make the type mix dynamic.

The article should not receive a visual type just because the taxonomy has a slot for it.

### Finding 8: Six-Node Arc Is Useful, But Should Not Become A Universal Story Template

Files:

- `.claude/skills/article-arc/SKILL.md`
- `.claude/skills/article-skeleton/SKILL.md`

Observed risk:

The arc model has fixed nodes:

- Starting State.
- Opening Reframe.
- First Turn.
- Middle Build.
- Trust Shift.
- Arrival State.

Product meaning:

This is a good mental model. But if every article must visibly follow the same emotional choreography, the system may produce predictable articles.

Correct direction:

Use the six nodes as diagnostic coverage, not a visible plot template.

Some article types may need a fast trust shift. Some may need no dramatic reframe. Some may be comparison-first. Some may be case-proof-first.

### Finding 9: Topic Scoring Is Operationally Useful But Strategically Overconfident

Files:

- `.claude/agents/topic-cluster-researcher.md`
- `templates/deep-seo-card.md`

Observed risk:

The topic workflow uses:

- 14-field cards.
- 5 weighted scoring dimensions.
- T1/T2/T3 thresholds.
- 50+ candidate pool.
- 8+ strategic pillars.

Product meaning:

This can help prioritize, but the numbers should not pretend to be truth. Topic opportunity depends on SERP volatility, content quality, business proof, conversion intent, and timing.

Correct direction:

Keep scoring as an aid, but require qualitative operator judgment:

- Why this topic now?
- What unique proof can we bring?
- What would make this article impossible for competitors to copy?
- What is the hidden risk if we rank but attract the wrong reader?

## Lower-Severity Findings

### Finding 10: Templates Are Useful For Artifacts, But Some Templates Contain Default Content Shape

Files:

- `templates/section-contracts.md`
- `templates/image-plan.md`
- `templates/publish-package.md`
- `templates/reader-qa.md`

Observed risk:

Artifact templates help execution, but they also imply what every article should contain.

Product meaning:

Templates should capture required records, not force the same editorial shape.

Correct direction:

Keep templates for traceability. Avoid embedding sample article architecture as if it were universal.

### Finding 11: Examples Are Too Specific And Can Leak Into Outputs

Files:

- `.claude/skills/voice-and-humanization/SKILL.md`
- `.claude/skills/image-strategy/SKILL.md`
- `.claude/skills/internal-linking/SKILL.md`
- `templates/image-plan.md`

Observed risk:

Many examples use the same product world: metal dividers, Riyadh, hotel lobby, PVD Rose Gold, 316 stainless, QC gates.

Product meaning:

If this project is meant to generalize across B2B clients, those examples may contaminate outputs. If the project is only for that one business, this is less risky.

Correct direction:

Examples should either be clearly marked as project-specific or replaced with abstract placeholders that still show the decision logic.

## What Is Not Template Risk

Not every strict rule is bad.

These should remain hard:

- Locked profile gate.
- No invented project context.
- Source traceability for factual claims.
- No fake real-photo paths.
- No AI image presented as real project proof.
- Publish requires QA completion.
- State transitions must be durable.

These are operational safety rules, not editorial templates.

## Highest-Leverage Fixes If Editing Is Approved Later

1. Create a global rule: fixed counts are suggestions only unless tied to factual safety or platform validity.

2. Reframe AIO as dynamic capture:
   - Capture as many natural opportunities as possible.
   - Do not use a fixed count.
   - Do not force every H2 to become an answer unit.
   - Let benchmark rhythm decide placement.

3. Split `voice-and-humanization` into clearer responsibilities:
   - Human judgment and field voice.
   - Anti-AI pattern cleanup.
   - AIO capture guidance as a separate, optional layer.

4. Replace per-H2 Tier 1 enforcement with article-level and decision-section enforcement.

5. Change `structure-variation` from "no consecutive same format" to "no lazy repetition; intentional benchmark rhythm is allowed."

6. Upgrade Reader QA to detect template feeling:
   - no pull,
   - no tension,
   - no earned judgment,
   - assembled-module feel,
   - enrichment clutter.

7. Make visual and link density dynamic:
   - no default visual count,
   - no default link count,
   - no required chart if no chart improves the article.

8. Remove or downgrade fake precision:
   - benchmark percentages,
   - fixed alignment thresholds,
   - topic scores as final truth.

9. Clean shortcode contradiction between `internal-linking` and `article-enrich`.

10. Mark domain-specific examples as examples only, not reusable defaults.

## Product-Level Conclusion

The system should not become less ambitious.

It should become more dynamic.

The target is:

- benchmark-led structure,
- dynamic AIO capture,
- strong proprietary evidence,
- human persuasion,
- enrichment only where it improves the reading path,
- QA that blocks template-feeling output even when all boxes are checked.

That is the path away from "complete but flat" and toward articles that can compete for AI Overview without sounding like they were written for a machine.
