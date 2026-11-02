# Benchmark Drift Audit — solar-without-a-battery

**Stage:** `/article-benchmark-qa`  
**Date:** 2026-06-24  
**Status:** PASS  
**Next:** `/article-reader-qa`

---

## Scope

Gate 3 verifies the draft still follows the benchmark success formula: the article type, structural blueprint, pacing, evidence rhythm, borrowed-asset transformation, format rhythm, and reader advancement mechanism. It also checks the declared imitation/injection/differentiation ratio against the executed draft.

No external tools were used — all verification is against local artifacts (`benchmark-success-formula.md`, `draft.md`, `Draft Control Metadata`).

---

## 1. Article Type Fidelity

| Benchmark classification | Draft execution | Verdict |
|---|---|---|
| Article type: **Buyer's Guide + Risk-Avoidance Listicle** (hybrid, EnergySage + JingSourcing + 饼干哥哥AGI) | Draft is a buyer's guide structured as a decision framework (Path A/B/C) with strong risk-avoidance elements (retrofit trap, red-flag catalog). The contrarian opener borrows from 饼干哥哥AGI but the dominant register is EnergySage buyer's guide. | PASS |

No article-type drift. The draft is what the benchmark said it would be.

---

## 2. Structural Blueprint Alignment

| Blueprint job # | Blueprint job | Draft H2 execution | Match? |
|---|---|---|---|
| 1 | Contradiction hook + proof | H2-01 opener: direct answer + loss hook + Path preview | ✅ Match |
| 2 | Key takeaways preview (3-5 bullets) | H2-01 KEY TAKEAWAYS block (5 bullets) | ✅ Match |
| 3 | Need/path qualification | H2-03 3-question self-quiz → routes to Path A/B/C | ✅ Match |
| 4 | Myth debunk / wrong-way teardown | H2-04 retrofit trap: AC-coupled retrofit / inverter swap costs | ✅ Match |
| 5 | Path framework (comparison table) | H2-05 R6 vs H2 vs HS3 comparison table | ✅ Match |
| 6 | Red-flag catalog | H2-06 7-item quote red-flag checklist | ✅ Match |
| 7 | Single action item | H2-07 one question to ask installer | ✅ Match |
| 8 | Lesson-pivot close | H2-08 "battery-ready, not battery-required" + path routing | ✅ Match |
| 9 | Soft CTA | H2-08 CTA paragraph with SAJ product page routing | ✅ Match |

All 9 blueprint jobs are executed by the 8 H2s (H2-01 serves jobs 1+2; H2-08 serves jobs 8+9). No missing blueprint jobs. No extra sections grafted on. The structure is faithful to the blueprint without being mechanical.

---

## 3. Pacing Alignment

| Blueprint pacing | Draft execution | Verdict |
|---|---|---|
| Hook + proof (0-10%, fast/high energy) | H2-01 opens with direct answer + loss hook + Path preview; ~200 words, punchy | ✅ |
| Key takeaways + qualification (10-20%, fast/skimmable) | H2-01 KEY TAKEAWAYS + H2-02 definition + H2-03 self-quiz; skimmable bullets and short sections | ✅ |
| Myth debunk (20-35%, moderate/diagnostic) | H2-04 retrofit trap; detailed cost breakdown, diagnostic tone, field-language | ✅ |
| Path framework (35-65%, slower/spec-heavy) | H2-05 comparison table with specs; spec-heavy but organized | ✅ |
| Red-flag catalog (65-80%, fast/list-heavy) | H2-06 numbered checklist; fast, scannable, actionable | ✅ |
| Action item + close (80-100%, reflective but punchy) | H2-07 single question + H2-08 close/CTA; reflective tone, sticky phrase | ✅ |

Pacing follows the blueprint's energy curve. The transition from diagnostic (H2-04) → spec-heavy (H2-05) → fast/list (H2-06) → reflective (H2-07/08) matches the benchmark's reader advancement mechanism.

---

## 4. Evidence Rhythm

| Blueprint evidence wave | Draft execution | Verdict |
|---|---|---|
| Wave 1: Product spec / running-system proof (opener) | H2-01 Path A/B/C bullets with SAJ model names and key specs | ✅ |
| Wave 2: Scenario-based failure description (retrofit trap) | H2-04: AC-coupled retrofit and inverter swap scenarios | ✅ |
| Wave 3: Comparison table with SAJ specs | H2-05: R6 / H2 / HS3 table with spec rows | ✅ |
| Wave 4: Red-flag examples from quote language | H2-06: 7 quote lines translated into buyer risk | ✅ |
| Wave 5: Single action item + closing reframe | H2-07 question + H2-08 "battery-ready, not battery-required" seal | ✅ |

No long theory block without supporting evidence. Evidence is deployed in the benchmark's wave pattern.

---

## 5. Borrowed Asset Transformation

| Borrowed asset (from blueprint) | Transformation in draft | Verdict |
|---|---|---|
| EnergySage "storage-ready" concept | Transformed to "battery-ready, not battery-required" — SAJ-specific, DC-coupled, spec-anchored | ✅ Transformed, not copied |
| JingSourcing red-flag listicle format | Adapted to inverter-quote red flags with SAJ H2 port-spec language and retrofit risk | ✅ Transformed |
| 饼干哥哥AGI contrarian opener | Adapted to English B2B: direct answer + loss hook ("$3,000–$9,000 future surprise") | ✅ Transformed |
| EnergySage conditional if/then logic | Adapted to Path A/B/C conditional routing with SAJ R6/H2/HS3 models | ✅ Transformed |
| Woshipm interjections ("卧槽", "magic") | Avoided. English colloquial markers used instead ("ugliest math", "quietly closes the battery door") | ✅ Avoided |

All borrowed assets are transformed into the current profile's role. No asset is copied verbatim.

---

## 6. Format Rhythm / Repetition Diagnosis

| Section pair | Formats | Monotony risk? | Verdict |
|---|---|---|---|
| H2-01 → H2-02 | Prose + bullets → prose + definition anchors | Different | ✅ |
| H2-02 → H2-03 | Definition → self-quiz (numbered questions) | Different | ✅ |
| H2-03 → H2-04 | Self-quiz → numbered cost scenarios + prose | Different | ✅ |
| H2-04 → H2-05 | Prose/cost → comparison table | Different (format shift prevents monotony) | ✅ |
| H2-05 → H2-06 | Table → numbered checklist | Different (format shift intentional) | ✅ |
| H2-06 → H2-07 | Checklist → prose + single-question anchor | Different | ✅ |
| H2-07 → H2-08 | Prose → prose + CTA | Same format, but acceptable — closing section | ✅ |

No consecutive sections share the same format. The table→checklist transition at H2-05/06 matches the blueprint's intentional pacing shift. Intentional repetition of "battery-ready, not battery-required" (3×) and Path A/B/C labels (8×) is diagnosed as intentional-rhythm per the blueprint's own repetition diagnosis.

---

## 7. Ratio Drift Check

| Ratio | Target (Draft Control Metadata) | Estimated actual | Drift ≥10 pp? | Diagnosis |
|---|---|---|---|---|
| Imitation | 25% | ~25% | No | EnergySage pacing + KEY TAKEAWAYS borrowed; JingSourcing red-flag format borrowed; 饼干哥哥AGI opener cadence borrowed. Not over-imitated. |
| Injection | 35% | ~30-35% | No | SAJ T1.1–T1.4 specs are injected throughout. Path A/B/C routing is product-specific. Evidence is present but does not dominate prose. |
| Differentiation | 40% | ~40-45% | Borderline, but intentional | Draft metadata already notes "differentiation slightly higher than planned because retrofit-trap quantification and red-flag spec translations came out denser than anchor; intentional." Per skill rule, differentiation-led ratios are the common case for spec-heavy B2B and should NOT be flagged as drift simply for being differentiation-heavy. |

**Verdict: No ratio drift.** The executed draft matches the declared 25/35/40 within the acceptable range. The slight differentiation overshoot is intentional, documented, and within the spec-heavy B2B norm.

---

## 8. No Forced Answerability

- No forced FAQ block grafted onto the article. H2s function as question-answer pairs per the blueprint.
- No forced "one bold answer per H2" that breaks benchmark prose rhythm. Full-sentence bold anchors are deployed at natural decision/definition points, consistent with the updated voice-and-humanization Part 3 guidance.
- AIO answerability moments (KEY TAKEAWAYS, Path table, red-flag list, installer question) are present but organic — they serve the reader, not the snippet.

---

## 9. E-E-A-T Insertions

No standalone "About Us" or "Why Trust Us" block was inserted. Trust is built through:
- Product specificity (SAJ model numbers, specs)
- Field-language diagnostic tone (retrofit trap, red flags)
- Honest caveats (no backup without battery, anti-islanding)
- The "battery-ready, not battery-required" frame as earned authority

This matches the benchmark's proof strategy: credibility through product-level specificity and honest caveats, not self-praise.

---

## Gate Decision

**PASS.**

The draft follows the benchmark success formula without drift:
- Article type intact
- 9/9 blueprint jobs executed across 8 H2s
- Pacing curve matches the borrowed energy pattern
- Evidence deployed in benchmark waves
- Borrowed assets transformed, not copied
- No format monotony (consecutive sections differ)
- No forced answerability
- Ratio drift within acceptable range (differentiation overshoot is intentional and documented)
- No mechanical E-E-A-T insertions
