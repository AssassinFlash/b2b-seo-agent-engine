---
name: quality-gates
description: "Use when: (1) a draft is complete and needs Truth QA in /article-truth-qa, (2) verifying Information Gain in /article-information-gain-qa, (3) checking benchmark fidelity in /article-benchmark-qa, (4) verifying human reading quality in /article-reader-qa. The four QA gates that protect every article before publishing. Each gate has pass/block authority — no article proceeds past a blocking gate."
user-invocable: false

---

# Quality Gates

## Purpose

Prevent articles from reaching publishable state with unverified claims, generic content, broken benchmark structure, or mechanical prose. Each gate has blocking authority — a single BLOCK stops progression until the issue is repaired.

## When to Use

- `/article-truth-qa`: Gate 1 — fact verification
- `/article-information-gain-qa`: Gate 2 — unique expertise check
- `/article-benchmark-qa`: Gate 3 — benchmark structure fidelity
- `/article-reader-qa`: Gate 4 — human reading experience

## Instructions

### Gate 1 — Truth QA

Verify that the draft stays inside its evidence boundaries. Strict mode verifies every factual claim against its evidence source. Light / non-blocking mode (operator-requested) relies on the upstream `evidence-opinion-pack.md`, checks obvious contradictions and red lines, and records draft-born performance hooks / estimates as watchlist items without redoing full research.

Check: product specs, certifications, factory claims, project data, client quotes, market claims, and any draft-born claims that appeared during writing.

**Block if**: strict mode finds an unverified factual claim, borrowed case as owned, red-line violation, or safety/comparative/unit issue; light mode finds a clear red-line violation, impossible claim, dangerous safety claim, or obvious contradiction with the evidence pack. Do not block a supportable strong stance merely because it is aggressive.

**Template**: `templates/truth-qa.md`

### Gate 2 — Information Gain QA

Verify the article contains information only THIS business could provide and actively beats the current SERP consensus vector (Google Information Gain patent `US20200349181A1`). The core test: if a competitor replaced the brand name, would the article still feel mostly intact? If yes → BLOCK and diagnose which sections are replaceable.

**Block if**:
- The article is mostly replaceable by a competitor or merely echoes the platitudes listed in `intent-research.md`'s **SERP Consensus Target** without dismantling/qualifying them;
- Decision-critical sections lack Tier 1 **Forensic Specificity** (caliper/instrument metrics, tolerances, pass/fail QC failure anatomy);
- The article lacks **Anti-Sell Disqualification Boundaries** (never tells the buyer when NOT to buy the high-spec option);
- Or Tier 1 material is present in the profile/fact-library but unused where it changes the reader's decision.

**Template**: `templates/information-gain-qa.md`

### Gate 3 — Benchmark Drift QA

Verify the article still follows the benchmark success formula — not the competitor's structure, but the Structural Blueprint and reader advancement mechanism extracted during benchmark-extract. Check that answerability structures didn't create mechanical SEO templates, and verify that the **Above-the-Fold Viewport Contract** (first ~180 words + micro-anchor) and **Buying Committee Internal-Champion Enablement** were executed as planned.

**Block if**: the article type has drifted from the benchmark formula, pacing is broken, the opening fails the Above-the-Fold 3-second anti-pogo test, or answerability blocks feel forced.

**Template**: `templates/benchmark-drift-audit.md`

### Gate 4 — Reader QA

Verify the article reads like one continuous piece written for humans — not stitched-together modules. Check for rhythm variation, format monotony, natural transitions, **Self-Contained RAG Citation Chunks** (40–60 word H2 openings with explicit subject entity + condition + verdict + metric, zero dangling pronouns), **Named Engineer/Author voice consistency**, and **Buying Committee dual-register** (technical depth for specifiers + TCO/risk clarity for approvers).

**Block if**: the draft lacks a Numeric Control Vector, the article feels complete but flat, repeated formats feel lazy rather than benchmark-native, the opening doesn't give an answer + reframe + path preview in the first ~200 words (the 3-second / dwell-time test), the trust shift feels like a "why choose us" section, full-sentence AI-citation bolds are missing in multiple H2s, AIO answers interrupt the prose, or prose reads like a supplier wrote it.

**Diagnose control drift**: check whether the draft stated and followed its Numeric Control Vector:
- Imitation / injection / differentiation ratio (with the spec-heavy B2B common-case being **differentiation ≥ imitation** when proprietary evidence is the main advantage — do not flag differentiation-led ratios as drift)
- AIO / bold targets — distinguish **full-sentence bold (≥8 words, AI citation anchors, at least 1 per H2 default)** from **short navigation bolds (<8 words, structural labels, not counted toward AI anchors)**; under-controlled = no full-sentence anchors; over-controlled = inflated short bolds without a real anchor
- Opinion intensity — normal range 4-8 for B2B buyer guides; **7-8 is the stance climax default at decision sections, not a drift signal**. 9-10 without proprietary proof is drift. Below 4 when buyer risk is high is drift. See `voice-and-humanization` Opinion Intensity Scale + Stance vs Hype Boundary.
- Evidence pressure
- Format rhythm
- Opener dwell-time test (first ~200 words: direct answer + reframe hook + path/framework preview)
- Continue-reading hooks at H2 endings (each non-final H2 should hook the next section)

Missing or violated controls should be named as drift causes, not hidden behind vague "quality" feedback. **Hype words at any intensity are always drift** (see `voice-and-humanization` Stance vs Hype Boundary); quantified stance at 7-8 is not drift.

**Template**: `templates/reader-qa.md`

---

## Examples

### Input (draft section):
```
### Materials
Our screens are made from 304 and 316 stainless steel. 
304 is good for indoor use. 316 is better for outdoor use. 
We also offer aluminum options.
```

### Gate 2 (Information Gain) output: BLOCK
- Decision-critical material section has no Tier 1 source anchoring the claim
- Any competitor could write this section verbatim
- No project example, no specific data, no judgment

### After repair:
```
### Choose the Material by Environment, Not by Appearance
[Passes — anchored in Riyadh project (316 SS, 200+ panels), 
Singapore project (304 SS, 45 panels), includes conditional 
judgments and specific failure modes]
```

---

## Guardrails

### Anti-Patterns
- Treating QA as a rubber stamp — gates have real blocking authority
- Running QA gates out of order (Truth before Info Gain before Benchmark Drift before Reader)
- Skipping a gate because the previous one passed
- Fixing surface issues without addressing the root cause of a block

### When to Ask for Clarification
- A claim appears in multiple places with conflicting evidence
- The operator is the only source for a critical fact (flag as `user-needed`, do not assume)

### Gate Authority
All four gates must PASS before `/article-publish-pack`. A BLOCK at any gate stops progression. Fix the issue, re-run the gate, and only proceed when it clears.
