# Truth QA — solar-without-a-battery

**Stage:** `/article-truth-qa`  
**Mode:** Light / non-blocking pass  
**Date:** 2026-06-24  
**Status:** PASS  
**Next:** `/article-information-gain-qa`

---

## Scope

This was a **light Truth QA** pass by operator direction. It does **not** repeat the full fact-check already performed upstream in `evidence-opinion-pack.md`. It relies on that pack's Tier 1 / Tier 2 verification and checks only for obvious contradictions, red-line violations, and draft-born claims that are so unsupported they must block the article.

No external web verification was run in this pass.

## Inputs Checked

- `draft.md`
- `evidence-opinion-pack.md`
- `project-profile.md` red lines as referenced by evidence pack
- `Draft Control Metadata` Truth QA Watchlist

---

## Pack-Backed Claim Mapping

| Draft claim family | Evidence anchor | Light QA status |
|---|---|---|
| SAJ H2 can run grid-tied without a battery; no backup until battery added | T1.2 | PASS |
| SAJ H2 is DC-coupled hybrid; 180–800 V LiFePO4; dual 50 A ports | T1.1 | PASS |
| SAJ R6 is grid-tied/string; 5–50 kW; up to 98.8% peak efficiency; IP65 | T1.3 | PASS |
| SAJ HS3 is 6-in-1 ESS; 5–40 kWh; 5–12 kW; IP65; sub-20 ms UPS | T1.4 | PASS |
| Sunriver stance does not bash batteries; argues for right timing / hardware path | T1.7 | PASS |
| Hybrid inverters can often work without battery in grid-tied mode, but some models require battery boot | T2.1 / T2.2 | PASS |
| Battery cost can dominate solar quote and retrofits can be harder than expected | T2.3 / T2.5 | PASS |
| Export tariff / self-consumption regret scenarios | T2.4 | PASS |

No obvious contradictions with the evidence pack were found in this light pass.

---

## Draft-Born Claim Watchlist

These claims were noted in `Draft Control Metadata`. They are **not blocking in this light pass** but should be revisited if later QA gates or editorial review require stricter support.

| Claim | Current treatment | Light QA decision |
|---|---|---|
| `$3,000-to-$9,000 future surprise` / `$4,000–$8,000` AC-coupled retrofit adder / `$5,000–$9,000` inverter swap | Draft-born quantified stance. Plausible as retrofit-cost framing; not independently reverified in this pass. | PASS, non-blocking. Keep for performance-first draft. If strict Truth QA later demands source, soften to "thousands of dollars." |
| "Most installers will not flag..." | Strong stance based on quote-risk framing, not a survey claim. | PASS. Treated as opinion/judgment, not measured fact. |
| "Most homeowners on the post-NEM 3.0 grid are within five years of possibly wanting a battery" | Draft metadata already labels this as opinion, not Tier 1 fact. | PASS. Keep as judgment if phrased as conditional; avoid presenting as survey data. |
| "Hybrid premium is option pricing, not equipment pricing" | Interpretive frame supported by comparison logic. | PASS. Strong stance, not factual overclaim. |

---

## Calculation / Units / Comparative / Safety Findings

### calculation-audit

Light pass only. Detailed independent recalculation was intentionally not performed. No obvious arithmetic contradictions were detected from the draft text.

| Original value / range | Recalculated value | Delta | Status |
|---|---|---|---|
| SAJ R6 5–50 kW, 98.8% peak efficiency | Evidence pack T1.3 | N/A | PASS |
| SAJ H2 180–800 V, dual 50 A ports | Evidence pack T1.1 | N/A | PASS |
| SAJ HS3 5–40 kWh, 5–12 kW, sub-20 ms UPS | Evidence pack T1.4 | N/A | PASS |
| $3,000–$9,000 retrofit framing | Draft-born estimate; not recalculated in light mode | N/A | PASS, watchlist |

### unit-mismatch findings

No obvious kW/kWh, cost-rate/total-cost, or battery/inverter unit mismatch found in the light pass.

### comparative-claim re-validation

No unsupported superlative such as "highest," "fastest," "only," or "first" was found in the publishable body during this light pass. Comparative language is mostly conditional (`cheapest`, `higher`, `more expensive`) and tied to the Path A/B/C comparison logic.

### safety-critical-spec checklist

Safety-adjacent claims are limited to anti-islanding / outage backup behavior, IP65, UPS switching, and inverter/battery specs. In this light pass these are accepted by reference to Tier 1 / Tier 2 evidence anchors rather than reverified externally.

| Claim family | Source count in evidence pack | Status |
|---|---:|---|
| No backup without battery / anti-islanding behavior | T1.2 + T2.1 | PASS |
| H2 battery voltage / ports | T1.1 | PASS (manufacturer/source-library-backed) |
| R6 efficiency / IP65 | T1.3 | PASS (manufacturer/source-library-backed) |
| HS3 UPS / IP65 / storage capacity | T1.4 | PASS (manufacturer/source-library-backed) |

### upstream-revision-follow-up

No `upstream-revision-suggestions.md` item was checked in this light pass. No active blocking upstream revision issue was surfaced by the current draft metadata.

---

## Red Lines

| Red line | Draft behavior | Status |
|---|---|---|
| Do not bash batteries | Draft argues for timing/hardware path; batteries are framed as right for outages, TOU, NEM 3.0, backup needs | PASS |
| Do not present Sunriver as universally best | Draft routes by path (R6 / H2 / HS3) and uses conditional guidance | PASS |
| Avoid unsupported certainty | Strong stance appears, but most is framed as judgment / conditional decision logic | PASS |

---

## Verdict

**PASS — light / non-blocking.**

The draft is consistent enough with the prior evidence pack to proceed to `/article-information-gain-qa`. The strongest draft-born cost ranges remain on the watchlist but do not block under the operator-approved light mode.

If stricter factual review is later required, the first repair target should be the retrofit cost ranges (`$3,000–$9,000`, `$4,000–$8,000`, `$5,000–$9,000`), which can be softened to "thousands of dollars" without changing the article's core performance hook.
