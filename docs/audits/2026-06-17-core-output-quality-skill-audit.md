# 2026-06-17 Core Output Quality Skill Audit

Mode: read-only audit. No active Skill, Agent, Script, config, or template file was changed.

Purpose: inspect whether the core article-production chain can produce writing that is not only complete, but genuinely persuasive, human, benchmark-led, and hard to dismiss.

Scope reviewed:

- `.claude/skills/article-benchmark-extract/SKILL.md`
- `.claude/skills/benchmark-transmutation/SKILL.md`
- `.claude/skills/article-skeleton/SKILL.md`
- `.claude/skills/article-draft/SKILL.md`
- `.claude/skills/article-reader-qa/SKILL.md`
- `.claude/skills/article-benchmark-qa/SKILL.md`
- `.claude/skills/article-information-gain-qa/SKILL.md`
- `.claude/skills/quality-gates/SKILL.md`
- `.claude/skills/structure-variation/SKILL.md`
- `.claude/skills/voice-and-humanization/SKILL.md`
- `.claude/skills/article-evidence-opinions/SKILL.md`

## Executive Verdict

The project already has a serious quality system. The problem is not absence of standards.

The real issue is that several standards pull the writer in different directions:

1. The system says the article should copy benchmark structure, rhythm, and reasoning.
2. The benchmark extraction Skill blocks structure too early by saying the extraction is not a section template, not an H2 sequence, and not a format prescription.
3. The skeleton and information-gain gates force every section to carry Tier 1 evidence, which can flatten sections that should mainly serve pacing, persuasion, setup, or transition.
4. The draft Skill has the right writing ambition, but the post-draft checks drift into fake precision and mechanical proof.
5. Reader QA is too light for the user's real quality problem: articles that look finished but feel flat.

So the current system is capable, but it is not yet "unbeatable." It can create an article that passes gates while still missing benchmark energy, narrative pull, and human persuasion.

## Finding 1: Benchmark Structure Copying Is Required, But Benchmark Extraction Suppresses It Too Much

Severity: high.

Evidence:

- `article-benchmark-extract` says the output is "NOT a section template, NOT an H2 sequence, NOT a format prescription" and reserves those decisions for skeleton design.
- `benchmark-transmutation` says the new rule is "copy the structure, transform the content, differentiate the voice."
- `article-skeleton` says to ask how benchmark articles structured their sections, then imitate rhythm and evidence deployment pattern.

Product meaning:

The system wants the writer to copy structure, but the earliest benchmark-learning stage is afraid of outputting structure. That weakens the entire chain, because skeleton has to imitate structure without receiving enough structural material from the extraction stage.

This does not mean benchmark extraction should output final H2s. It should not lock the final outline too early.

But it should output a borrowable structural blueprint:

- What order the benchmark uses to move the reader.
- Which section jobs appear and why.
- Where the article gets fast, slow, skeptical, practical, or decisive.
- Which structural moves are worth copying.
- Which moves are only brand habit and should not be copied.

Decision implication:

The right direction is not "do not copy." The right direction is:

Copy the benchmark's working structure, then transform the content and adjust the voice.

## Finding 2: Per-Section Tier 1 Requirements Are Too Rigid For High-End Writing

Severity: high.

Evidence:

- `article-skeleton` says each H2 must attach to a Tier 1 anchor.
- `article-information-gain-qa` blocks any H2 with zero Tier 1 anchor.
- `quality-gates` blocks any H2 section with zero Tier 1 sources.

Product meaning:

This is a strong anti-generic rule, but it is too blunt. A persuasive article often needs some sections whose main job is pacing, reframing, emotional setup, contrast, transition, or decision framing.

If every H2 is forced to prove itself through Tier 1 evidence, the article can become dense but not better. It may sound complete while losing rhythm.

Decision implication:

Information gain should remain important, but it should be judged at article level and at key decision-section level, not mechanically at every H2.

The stronger product rule is:

- The article must contain proprietary insight.
- The important decision sections must be anchored in proprietary evidence.
- No major claim should be unsupported.
- But not every section needs to carry the same evidence burden.

## Finding 3: Reader QA Does Not Yet Catch "Complete But Flat"

Severity: high.

Evidence:

- `article-reader-qa` checks format monotony, voice lens execution, opinion intensity, bold usage, transitions, human texture, supplier voice, and opening strength.
- Its blocking cases are mostly: repeated format, weak opening, supplier catalog tone, and failed voice lens use.

Product meaning:

These are useful checks, but they mostly catch obvious defects. They do not fully catch the most dangerous defect: a draft that has all required parts, all evidence, all headings, and still does not pull the reader forward.

That is exactly the failure mode the user cares about.

Reader QA should ask harder editorial questions:

- Would a serious reader keep going after each section?
- Does each section create tension, answer it, or raise the next useful question?
- Is there any paragraph that sounds correct but has no pressure, judgment, or movement?
- Does the article preserve the benchmark's energy, not just its outline?
- Does the writing feel authored, or assembled?

Decision implication:

Reader QA should become the main "flatness blocker." It should not just check polish; it should be allowed to reject a structurally complete but emotionally and rhetorically weak article.

## Finding 4: Draft Skill Has The Right Ambition, But Some Proof Language Is Mechanical

Severity: medium.

Evidence:

- `article-draft` correctly requires full benchmark reading, one continuous pass, primary benchmark voice anchoring, and no subagents for drafting.
- It says the benchmark is the authority if the Humanizer conflicts with benchmark-intentional style.
- But it also asks Humanizer to produce a quantified report and says to report "0 AI patterns detected across 33 pattern types" when no detections appear.
- The phrase "Ask the user to select" appears twice in the benchmark-anchor selection flow.

Product meaning:

The drafting core is one of the strongest parts of the project. It understands that article quality depends on continuity, rhythm, and benchmark voice.

But the proof layer is weaker than the writing layer. A numbered report can make the system feel rigorous without proving that the article is good.

Decision implication:

Keep the draft philosophy. Do not dilute it.

Clean up duplicate instructions and replace fake precision with editorial evidence:

- What benchmark moves were successfully imitated?
- Where did the draft preserve rhythm?
- Which AI-default patterns were actually removed?
- Which flagged patterns were kept because they were benchmark-native?

## Finding 5: Benchmark QA Uses A Score That Looks Precise But Is Not Grounded

Severity: medium.

Evidence:

- `article-benchmark-qa` example outputs "Success formula alignment score: 85%."
- The Skill does not define a robust scoring rubric that would make 85% meaningful.

Product meaning:

This creates false confidence. The user does not need a number that sounds scientific; the user needs to know whether the draft learned why the benchmark works.

Decision implication:

Benchmark QA should move away from numeric scoring and toward specific drift findings:

- Which benchmark structural moves were preserved?
- Which were lost?
- Where did the draft copy shape but miss the reason?
- Where did SEO answerability damage the benchmark rhythm?
- Where did evidence injection make the article stronger or heavier?

## Finding 6: Structure Variation Is Useful, But It Must Not Destroy Benchmark-Native Rhythm

Severity: medium.

Evidence:

- `structure-variation` blocks repeated consecutive formats.
- `benchmark-transmutation` says some benchmark uniformity is source-brand habit and should not be copied.
- `article-skeleton` and `article-draft` apply the no-consecutive-same-format rule.

Product meaning:

The variation rule protects against template writing. That is good.

But if applied mechanically, it can also break a benchmark's successful rhythm. Some high-performing articles use intentional repetition to create reader confidence. The system should not copy lazy repetition, but it should be allowed to preserve intentional rhythm.

Decision implication:

The rule should mean:

Do not repeat formats because the model is lazy.

It should not mean:

Break a benchmark's rhythm even when repetition is the reason the article works.

## Finding 7: Voice And Humanization Is Strong As A Support Skill, Weak As A Master Rule

Severity: medium.

Evidence:

- `voice-and-humanization` gives useful guidance on judgments, trade-offs, field language, and avoiding generic marketing.
- It also includes default bold density, question-H2 bold answer requirements, objective third-person snippet rules, and word-count windows.

Product meaning:

The humanization Skill is valuable when it helps the writer sound specific, situated, and judgmental.

It becomes risky when it turns writing into a checklist of extractable sentences. That can conflict with benchmark-led prose and make the article feel optimized instead of authored.

Decision implication:

Use this Skill as a filter and craft aid, not as the master aesthetic.

The primary master should be:

Full benchmark article, copied structure, copied rhythm, transformed substance, and project-specific judgment.

## What I Would Not Change First

I would not start by deleting Agents.

I would not start by rewriting scripts.

I would not start by expanding security or fake-fact controls, because that is not the user's current highest concern.

I would not use the existing example article as a quality standard.

I would not define a "golden sample" rubric for the user. The user's eye should remain the final standard.

## Highest-Leverage Fix Order If Editing Is Approved Later

1. Align `article-benchmark-extract`, `benchmark-transmutation`, and `article-skeleton` so benchmark extraction produces both:
   - Structural Blueprint: what to copy.
   - Reader Advancement Logic: why it works.

2. Relax per-H2 Tier 1 requirements into article-level and key-decision-section requirements.

3. Upgrade `article-reader-qa` into a real flatness blocker.

4. Replace benchmark QA scoring with concrete drift diagnosis.

5. Clean `article-draft` duplicate selection wording and make Humanizer proof editorial instead of numeric.

6. Clarify that `structure-variation` prevents lazy repetition, not intentional benchmark-native rhythm.

## Product-Level Conclusion

The current system is not broken. It is over-instructed in some places and under-instructed in the most subjective place: judging whether the article actually has force.

The project should keep its benchmark-led direction. The user is right that structure should be copied.

The next real improvement is to make the chain learn and preserve the benchmark's structure, rhythm, and persuasion logic, while using evidence and QA to strengthen the article instead of making it mechanically compliant.
