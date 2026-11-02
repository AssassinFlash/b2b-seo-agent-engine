---
name: evidence-policy
description: "Use when: (1) claims, data, or E-E-A-T material is prepared in /article-evidence-opinions, (2) section contracts are built in /article-skeleton, (3) Truth QA verifies claims in /article-truth-qa, (4) any factual statement is about to enter a draft. Governs how evidence enters B2B SEO content — classifies proprietary, industry, and generic sources; assigns priority-based source counts; enforces calculation/unit verification; mandates layman translation; and tracks user overrides."
user-invocable: false

---

# Evidence Policy

## Purpose

Prevent B2B articles from being built on generic, replaceable information. The Mannlee case (16K → 456 traffic after the March 2026 Core Update) showed that factually correct but non-unique content is not worth producing.

This skill upgrades evidence handling to S5-style rigor. It covers source tier classification, priority-based source counts, data-source hierarchy, evidence state labels with error taxonomy, layman translation standards, calculation and unit verification, and user override tracking.

Use this policy whenever a claim, number, technical term, or comparison is prepared for a draft or QA gate.

## When to Use

- `/article-evidence-opinions`: classify every fact by tier, priority, and source count before processing into opinions
- `/article-skeleton`: map Tier 1 / Priority 1 evidence to decision-critical sections
- `/article-truth-qa`: cross-check claims against tiers, units, and calculation logs
- Any time a default, assumption, or number approaches draft text

## A. Source Tier Classification

| Tier | Source Type | Information Gain | Solar / Inverter / Energy Storage Examples |
|---|---|---|---|
| Tier 1 — Proprietary | Factory data, project records, internal test results, team expertise, certifications held, owned case studies, `knowledge/fact-library.json` | High — only this business can provide | "SunRiver's installed hybrid inverters in Kenya maintained 98.2% availability over 18 months across 47 sites, with zero battery-related shutdowns." |
| Tier 2 — Industry | Official standards, regulatory filings, peer-reviewed research, verified trade data, reputable industry reports | Medium — verified but not unique | "IEC 62109-1 defines safety test requirements for PV inverter systems." |
| Tier 3 — Generic | Wikipedia, general web pages, common knowledge, unverified blog posts | Low — zero information gain | "A hybrid inverter can combine solar, battery, and grid power." |

Decision-critical sections must anchor their core claim in Tier 1 evidence. Setup, transition, and pacing sections may use Tier 2–3 context if they introduce no unsupported major claim.

## B. Priority Levels & Source Count Protocol

Assign a Priority level to every claim before it enters a draft.

| Priority | Claim Type | Minimum Source Requirement |
|---|---|---|
| Priority 1 | Decision-critical, safety, compliance, major cost, or risk claims | 2+ independent sources |
| Priority 2 | Technical specifications, market data, performance comparisons | 2+ authoritative sources |
| Priority 3 | Background, definitions, guidance, transitional context | 1+ authoritative source |

Definitions:

- **Independent sources**: sources that do not share the same underlying data, author, manufacturer datasheet, or press release. A manufacturer datasheet and an independent third-party test lab report are independent; two blog posts citing the same press release are not.
- **Authoritative sources**: Tier 1 evidence, official manufacturer documentation, government or standards-body publications, peer-reviewed research, or verified installer/industry reports.

A Priority 1 claim may not rely on a single source, even if that source is Tier 1.

## C. Data Source Hierarchy

When multiple sources are available, prefer sources in this order:

1. Official manufacturer datasheets and installation manuals
2. Official government data and regulatory documents
3. Industry standards (UL, IEC, IEEE, NEC, etc.)
4. Peer-reviewed research and technical reports
5. Verified installer / EPC / industry reports
6. Reputable publisher guides and explainers

A lower-tier source can support background context, but it cannot override a higher-tier source on the same factual point.

## D. Evidence State Labels

Use one primary state label per claim:

| Label | Meaning |
|---|---|
| `verified` | Directly confirmed; safe to use as fact |
| `assumption` | Plausible but unverified; mark clearly, do not present as fact |
| `needs-external` | Requires an outside source before use |
| `blocked` | Must not appear until evidence is provided |

Error taxonomy for QA findings:

| Label | Meaning |
|---|---|
| `incorrect` | Factually wrong against a verified source |
| `false-claim` | Statement presented as fact but unsupported |
| `false-comparative-claim` | Comparison that misrepresents one or both sides |
| `math-error` | Arithmetic or modeling mistake |
| `units-error` | Incorrect or inconsistent units |
| `needs-clarification` | Wording or scope is ambiguous |

## E. Layman Translation Standard

Every technical term or specification entering the draft must pass this 5-step translation:

1. **Technical Term** — the precise engineering term or spec
2. **Layman Definition** — what it means in plain language
3. **Real Impact** — why it matters to the buyer or system
4. **Comparison** — how it stacks against the nearest familiar alternative
5. **Usage Recommendation** — what the reader should actually do with it

Example:

| Step | Entry |
|---|---|
| Technical Term | 6000-cycle LFP battery at 90% DoD |
| Layman Definition | A lithium-iron-phosphate battery that can be deeply discharged daily for roughly 16 years |
| Real Impact | Lower replacement frequency and safer thermal behavior in hot climates |
| Comparison | NMC batteries typically last 4,000–5,000 cycles at similar depth |
| Usage Recommendation | Specify LFP for daily cycling projects where ambient temperatures regularly exceed 35 °C |

Store approved translations in the article's evidence pack. Do not re-simplify them differently in each section.

## F. Calculation & Units Verification

Any number entering the draft must pass three checks:

1. **Arithmetic check** — recalculate the value independently
2. **Unit consistency check** — confirm the unit matches the quantity
3. **Comparison dimension check** — verify apples-to-apples comparison

Common unit traps to flag:

- $/kWh vs $/kW (energy vs power cost)
- kWh vs kW (capacity vs output)
- % vs percentage points
- Peak vs continuous power or current
- AC vs DC ratings
- Nominal vs usable battery capacity

Calculation log format (append to evidence pack):

```markdown
- Claim: [statement]
- Raw inputs: [values + units]
- Arithmetic: [show work]
- Unit check: [pass / fail]
- Comparison dimension: [pass / fail]
- Verdict: [verified / blocked / needs-clarification]
```

## G. User Override Tracking

When a user decides to keep a claim despite source contradiction, record the override in the evidence pack:

```markdown
- Claim: [statement]
- Contradicting source: [source]
- User override rationale: [why operator chose to retain]
- Risk label: `user-override`
```

| Field | Value |
|---|---|
| Flag ID | `OVERRIDE-{YYYYMMDD}-{###}` |
| Original finding | [state label + description] |
| User decision | keep / revise / remove |
| Rationale | why the override is justified |
| Owner | who approved it |

An override does not remove the underlying state label. The claim must still carry a `user-override` tag in the draft so Truth QA can see it.

## H. Forensic Specificity & Linkable Stat-Block Standard (法医级证据与被动外链磁铁标准)

Generic B2B claims ("high precision", "strict QC", "durable coating") carry zero Information Gain because any supplier can type them. Every Tier 1 claim in a decision-critical section must be upgraded to **Forensic Specificity**, and every flagship article should feature at least one **Linkable Stat-Block / Reference Table (Authority Hacker Passive Backlink Magnet)** with a stable `#id` anchor that trade journalists, architects, and industry bloggers can cite:

| Weak Supplier Claim (Forbidden) | Forensic Engineering Proof (Required) |
|---|---|
| "We use high-precision laser cutting and strict QC." | "Cut on a 6kW Trumpf fiber laser to ±0.15 mm kerf tolerance; every 10th panel is checked with a Mitutoyo digital caliper before PVD racking." |
| "Our hybrid inverter switches seamlessly during outages." | "Oscilloscope-verified transfer time of 14 ms under a 6.2 kW inductive load (SAJ HS3 test bench log #2026-04), keeping desktop PSUs and Wi-Fi routers online without rebooting." |
| "316 stainless steel resists corrosion outdoors." | "After 1,000-hour ASTM B117 neutral salt-spray testing, 304 brushed panels showed tea-staining at weld heat-affected zones within 360 hours, whereas 316L molybdenum-bearing panels showed zero pitting." |

## I. Anti-Sell & Disqualification Boundaries (反推销劝退准则)

Nothing builds B2B buyer trust faster than a manufacturer or distributor explaining **when NOT to buy their high-spec product**. Every article evidence pack must document 2–3 concrete disqualification boundaries:
- **Overkill boundary**: when the buyer's environment or duty cycle does not justify the premium grade/model (e.g., "If your partition sits in an HVAC-controlled interior office more than 5 km from the coast, paying the 28–35% premium for 316L stainless over 304 is wasted budget").
- **Incompatible site/system boundary**: when site constraints make the product the wrong engineering choice.
- **Anti-Footprint Fact Rotation**: Before selecting Tier 1 cases/facts for a new article, run `python3 scripts/sync_draft_born_claims.py content-workspace/<project-slug> --recommend` and prioritize verified facts with the lowest `usage_count` so the site never repeats the same case study across every article.
- **Industry Baseline vs. Owned Measurement Boundary (测量与归属边界铁律)**: Competitor research and industry averages may only be cited as external reference baselines — **never** present industry averages or competitor numbers as our own factory/site measurements (`竞品调研和行业平均值只作参照，不得写成我方实测`). Customer-facing downloadable resources must point only to owned media library URLs, never third-party file links.

## J. Anti-Patterns

Do NOT:

- Use a single-source Priority 1 claim
- Skip the units check on any number
- Re-simplify a technical term instead of using the approved 5-step translation
- Present a Tier 3 fact as the primary evidence for a decision-critical section
- Write a paragraph a competitor could reproduce by swapping the brand name
- Label a default assumption as `verified` without operator confirmation
- Fill a section with Tier 2–3 sources and call it "well-researched"
- Fail to record a user override

## Examples

### Example 1 — Tier 1 anchored solar claim

**Input:** "Our hybrid inverter works without a battery."

**Output:** "For the SunRiver Kenya mini-grid, 23 of 47 sites ran the SR-Hybrid-5K in battery-less mode for 14 months. Site logs show 98.2% inverter availability and no battery-related shutdowns, because the unit was sized for direct solar-to-load delivery with grid fallback."

### Example 2 — Correcting a Tier 3 default about LFP thermal stability

**Input:** "LFP batteries are completely fireproof."

**Output:** "LFP chemistry is more thermally stable than NMC, with typical thermal runaway onset above 200 °C vs ~130 °C for NMC. However, no lithium-ion battery is fireproof. Installations must still follow UL 9540 / IEC 62619 spacing, ventilation, and BMS requirements. SunRiver's site data from 12 East African installations recorded zero thermal incidents over 18 months, but that record depends on the specified clearance and temperature-controlled enclosures."

### Example 3 — Catching a kWh vs kW unit trap

**Input:** "This 10 kWh inverter can power a 10 kW load for one hour."

**Output:** "Blocked. A 10 kWh figure describes stored energy, not inverter output power. The SR-Hybrid-5K has a 5 kW continuous AC output and 10 kWh of usable battery storage. At a 5 kW continuous load, the battery pack would last roughly 2 hours at 100% discharge — less after inverter efficiency losses."

### Example 4 — User override on a single-source P1 claim

**Finding:** "Priority 1 safety claim 'single-phase inverter rated for 230 V only' relies on one datasheet. Needs second independent source."

**User override:** "Keep. SunRiver engineering provided the internal compliance test report (TIER-1-2026-047) that independently confirms the rating."

**Record:** Add `OVERRIDE-20260623-001`, attach the report, and tag the draft claim with `user-override`.

## When to Ask for Clarification

- A claim in the outline has no Tier 1 source match in the source library → flag as `needs-external`
- A draft-born claim is useful but unverified → capture for Truth QA, do not silently publish
- A Priority 1 claim cannot reach two independent sources → ask the operator for a second source or record a user override

## When This Skill Should NOT Be Used

- Pure opinion/editorial sections where the primary value is the writer's judgment, not factual anchoring
- FAQ answers that reference publicly available commercial terms already published on the business's own website
