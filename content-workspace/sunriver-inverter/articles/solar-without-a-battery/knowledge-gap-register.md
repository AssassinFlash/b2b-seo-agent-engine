# Knowledge Gap Register — Solar Without a Battery

**Article:** `solar-without-a-battery`  
**Project:** `sunriver-inverter`  
**Created at:** `/article-evidence-opinions`  
**Last updated:** 2026-06-24

Pre-writing risk inventory of claims, specs, and assertions that need verification before drafting or during Truth QA.

---

## Technical Specifications

| Claim / Spec | Current Status | Source Needed | Owner | Risk | Resolved In |
|---|---|---|---|---|---|
| SAJ H2 can operate grid-tied without a battery | `verified` | SAJ H2 user manual working modes; Sunriver `/can-hybrid-inverter-work-without-battery/` | evidence-opinions | medium | research/technical-verification.md |
| SAJ H2 supports DC-coupled battery expansion 180–800 V LiFePO4 | `verified` | SAJ official H2 product page / datasheet; Sunriver H2 product page | evidence-opinions | low | research/technical-verification.md |
| SAJ R6 is pure on-grid/string inverter, 5–50 kW, up to 98.8% efficiency | `verified` | SAJ official R6 page / datasheet | evidence-opinions | low | research/technical-verification.md |
| SAJ HS3 is 6-in-one integrated ESS, 5–40 kWh modular, 5–12 kW output | `verified` | SAJ official HS3 page / datasheet; Sunriver HS3 product page | evidence-opinions | low | research/technical-verification.md |
| Hybrid inverters generally work without battery in grid-tied mode | `verified` | Multiple independent sources (Eneronix, SRNE, Enertech, Solar.com) | evidence-opinions | low | research/technical-verification.md |
| Some hybrid inverters require a battery to boot | `verified` | SRNE, Savolture warnings | evidence-opinions | medium | research/technical-verification.md |

## Terms & Concepts Needing Definition

| Term / Concept | Definition Draft | Verification Needed | Owner | Risk | Resolved In |
|---|---|---|---|---|---|
| Battery-ready / battery-capable inverter | Hybrid inverter that can run grid-tied now and accept a battery later via DC coupling | confirmed by usage across sources | evidence-opinions | low | research/technical-verification.md |
| Anti-islanding | Grid-tied inverter shuts down during outage to protect line workers; no backup without battery | confirmed across sources | evidence-opinions | low | research/technical-verification.md |
| Net metering vs net billing | Net metering = retail credit; net billing = lower avoided-cost credit | confirmed by SERP/Briggs & Stratton/Sun Valley Solar | evidence-opinions | medium | research/serp-refresh.md |
| AC coupling vs DC coupling | AC = battery added via separate inverter; DC = battery connected directly to hybrid inverter | confirmed by EnergySage/Aurora Solar | evidence-opinions | medium | research/serp-refresh.md |

## Competitive / Market Claims

| Claim | Current Status | Source Needed | Owner | Risk | Resolved In |
|---|---|---|---|---|---|
| "Installers push batteries because of margin/incentive misalignment" | `assumption` | No primary source; must be framed as buyer concern, not fact | evidence-opinions / truth-qa | high | buyer-voice research |
| "Battery nearly triples system cost while roughly doubling savings" | `verified` | German balcony-solar owner math (r/solarenergy) | evidence-opinions | medium | research/buyer-voice.md |
| "Solar-only payback can be materially shorter with good net metering" | `verified` | Multiple buyer-voice sources + Solar.com | evidence-opinions | medium | research/buyer-voice.md |
| Solar.com now dominates the "no battery" SERP | `verified` | SERP refresh top 5 | evidence-opinions | low | research/serp-refresh.md |
| EnergySage still owns "can I add battery to solar later" | `verified` | SERP refresh top 5 | evidence-opinions | low | research/serp-refresh.md |

## Regulatory / Incentive Claims

| Claim | Current Status | Source Needed | Owner | Risk | Resolved In |
|---|---|---|---|---|---|
| NEC does not mandate batteries for solar systems | `verified` | NFPA 70 scope; Article 706 applies only to ESS > 1 kWh | evidence-opinions | low | research/regulatory-verification.md |
| IRS §25D Residential Clean Energy Credit expired after Dec 31, 2025 | `needs-external` | Multiple industry sources report OBBBA termination; IRS/Treasury guidance preferred | truth-qa | high | research/regulatory-verification.md |
| EU Battery Regulation does not require homeowners to install batteries | `verified` | EUR-Lex summary / ECHA scope | evidence-opinions | low | research/regulatory-verification.md |
| California NEM 3.0 reduces export compensation, making solar-only less attractive | `verified` | CPUC Decision 22-12-056; Enphase/GreenLancer | evidence-opinions | medium | research/regulatory-verification.md |
| AHJ requirements do not require batteries | `verified` | NEC + local jurisdiction pattern | evidence-opinions | low | research/regulatory-verification.md |

---

**Status key:**
- `verified` — confirmed by a source
- `assumption` — transparently labeled in draft
- `needs-external` — must be verified before publish
- `blocked` — cannot be verified; must be removed or weakened

**Risk key:**
- `low` — minor inaccuracy, easy to fix
- `medium` — could mislead a buyer decision
- `high` — safety, warranty, compliance, or major cost implication
