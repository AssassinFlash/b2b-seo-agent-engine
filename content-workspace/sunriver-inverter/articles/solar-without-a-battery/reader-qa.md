# Reader QA — solar-without-a-battery

**Stage:** `/article-reader-qa`  
**Date:** 2026-06-24  
**Status:** PASS  
**Next:** `/article-enrich`

---

## Human Reading Checks

| Check | Assessment | Verdict |
|---|---|---|
| Natural lead | Opens with direct answer, not generic preamble. No "energy storage is the rising star." Reframe hook lands in sentence 2. | ✅ Passes 3-second test |
| Section transitions | Each H2 ending hooks the next with a loss frame, question, or quantified tease. "Here is how to spot which one does it." / "Here is what the real math looks like." / "These are the lines to watch for." | ✅ Clean, hook-driven |
| Paragraph rhythm | Short paragraphs (1-3 sentences). EnergySage cadence. Mix of single-line punches ("That is the retrofit trap in plain English.") and diagnostic paragraphs. No wall of text. | ✅ Natural |
| Lists and tables feel helpful | H2-05 comparison table is the article's structural anchor. H2-06 red-flag checklist is scannable and actionable. H2-03 numbered questions feel diagnostic, not formulaic. | ✅ Helpful, not mechanical |
| No repetitive definition pattern | H2-02 defines battery-ready but only once. No definitional echo across sections. Each section serves a distinct reader job. | ✅ |
| No visible machine-answer tone | No "in this article we will discuss." No "furthermore / moreover / in conclusion." No passive-voice bloat. Colloquial field-language throughout ("ugliest math," "quietly closes the battery door," "scramble"). | ✅ |
| Brand role feels credible | Sunriver speaks as supply partner / SAJ distributor. Path A/B/C routing is product-specific without being sales-pitchy. CTA is path-routing, not hard sell. | ✅ |
| Reader pull after each major section | All 7 non-final H2s end with a continue-reading hook. Loss frames, questions, and quantified teases alternate. No section dead-ends. | ✅ |
| Complete-but-flat sections | None. Even the qualification section (H2-03) builds toward a concrete routing decision. Definitional section (H2-02) uses the weak/real/premium three-way frame to create structure. | ✅ |
| Benchmark energy preserved | EnergySage conditional-answer cadence + JingSourcing red-flag rhythm + 饼干哥哥AGI opener punch are all present. The article reads like a buyer's guide, not a whitepaper. | ✅ |
| AIO answers feel natural | KEY TAKEAWAYS block, Path table, red-flag translations, and installer question are all organic. No forced "bold answer per H2" that breaks prose rhythm. Full-sentence bolds are at natural decision/definition points. | ✅ |
| Template assembly risk | No section reads like "insert Path A/B/C boilerplate." Each H2 serves a distinct reader job with its own voice lens and format. | ✅ |

---

## Dwell-Time / CTR Checks

(Aligned with `/article-draft` Phase 2 Hard Writing Requirements 1-2.)

| Check | Assessment | Verdict |
|---|---|---|
| Opener 3-second test — first ~200 words: direct answer + reframe hook + path/framework preview | ✅ All three present. "Yes — and for most homeowners..." (answer), "But here is the buying mistake..." (reframe/loss hook), "Three hardware paths matter..." (framework preview). | PASS |
| Continue-reading hook at every non-final H2 ending | ✅ 7/7 H2 endings hook the next. Mix of loss frames, questions, and quantified teases. Last H2 closes with CTA (no hook needed). | PASS |
| Hype-free | ✅ Verified in Draft Control Metadata. No banned hype words. Field-language stance ("quietly selling you a $3,000-to-$9,000 future surprise") is stance, not hype. | PASS |

---

## Numeric Control Vector Drift

| Control | Intended (Draft Control Metadata) | Execution Diagnosis | Drift? |
|---|---|---|---|
| Imitation / injection / differentiation | 25% / 35% / 40% | ~25% / 30-35% / 40-45%. Differentiation slight overshoot is intentional (retrofit-trap + red-flag translations denser than anchor). Spec-heavy B2B common case. | No — within range |
| Full-sentence bold AI-citation anchors (target: ≥1 per H2) | ≥1 per H2 | 8/8 H2s have at least one full-sentence bold. 26 full-sentence bolds total, 19 short navigation bolds. | ✅ No drift |
| Short navigation bolds (not counted toward AI anchor target) | Separate from full-sentence | Path labels, Rule numbers, list-item leads are all <8 words and used for structure, not citation. | ✅ No drift |
| Opinion intensity (B2B buyer guide stance climax: 7-8 normal; 9-10 sparing; below 4 with high buyer risk = under-controlled) | 7/10 average | H2-04 and H2-06 push to 8; H2-02 holds at 5-6. Average ~7. No section below 4. No section at 9-10. | ✅ No drift |
| Evidence pressure | ~80/100 | Every spec claim traces to T1.1–T1.7. Draft-born cost ranges on watchlist but anchored to industry norms. | ✅ No drift |
| Format rhythm | No consecutive same formats | All 7 consecutive pairs differ. Table→checklist at H2-05/06 is intentional shift. | ✅ No drift |

---

## Flatness Diagnosis

- **Sections that are technically correct but weak:** None identified. All 8 H2s serve distinct reader jobs with concrete output (decision, definition, screening tool, action item).
- **Paragraphs with no tension, judgment, scene, or consequence:** None. Even the qualification section (H2-03) ends with a routing decision that has consequence. Definition section (H2-02) uses conditional framing (weak/real/premium) to create structure.
- **Places where the article stops pulling the reader forward:** None. Continue-reading hooks at all 7 non-final H2 endings ensure forward pull. No dead-end sections.
- **Required rewrite direction:** None.

---

## Stance Intensity vs Hype Check

(Aligned with `voice-and-humanization` Stance vs Hype Boundary)

| Strong claim in draft | Type | Verdict |
|---|---|---|
| "The installer who tells you to add a battery later is doing you a favor only if your inverter is battery-ready. Otherwise, they are quietly selling you a $3,000-to-$9,000 future surprise." | Quantified stance, falsifiable, anchored to retrofit cost scenarios | ✅ Stance, not hype |
| "The cheapest inverter on your quote can quietly close the battery door for the next 10 years." | Named risk, conditional, buyer-facing | ✅ Stance, not hype |
| "Hybrid premium is option pricing, not equipment pricing." | Strong interpretive frame, supported by comparison logic | ✅ Stance, not hype |
| "Most homeowners on the post-NEM 3.0 grid are within five years of possibly wanting a battery." | Opinion, labeled as judgment in metadata | ✅ Acceptable as judgment; not presented as survey data |
| No banned hype words (unleash, revolutionize, skyrocket, ultimate, etc.) | Verified | ✅ Clean |

---

## Voice Consistency

| Voice lens (assigned) | Section | Execution |
|---|---|---|
| Josh Braun (contrarian-but-qualified) | H2-01, H2-04, H2-06 | Present: direct, diagnostic, field-language ("ugliest math," "quietly closes the battery door," "they will not be the one on the truck") |
| Sujan Patel (systematic, executable) | H2-02, H2-05 | Present: definitional precision, comparison table logic, conditional if/then framing |
| Ann Handley + Sujan | H2-03 | Present: warm diagnostic tone, scenario-driven, buyer empathy |
| Joe Sugarman | H2-07, H2-08 | Present: sticky one-liner close ("battery-ready, not battery-required"), memorable question, path-routing CTA |

Voice lenses are consistently applied. No section reads in a voice that contradicts its assigned lens.

---

## Gate Decision

**PASS.**

The draft reads like a human-authored buyer's guide — not a template assembly, not AI-generic, not mechanical. It passes the 3-second opener test, maintains continue-reading hooks at every transition, avoids hype while delivering strong stance, and preserves the benchmark's EnergySage + JingSourcing + 饼干哥哥AGI energy curve.

All Numeric Control Vector dimensions are within range. No flatness, no format monotony, no forced answerability, no template assembly risk.

**Recommendation:** proceed to `/article-enrich`.
