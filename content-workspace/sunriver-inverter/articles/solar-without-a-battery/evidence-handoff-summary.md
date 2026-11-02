# Evidence Handoff Summary — Solar Without a Battery

**Article:** `solar-without-a-battery`  
**Project:** `sunriver-inverter`  
**From stage:** `/article-evidence-opinions`  
**To stages:** `/article-skeleton`, `/article-arc`, `/article-draft`  
**Date:** 2026-06-24  
**Handoff artifact:** `evidence-opinion-pack.md`  
**Supporting artifact:** `knowledge-gap-register.md`  

---

## 1. Executive Summary

The evidence pack for this article is **ready for skeleton construction**. Validation produced 7 Tier-1 proprietary facts, 6 Tier-2 independent facts, 3 Tier-3 background facts, 6 technical traps, and 5 expert stances. Two high-risk flags remain and are explicitly tracked for Truth QA; no upstream corrections were required, so `upstream-revision-suggestions.md` was **not** produced.

| Validation stat | Count |
|---|---|
| Tier 1 facts (Sunriver/SAJ) | 7 |
| Tier 2 facts (independent) | 6 |
| Tier 3 facts (background) | 3 |
| Technical traps identified | 6 |
| Expert stances defined | 5 |
| High-risk knowledge-gap flags | 2 |
| Upstream corrections forced | 0 |

---

## 2. Top 10 Critical Facts Requiring Author Attention

1. **SAJ H2 is a DC-coupled hybrid inverter** that supports 180–800 V LiFePO4 batteries and dual 50 A battery ports — use in Path B / comparison table.
2. **SAJ H2 can run grid-tied without a battery** but provides no backup power until a battery is added — opener and FAQ.
3. **SAJ R6 is a pure three-phase on-grid/string inverter**, 5–50 kW, up to 98.8% peak efficiency, IP65 — Path A / comparison table.
4. **SAJ HS3 is a 6-in-one integrated ESS**, 5–40 kWh modular LiFePO4, 5–12 kW, IP65, <10–20 ms UPS — Path C / comparison table.
5. **Most modern hybrid inverters work without a battery in grid-tied mode**, but some require a battery to boot — safety-critical caveat for checklist.
6. **Battery nearly triples system cost while roughly doubling savings** — use as the economic tension in the trade-off section.
7. **Solar.com now dominates the "solar without a battery" SERP**; EnergySage owns the retrofit query — positioning and differentiation anchor.
8. **NEC 2023 Articles 690/705/706** do not mandate batteries; battery-free systems avoid Article 706 ESS complexity — regulatory freshness anchor.
9. **IRS §25D termination after Dec 31, 2025** is reported by multiple industry sources but still needs IRS/Treasury confirmation — high-risk flag, use disclaimer.
10. **Sunriver brand stance is not anti-battery**; the article must argue for right timing and right hardware path, not "batteries are a scam."

---

## 3. Complexity Warnings per Section

| Section / H2 area | Complexity | Author guidance |
|---|---|---|
| Opener / provocation | Medium | Lead with concrete product behavior, not theory. Use Josh Braun contrarian-but-qualified tone. |
| Path A (R6 string inverter) | Low | Pure on-grid specs are straightforward; stress the retrofit lock-out risk. |
| Path B (H2 hybrid without battery) | Medium-High | Must clarify "battery-optional" operation without overstating backup. Include spec table. |
| Path C (HS3 all-in-one) | High | Avoid implying HS3 works without its internal battery; frame as the storage-now path. |
| Cost / trade-off | Medium | Use conditional language around payback; anchor to net-metering vs. net-billing context. |
| Retrofit trap | Medium | Use buyer-voice quotes; do not state installer-margin motive as fact. |
| Red-flag checklist | Low-Medium | Each checklist item needs a one-line "why it matters" tied to a verified fact. |
| FAQ / AIO blocks | Medium | Answer directly, then immediately qualify with the safety/cost caveat. |

---

## 4. Suggested Analogies (from evidence work)

| Concept | Analogy | Best placement |
|---|---|---|
| Battery-ready hybrid inverter | "Buying a house with pre-run conduit: you don't need the second bathroom now, but the pipes are already in the wall." | Path B introduction |
| String inverter retrofit trap | "Buying a car with a sealed engine bay and then discovering you can't add a tow hitch." | Retrofit trap section |
| Net metering vs. net billing | "Retail store credit vs. thrift-store resale value for your excess power." | Economics section |
| All-in-one ESS | "A generator-in-a-box, not a battery you can peel off later." | Path C caveat |

---

## 5. S6 / Skeleton Writing Recommendations

1. **Anchor the voice in EnergySage's conditional if/then rhythm**, but differentiate with Sunriver's specific product-path specificity (R6 vs. H2 vs. HS3).
2. **Place the comparison table early** — after the opener tension and before the path explanations.
3. **Do not bury the no-backup caveat**; state it in the first 200 words and repeat it in the FAQ.
4. **Use the 6 technical traps as the red-flag section spine**, not as scattered asides.
5. **Assign one expert stance per major H2** to keep opinion density controlled.
6. **Reserve the IRS §25D claim for a clearly disclaimed sidebar or FAQ**, and flag it explicitly for Truth QA.
7. **Keep the internal-link plan intact**; the existing deep articles already map to each path.

---

## 6. Quality Assurance Checklist

- [x] All Tier 1 facts sourced from SAJ official pages or Sunriver materials
- [x] All Tier 2 facts cross-checked against independent sources
- [x] High-risk flags recorded in `knowledge-gap-register.md`
- [x] No upstream corrections required (no `upstream-revision-suggestions.md`)
- [x] Voice lenses and numeric controls documented
- [x] Technical traps and expert stances ready for skeleton embedding
- [x] Internal link targets mapped to existing Sunriver content
- [x] External citation plan aligned with source hierarchy

---

## 7. Deliverables Handed Off

| Artifact | Path | Status |
|---|---|---|
| Evidence & Opinion Pack | `articles/solar-without-a-battery/evidence-opinion-pack.md` | ✅ Complete |
| Knowledge Gap Register | `articles/solar-without-a-battery/knowledge-gap-register.md` | ✅ Complete |
| Evidence Handoff Summary | `articles/solar-without-a-battery/evidence-handoff-summary.md` | ✅ Complete |
| Upstream Revision Suggestions | `articles/solar-without-a-battery/upstream-revision-suggestions.md` | ➖ Not required |

---

**Next skill:** `/article-skeleton`
