# Regulatory Verification — `solar-without-a-battery`

> Project: Sunriver Electric  
> Article: Solar Without a Battery  
> Task: Verify scope and plain-language meaning of standards/regulations for solar + battery storage  
> Prepared: 2026-06-23  
> Status: Intermediate research file — NOT the final evidence-opinion pack.

---

## 1. NEC 2023 (NFPA 70) — Solar & Energy Storage System Requirements

### What it actually covers
- **Article 690** governs solar photovoltaic (PV) systems: array wiring, disconnecting means, grounding, rapid shutdown (690.12), arc-fault protection, and overcurrent protection.
- **Article 706** governs Energy Storage Systems (ESS) greater than 1 kWh capacity, whether stand-alone or interactive with other power sources. It covers disconnecting means, overcurrent protection, safety labeling, ventilation/gas diffusion, working space, and emergency shutdown for dwellings.
- **Article 705** governs interconnection of electric power production sources with the utility grid.
- Listed/reference standards commonly invoked: UL 9540 (ESS), UL 1973 (stationary batteries), UL 1741 SA (smart inverters), NFPA 855 (installation of stationary ESS), IEEE 1547.
- **2023 NEC restructure note:** The 2023 edition began reorganizing Chapter 7; the 2029 edition is expected to complete the restructuring of power-production and ESS articles.

### What it does NOT cover
- NEC does **not** mandate that a solar system must include a battery.
- NEC does **not** set product pricing, financing, or tax rules.
- NEC does **not** grant interconnection approval or net metering rights; those come from the utility/AHJ.
- NEC is an electrical/installation code, not a fire/building/structural code (those are IFC, IBC, IRC, NFPA 855, local amendments).

### Plain-language implication for a homeowner considering solar without a battery
A grid-tied solar-only system still must meet NEC Article 690 (PV wiring, rapid shutdown, grounding, labeling) and Article 705 (utility interconnection), but it **completely avoids Article 706** and the extra documentation, disconnects, ventilation, and ESS labels that come with batteries. Skipping the battery means a simpler permit package and fewer inspection points.

### Date / region limitations
- **Edition:** NFPA 70-2023 is current as of this research. Some jurisdictions still enforce 2020 or 2017 NEC, while others are moving toward 2026.
- **Region:** United States and territories that adopt NEC. Adoption is state/county/city-specific; local amendments may add battery fire-setback, ventilation, or installation requirements beyond NEC.

### Confidence level
**High.** Based on NFPA NEC scope statements, SEIA code guides, and multiple NEC interpretation resources.

### Sources
- NFPA 70 (NEC) Article 706 scope statements in code-making panel drafts (706.1 applies to ESS > 1 kWh).
- SEIA, "U.S. Codes & Standards for Energy Storage Systems" (2016) and subsequent NEC interpretation guides.
- EPRI, "Evolution of Battery Energy Storage Safety Codes and Standards" (Article 706 > 1 kWh threshold).
- Solar Permit Solutions, "NEC 690 and 706 Compliance Checklist" (Dec 2025).

---

## 2. IRS Form 5695 / Residential Clean Energy Credit (IRC §25D)

### What it actually covers
- IRS Form 5695 is the form used to claim the **Residential Clean Energy Credit** under Internal Revenue Code §25D.
- Historically (post-IRA 2022) the credit covered 30% of the installed cost of eligible clean-energy property placed in service by the homeowner, including:
  - Solar PV panels
  - Solar water heaters
  - Wind turbines
  - Geothermal heat pumps
  - Fuel cells
  - **Battery storage technology** (minimum 3 kWh capacity)
- A key IRA change (effective 2023–2025) was that **standalone batteries** qualified even if not paired with solar.

### What it does NOT cover
- The credit is **not a rebate or refund**: it is a non-refundable credit against federal income tax liability; unused amounts may be carried forward.
- It does **not** cover leased or PPA systems (the owner-lessor claims the commercial credit, not the homeowner).
- It does **not** apply to portable power stations or small batteries below 3 kWh.
- **Critical 2026 limitation:** Multiple authoritative sources report that the One Big Beautiful Bill Act (OBBBA), signed July 2025, terminated the §25D Residential Clean Energy Credit for expenditures made after **December 31, 2025**.

### Plain-language implication for a homeowner considering solar without a battery
For a system placed in service in 2026, the federal 30% tax credit for battery storage appears to be **unavailable** under current law. That changes the math for "battery now vs. battery later":
- A homeowner who installs solar-only today and adds a battery in 2026 or later would likely **not** get the 30% federal credit on that later battery purchase.
- This strengthens the case for buying a **battery-ready hybrid inverter** (e.g., SAJ H2) now and deferring the battery decision, but it removes one financial cushion that previously made future batteries cheaper.
- **Required disclaimer:** Tax law can change; homeowners must confirm current status with a qualified tax professional before making a financial decision.

### Date / region limitations
- **Date:** As of this research (June 2026), the §25D credit is reported to have expired for property placed in service after **December 31, 2025**. The IRA's earlier schedule (30% through 2032, step-down to 26%/22%, then expire) was superseded by OBBBA.
- **Region:** United States federal tax law.
- **Note:** 2025 installations may still be claimed on 2025 tax returns filed in 2026, and any unused 2025 credit can still be carried forward.

### Confidence level
**Medium-High for the expiration date; Medium for precise interpretation.** The OBBBA termination is reported consistently by the National Law Review, NAHB, and several industry analysts, but IRS/Treasury may issue further guidance. The article must use cautious phrasing and direct readers to a tax professional.

### Sources
- National Law Review, "One Big Beautiful Bill: Effect on Energy Credits" (July 11, 2025): §25D expires Dec 31, 2025.
- NAHB, "What to Know About Expiring Energy Tax Credits" (July 10, 2025).
- Instead.com, "Residential solar credits expire in 2025 — act now" (FAQ on §25D termination).
- Photons & Electrons, "Section 25D Battery Storage Credit Is Gone for New Installs" (May 2026).
- Palmetto/Ohio and Columbus local pages (2026) — note the same uncertainty for 2026+ installations.

---

## 3. EU Battery Regulation (EU) 2023/1542

### What it actually covers
- A directly applicable EU Regulation that replaces the previous Batteries Directive 2006/66/EC.
- Applies to **all batteries placed on the EU market or put into service**, including:
  - Portable batteries
  - SLI (starter/lighting/ignition) batteries
  - LMT (light means of transport) batteries
  - EV batteries
  - Industrial batteries, **including stationary battery energy storage systems (BESS)**
- Sets lifecycle requirements:
  - Restrictions on hazardous substances (mercury, cadmium, lead)
  - Carbon footprint declarations and performance classes (for certain categories)
  - Recycled-content targets (phased, from 2031 onward)
  - Performance and durability requirements
  - **Safety requirements for stationary battery energy storage systems**
  - Labelling, marking, QR codes, and battery passport (phased)
  - Due diligence for raw-material sourcing
  - Extended Producer Responsibility (EPR) for collection and recycling

### What it does NOT cover
- Batteries specifically designed for **military, space, or nuclear-safety** equipment are excluded.
- The regulation does **not** require every home solar system to include a battery.
- It does **not** set installation labor rules, pricing, or homeowner tax incentives (those are national Member State policies).
- Not all requirements apply immediately or to all battery categories; many obligations are phased.

### Plain-language implication for a homeowner considering solar without a battery
For a homeowner in the EU, the Battery Regulation is mostly invisible at the purchase stage, but it matters for product quality and future-proofing:
- A battery bought later must meet EU safety, labelling, and (eventually) carbon-footprint/recycled-content rules.
- A **battery-ready hybrid inverter** today lets the homeowner add a compliant battery later without replacing the core inverter.
- Skipping the battery now avoids any immediate battery-specific compliance or end-of-life obligations.

### Date / region limitations
- **Entry into force:** 17 August 2023.
- **General application:** 18 February 2024 (core provisions).
- **CE marking mandatory:** 18 August 2024.
- **Batteries Directive 2006/66/EC fully repealed:** 18 August 2025.
- **Battery passport obligation:** 18 February 2027 for EV, LMT, and industrial batteries > 2 kWh.
- **Region:** EU Member States (directly applicable).

### Confidence level
**High.** Based on EUR-Lex official summary, ECHA legislation profile, and Battery Compliance Guide analysis.

### Sources
- EUR-Lex summary of Regulation (EU) 2023/1542 (last update August 2025).
- ECHA legislation profile for EU Batteries Regulation (scope and substances).
- Battery Compliance Guide, "EU Battery Regulation (EU) 2023/1542 Overview" (battery categories, phased timeline).
- Instrux, "Key Differences between Battery Directive 2006/66/EC and Regulation EU 2023/1542 for Stationary Battery Energy Storage Systems" (Dec 2024).

---

## 4. Net Metering / Net Billing Rules (U.S., with California NEM 3.0 as the leading example)

### What it actually covers
- Net metering/net billing policies determine how a homeowner is compensated for electricity exported to the grid.
- **California NEM 3.0 / Net Billing Tariff (CPUC Decision 22-12-056), effective April 15, 2023:**
  - Replaced retail-rate credits with hourly Avoided Cost Calculator (ACC) values for exported energy.
  - Requires customers to be on Time-of-Use (TOU) rates.
  - Grandfathers NEM 1.0/2.0 customers for 20 years from their Permission to Operate (PTO) date.
  - Existing NEM 2.0 customers can generally add battery storage without losing grandfathered status.
  - Designed to incentivize solar + battery storage by making self-consumption and strategic export more valuable than pure solar export.

### What it does NOT cover
- Net metering rules do **not** require a battery.
- They do **not** guarantee the same compensation nationwide; rules vary by state, utility, and sometimes by municipality.
- NEM 3.0 does **not** apply outside the three California investor-owned utilities (PG&E, SCE, SDG&E) unless another jurisdiction voluntarily adopts similar rules.

### Plain-language implication for a homeowner considering solar without a battery
Under NEM 3.0-style rules, a solar-only system still works, but the economics shift:
- Exported solar is compensated at a much lower rate (roughly $0.05–$0.08/kWh vs. retail ~$0.30/kWh under NEM 2.0), so "oversizing and exporting" is less profitable.
- A battery lets the homeowner store midday solar and use or export it during peak-value evening hours.
- **Key takeaway for the article:** A battery is not mandatory, but under modern net-billing tariffs the payback period for solar-only is longer; a battery-ready hybrid inverter preserves the option to add storage later without a full system redesign.

### Date / region limitations
- **California NEM 3.0:** Effective April 15, 2023 for PG&E, SCE, SDG&E.
- **Grandfathering:** NEM 1.0/2.0 customers keep their tariff for 20 years from PTO.
- **Region:** Primarily California IOU territory as the flagship example; other U.S. states have their own net metering or net billing rules.

### Confidence level
**High for the California NEM 3.0 structure; Medium when generalizing to other states.** The CPUC decision and utility implementation details are well documented, but homeowners must check their local utility's tariff.

### Sources
- CPUC Decision 22-12-056 (Dec 2022) and NEM 3.0 fact sheet.
- GreenLancer, "NEM 3.0 California: Net Metering 3.0 Rates, Rules & Deadlines" (Jan 2026).
- Clean Power Alliance agenda packet (July 2023) summarizing NBT/ACC structure.
- Enphase, "Understanding NEM 3.0 and the future of net energy metering" (March 2023).

---

## 5. AHJ (Authority Having Jurisdiction) Solar & Battery Interconnection Requirements

### What it actually covers
- The AHJ is the local body (building department, fire marshal, electrical inspector) that enforces codes and issues permits.
- For solar + battery projects, AHJs typically require:
  - Site plan and electrical single-line diagram
  - Structural load calculations
  - Equipment spec sheets and certifications (UL 9540, UL 1973, UL 1741 SA)
  - Labeling and rapid-shutdown compliance (NEC 690.12)
  - ESS-specific labels, disconnects, and emergency shutdown procedures (NEC 706)
  - Utility interconnection agreement
  - Final inspection before Permission to Operate (PTO)
- Many AHJs also reference fire codes (IFC Section 1206, NFPA 855) for battery siting, separation distances, ventilation, and firefighter access.

### What it does NOT cover
- AHJ requirements do **not** override the NEC; they supplement it with local amendments.
- AHJs do **not** set federal tax credits or state rebate rules.
- AHJs do **not** require batteries; they only regulate batteries if the homeowner chooses to install one.
- Requirements are **not uniform**: there are over 36,000 AHJs in the U.S., each with its own forms, fees, review timelines, and interpretations.

### Plain-language implication for a homeowner considering solar without a battery
A solar-only system still needs AHJ permits and inspection, but the package is simpler and usually faster because it skips ESS-specific documentation, battery safety data sheets, fire-setback reviews, and extra disconnect/signage requirements. For homeowners on the fence, starting solar-only with a **battery-ready hybrid inverter** defers the heavier AHJ battery review until later.

### Date / region limitations
- **Region:** United States, local jurisdiction-specific.
- **Date:** AHJs adopt NEC editions on different schedules; some still use 2017/2020 NEC, others use 2023 or 2026.

### Confidence level
**High.** Based on industry permitting guides and AHJ workflow documentation.

### Sources
- Solar Permit Solutions, "AHJ Solar Permitting: Complete Guide" (Feb 2026).
- Exactus Energy, "AHJ Solar: Navigating Local Requirements" (April 2024).
- GreenLancer, "6 Tips For AHJ Solar Permitting Success" (Feb 2026).
- NYSERDA, "Energy Storage System Permitting and Interconnection Process Guide for New York City Lithium-Ion Outdoor Systems."

---

## Cross-Cutting Summary for the Article

| Topic | Covers | Does NOT Cover | Homeowner implication for solar-without-battery |
|-------|--------|----------------|------------------------------------------------|
| NEC 2023 | PV wiring, rapid shutdown, ESS safety/disconnects | Mandating batteries; pricing; utility approval | Avoids Article 706 complexity; still needs PV permit |
| IRS Form 5695 / §25D | 30% credit for eligible clean-energy property (historically incl. ≥3 kWh batteries) | Rebate/refund; leased systems | Federal battery credit appears expired for 2026+ installs; verify with tax pro |
| EU Battery Regulation 2023/1542 | Battery design, safety, labelling, recycling, passport (EU market) | Mandating batteries; installation labor rules | Future batteries must meet EU rules; battery-ready inverter defers compliance |
| Net Metering / NEM 3.0 | Compensation for exported solar; TOU rates; battery incentives via rate design | Requiring batteries; nationwide uniformity | Solar-only still allowed, but export value is lower; storage improves economics |
| AHJ requirements | Local permits, inspections, fire/electrical safety for installed systems | Tax credits; federal rules | Battery-free permits are simpler; battery adds ESS/fire review |

---

## Red Lines / Cautions for Drafting

1. **Tax claims:** Never state "you will get the 30% credit." Use "as of 2026, the federal Residential Clean Energy Credit has been reported to expire after 2025 — confirm with a tax professional."
2. **NEC claims:** Do not say "no permit needed without a battery." Say "permits are still required, but the scope is narrower."
3. **Regional claims:** Always anchor NEM 3.0 to California IOU territory; other regions have different rules.
4. **EU claims:** Clarify that EU 2023/1542 governs products placed on the EU market, not homeowner installation choices.
5. **AHJ claims:** Emphasize local variation — "check with your local Authority Having Jurisdiction."

---

## Sources Consulted

- NFPA 70 (NEC) code documents and code-making panel drafts (Article 706, 690, 705).
- SEIA Codes & Standards Working Group materials.
- EPRI battery storage safety codes report.
- Solar Permit Solutions NEC 690/706 checklist and AHJ permitting guide.
- National Law Review, NAHB, and industry analyses of the One Big Beautiful Bill Act (2025).
- IRS Form 5695 historical instructions (pre-2025).
- EUR-Lex and ECHA summaries of Regulation (EU) 2023/1542.
- Battery Compliance Guide and Instrux analysis of EU Battery Regulation for BESS.
- CPUC Decision 22-12-056 and NEM 3.0/Net Billing Tariff fact sheets.
- GreenLancer, Enphase, Clean Power Alliance, and other NEM 3.0 explainers.
- NYSERDA NYC ESS permitting guide.
