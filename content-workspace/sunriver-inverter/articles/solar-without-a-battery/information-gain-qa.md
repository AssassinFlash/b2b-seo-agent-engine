# Information Gain QA — solar-without-a-battery

**Stage:** `/article-information-gain-qa`  
**Date:** 2026-06-24  
**Status:** PASS  
**Next:** `/article-benchmark-qa`

---

## Scope

Gate 2 asks whether the article has a reason to exist beyond generic SERP content. This audit checks the draft against `evidence-opinion-pack.md`, `project-profile.md`, and `truth-qa.md`, then applies the competitor-replaceability test section by section.

No external competitor-search subagent was spawned. The draft's core proprietary angle is clear enough from the existing evidence pack: SAJ-specific R6 / H2 / HS3 path routing + retrofit-trap framing + quote red-flag checklist.

`Draft Control Metadata` was used for control context and excluded from article-section value judgments.

---

## Executive Verdict

**PASS.**

The article is not majority replaceable. A competitor could reproduce the generic premise (“solar can work without a battery”), but they could not reproduce the article's strongest decision logic by merely swapping their brand name:

- **Path A / B / C inverter architecture framework** tied to SAJ R6 / H2 / HS3.
- **Battery-ready, not battery-required** framing tied to SAJ H2's grid-tied-without-battery behavior and battery expansion specs.
- **Retrofit trap** translated into buyer-facing quote risk.
- **Quote red flags** that teach the reader how to detect whether a future battery path is genuinely preserved.
- **Single installer question** that compresses the entire hardware-path decision into one actionable test.

The draft uses generic SERP knowledge as setup, but decision-critical sections contain enough Tier 1 / project-specific evidence and proprietary judgment to pass.

---

## Article-Level Information Gain Diagnosis

| Dimension | Diagnosis | Status |
|---|---|---|
| Proprietary evidence weight | Strong. T1.1–T1.4 SAJ product specs are integrated into the core decision framework, not pasted as decoration. | PASS |
| Decision originality | Strong. The article reframes “battery or no battery” into “which inverter architecture preserves the battery option.” | PASS |
| Replaceability | Mixed by section, but not majority replaceable. Setup sections are replaceable; decision sections are SAJ/path-specific. | PASS |
| Generic SERP risk | Controlled. The article covers expected no-battery basics but quickly moves into product-path and quote-risk logic. | PASS |
| Buyer decision lift | Strong. Reader exits knowing Path A/B/C, what quote red flags to watch, and what question to ask installer. | PASS |

---

## Section-by-Section Replaceability Test

| Section | Core section job | Evidence / proprietary anchor | Replaceability diagnosis | Status |
|---|---|---|---|---|
| H2-01 — Is It a Mistake to Run Solar Panels Without a Battery? | Direct answer + Path A/B/C preview | T1.2 (H2 can run without battery), T1.3 R6, T1.4 HS3, T1.1 H2 | Generic “yes, grid-tied works” is replaceable; Path A/B/C preview tied to SAJ models is not. | PASS |
| H2-02 — What Does “Battery-Ready” Solar Actually Mean? | Define real battery-ready vs weak marketing version | T1.1 H2 dual 50 A ports / 180–800 V LiFePO4; T1.2 grid-tied without battery | Strong information gain. Competitor cannot swap in brand without matching hybrid no-battery operation + battery-port specs. | PASS |
| H2-03 — How Do You Know If You Actually Need a Battery? | Self-qualification via grid/outage/tariff/electrification questions | T2.1 / T2.4 / T3.1; profile buyer pains | Moderately replaceable, but acceptable as setup/qualification. It routes reader into the proprietary Path A/B/C framework. | PASS |
| H2-04 — Is It Really More Costly to Add a Battery Later? | Retrofit-trap economics | T2.5 retrofit difficulty; T1.1 / T1.3 architecture distinction | High reader value. Cost ranges are draft-born and truth-watchlisted, but the retrofit-trap framing is the article's key differentiated judgment. | PASS |
| H2-05 — Grid-Tied vs. Hybrid Solar | Path A/B/C comparison | T1.1 H2, T1.3 R6, T1.4 HS3 | Strong information gain. The table is product-path-specific and not generic solar advice. | PASS |
| H2-06 — Quote Red Flags | Supplier/installer screening checklist | T1.1 battery-port specs, T2.2 battery-optional caution, project voice | Strong. Some red flags are generic, but the line-item translation into inverter-path risk is differentiated and actionable. | PASS |
| H2-07 — Number One Installer Question | Single action item | Derived from T1.1/T1.2/T2.5 and article framework | Strong. The exact question compresses the article's proprietary decision logic into a buyer action. | PASS |
| H2-08 — Choose an Inverter That Lets You Decide Later | Product path routing + CTA | T1.1 / T1.3 / T1.4 | Strong information gain. Clear routing to SAJ R6 / H2 / HS3 makes article non-replaceable by generic competitors. | PASS |

---

## Decision-Section Tier 1 Coverage

| Decision-critical area | Tier 1 coverage | Diagnosis |
|---|---|---|
| Path B / H2 hybrid, battery later | T1.1 + T1.2 | Core recommendation is well anchored. |
| Path A / R6 no-battery low-CapEx path | T1.3 | Product-specific path is anchored. |
| Path C / HS3 all-in-one ESS | T1.4 | Product-specific path is anchored. |
| Brand stance: not anti-battery, right timing/path | T1.7 | Voice and red-line compliance are anchored. |
| Quote red flags / battery-port specificity | T1.1 + T2.2 | Enough support for screening logic. |
| Retrofit trap economics | T2.5 + draft-born estimate | The concept is supported; exact cost ranges remain Truth QA watchlist but do not block Info Gain. |

No decision-critical section is Tier 3-only.

---

## Competitor-Replaceability Summary

### Replaceable / generic layers

These claims are broadly available in the SERP and do not create information gain by themselves:

- Solar can run without a battery in a grid-tied setup.
- No battery means no backup during an outage.
- Batteries are expensive.
- Time-of-use / net billing can change the battery economics.
- AC-coupled retrofit can be more complex than adding storage upfront.

### Non-replaceable / value-creating layers

These are the article's information-gain core:

1. **The question is not battery vs no battery; it is inverter architecture.** This reframes the whole query.
2. **SAJ H2 becomes the “wait and see” Path B** — grid-tied today, battery-ready later.
3. **R6 / H2 / HS3 product routing** translates a generic solar question into a hardware decision.
4. **Quote red flags** convert knowledge into buyer defense.
5. **The installer question** gives a one-sentence test a reader can use before signing.
6. **Battery-ready, not battery-required** is a repeatable, memorable thesis competitors would need to actually support with product architecture.

---

## Specificity Test

| Specificity type | Present? | Evidence |
|---|---:|---|
| Named products | Yes | SAJ R6 / H2 / HS3 appear throughout. |
| Specs | Yes | H2 180–800 V LiFePO4, dual 50 A; R6 5–50 kW / 98.8%; HS3 5–40 kWh / sub-20 ms UPS. |
| Decision framework | Yes | Path A / B / C repeated across opener, table, conclusion. |
| Quote/process proof | Yes | Red-flag checklist + installer question. |
| Case-study proof | No | Not required for this article; not presented as owned cases. |
| Verified certifications | Limited | IP65 and product specs present; no certification-heavy argument made. |

Specificity is sufficient for the article type.

---

## Information Gain Risks / Watch Items

These are not blockers, but they should be watched in later gates:

| Risk | Why it matters | Recommendation |
|---|---|---|
| H2-03 self-qualification is mostly generic | Grid/outage/tariff/electrification questions are common buyer-guide logic | Accept as setup because it routes into proprietary Path A/B/C. Do not over-expand this section. |
| H2-04 cost ranges are draft-born | They create differentiation but need support if challenged | Keep for performance-first draft; if later strict review demands, soften ranges while preserving retrofit-trap stance. |
| Article may read product-forward in H2-08 | Product routing is valuable but can look commercial | Benchmark QA / Reader QA should ensure CTA feels earned and not like a hard sell. |
| Off-grid intent is only disambiguated, not deeply covered | Some “solar without battery” searchers mean off-grid | Accept current scope; if Reader QA flags confusion, add FAQ later rather than changing core structure. |

---

## Gate Decision

**PASS.**

The article provides meaningful information gain over generic SERP content because the central value is not the factual statement “solar works without a battery,” but the decision architecture:

> **Battery-free solar is safe only if the inverter path preserves the future battery option.**

That claim is supported by Tier 1 product evidence and is executed through the Path A/B/C framework, quote red flags, and installer question. The article should proceed to `/article-benchmark-qa`.
