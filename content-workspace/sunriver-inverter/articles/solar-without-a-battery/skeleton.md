# Section Contracts

## Article

- Project: `sunriver-inverter`
- Article slug: `solar-without-a-battery`
- Primary benchmark formula: EnergySage (residential buyer's guide) + 饼干哥哥AGI / woshipm (contrarian rant-with-lessons) + JingSourcing (risk-avoidance listicle)
- Primary keyword: `solar system without battery`
- Reader promise: "You can skip the battery now without regretting it later—if you choose the right inverter path."
- Stage: `/article-skeleton`
- Date: 2026-06-24
- Next skill: `/article-arc`

## Numeric Control Vector Summary

| Control | Chosen value | Justification |
|---|---|---|
| Imitation / injection / differentiation | 35% / 40% / 25% | Benchmark structure is strong (decision ladder, comparison table, red-flag catalog), but the SAJ-specific product routing and supply-partner expertise are the real information gain; voice differentiation keeps it from becoming a generic explainer. |
| AIO capture target | 8 answerable moments | Every H2 is a direct question; SERP is PAA/AIO-heavy. |
| Bold judgment target | 5–6 explicit trade-off calls | Enough to sound like a supply partner, not a chatbot; not so many that evidence can't support them. |
| Opinion intensity | 6/10 | Title is provocative; body stays manufacturer-credible. |
| Evidence pressure | High | Every claim tied to Tier 1/2 evidence; no unsupported generalities. |
| H2 count | 8 | Fits word count and decision-ladder arc. |
| Format repetition tolerance | Max 2 consecutive similar sections | Maintains rhythm variation. |

## Research Evidence

The H2 pool behind this skeleton was built from upstream artifacts, not live extraction. Full evidence is in `intent-research.md`, `content-type-library.md`, and `h2-heading-strategy.md` §Upstream Research Reference and §Raw Candidate Inventory.

| Upstream artifact | Extracted | Evidence |
|---|---|---|
| `intent-research.md` | 17 consolidated candidates + full research execution log | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/intent-research.md` |
| `content-type-library.md` | 8 library entries; 3 selected primary exemplars (LIB-01 EnergySage, LIB-04 JingSourcing, LIB-06 饼干哥哥AGI/woshipm) | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/content-type-library.md` |
| `topic-card.md` Outline Sketch | 8 outline items | Read file §Outline Sketch |
| `benchmark-candidates.md` + `benchmarks/*-extraction.md` | EnergySage H2 chain, JingSourcing debunked-assumption H2s, woshipm tiered headings | Read files |
| `benchmark-success-formula.md` | 9 section jobs | Read file §Structural Blueprint + §2.15 Section Function |
| User-provided 7:3 redesign | 8 final H2s | Operator input, 2026-06-24 |

No upstream gaps. All required artifacts from the upgraded `/article-skeleton` skill were present.

---

## Contracts

### H2-01: Is It a Mistake to Run Solar Panels Without a Battery?

- Section role in reader journey: Arrival / Opening Reframe. The reader lands believing "solar requires a battery" or fearing they are being cheap. This section answers the headline question immediately, reframes battery-less solar as a valid hardware strategy, and sets up the Path A/B/C decision framework.
- Benchmark pattern to imitate: 饼干哥哥AGI contradiction hook (provocative claim → proof in first 150 words) + EnergySage direct-answer opener.
- H2 70% SEO base: Is it a mistake to run solar panels without a battery?
- H2 30% hook element: "Mistake" — loss-aversion framing that challenges the reader's worry.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Josh Braun.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Josh Braun's contrarian-but-qualified sales voice means the section opens with a direct "No" but immediately qualifies it with "if…" The hook word "Mistake" is the fear the reader already has; the section reframes the real mistake as buying the wrong inverter, not skipping the battery.
- Allowed claims:
  - Battery-less solar is viable with the right inverter path.
  - A grid-tied system without a battery shuts down during outages for anti-islanding safety.
  - The real mistake is buying hardware that cannot accept a battery later.
- Evidence role (decision-critical / support / setup / transition): setup + decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T1.2: SAJ H2 can run grid-tied without a battery; behaves like a standard string inverter; no backup power until battery added.
  - T1.7: Sunriver brand stance — not anti-battery, argues for right timing and right hardware path.
  - T3.1: Grid-tied solar systems shut down during outages for anti-islanding safety; a battery is required for backup.
- Unique expertise contribution: Introduces the "battery-ready, not battery-required" reframe and maps the decision to inverter architecture rather than battery brand.
- Borrowed/transmuted benchmark assets: 饼干哥哥AGI contradiction-title structure; EnergySage direct-answer first paragraph; transmuted into Sunriver supply-partner voice.
- Target keywords/entities: `solar without a battery`, `solar panel without battery`, `solar system without battery`, `battery-ready inverter`, grid-tied, anti-islanding.
- E-E-A-T asset: Product-specific proof (SAJ H2 runs without battery) + explicit no-backup caveat + Sunriver supply-partner stance.
- Internal/external link requirements:
  - Internal: `/can-hybrid-inverter-work-without-battery/` (anchor concept: hybrid inverter without battery)
  - External: cite SAJ H2 manual / Sunriver product page for "battery-optional grid-tied" behavior.
- AIO / answerability instruction: Answer in one sentence: "No—if your inverter is battery-ready." Then qualify with backup/no-backup caveat and path preview.
- AIO extractability (direct answer / comparison / checklist / definition / question): direct answer.
- Format type: prose + key-takeaways box.
- Visual/table/checklist/HTML expression instruction: Key-takeaways box (3–5 bullets summarizing Path A/B/C and the no-backup caveat).
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Hero diagram placeholder — Path A/B/C decision fork with icons for R6, H2, HS3; alt text should include "solar without a battery decision paths".
- Forbidden claims or tone risks:
  - Do not claim battery-less solar avoids all permits/codes.
  - Do not say batteries are a scam or installers are dishonest.
  - Do not imply a hybrid inverter without a battery provides backup power.
- Draft acceptance criteria:
  - [ ] Answers the H2 in the first paragraph.
  - [ ] States the no-backup caveat clearly.
  - [ ] Introduces Path A/B/C labels.
  - [ ] Ends with a transition to H2-02 (defining battery-ready).
- Transition signal (how it leads to next section): "If 'battery-ready' is the key phrase, then we should define it before anyone sells it to you."
- Arc node role: Arrival / Opening Reframe.

---

### H2-02: What Does "Battery-Ready" Solar Actually Mean—And Is It Worth It?

- Section role in reader journey: Orientation. The reader now knows battery-less solar can work; this section defines the central term "battery-ready" and shows why it is worth paying attention to.
- Benchmark pattern to imitate: EnergySage "storage-ready" framing + JingSourcing debunked-assumption H2 ("Verified Supplier = badge, not quality assurance" → "battery-ready label ≠ any battery works").
- H2 70% SEO base: What does battery-ready solar mean and is it worth it?
- H2 30% hook element: "Actually" — debunks vague marketing language.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Sujan Patel.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Sujan Patel's clear, systematic, executable voice means the section treats "battery-ready" as a technical operating mode, not a marketing sticker. The "Actually" signals that the term is overused and needs a precise definition.
- Allowed claims:
  - "Battery-ready" means the inverter can accept a battery later without being replaced.
  - SAJ H2 is battery-ready because it has dual 50 A battery ports and supports 180–800 V LiFePO4 batteries.
  - "Battery-ready" is worth the premium only if storage is in the reader's 3–5 year plan.
- Evidence role (decision-critical / support / setup / transition): decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T1.1: SAJ H2 is a DC-coupled hybrid inverter; supports 180–800 V LiFePO4 batteries; dual 50 A battery ports; expandable with compatible SAJ B2 stacks.
  - T1.2: SAJ H2 can run grid-tied without a battery.
- Unique expertise contribution: Defines battery-ready through SAJ H2 spec ports/voltage rather than generic marketing copy; maps the concept to a concrete product behavior.
- Borrowed/transmuted benchmark assets: EnergySage "storage-ready solar panel system" → "battery-ready inverter"; JingSourcing debunked-assumption pattern.
- Target keywords/entities: `battery-ready inverter`, `battery-ready solar`, `hybrid inverter without battery`, `DC-coupled battery expansion`, LiFePO4.
- E-E-A-T asset: Named SAJ product specs with voltage/port thresholds; cites official product pages/manuals.
- Internal/external link requirements:
  - Internal: `/can-hybrid-inverter-work-without-battery/` (definition/support), `/modern-hybrid-solar-systems/` (context/authority)
  - External: SAJ H2 product page / datasheet for battery port and voltage specifications.
- AIO / answerability instruction: Define "battery-ready" in one sentence, then explain the H2 worth-it condition: worth it if you plan to add storage later; not worth it if you never will.
- AIO extractability (direct answer / comparison / checklist / definition / question): definition + comparison.
- Format type: prose + definition callout.
- Visual/table/checklist/HTML expression instruction: Definition callout box with the precise meaning of "battery-ready" and a contrast to "battery-required" and "battery-impossible."
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for a simple diagram showing inverter with pre-wired battery ports vs. inverter without them; alt text: "battery-ready inverter has battery ports built in".
- Forbidden claims or tone risks:
  - Do not imply that "battery-ready" means any battery will work.
  - Do not claim all hybrid inverters are battery-ready.
  - Avoid marketing-speak like "future-proof your home."
- Draft acceptance criteria:
  - [ ] Defines battery-ready in plain English.
  - [ ] Cites SAJ H2 spec ports/voltage.
  - [ ] Gives the conditional "worth it" rule.
  - [ ] Ends with transition to H2-03 (need qualification).
- Transition signal (how it leads to next section): "Knowing what battery-ready means is useless until you know whether you actually need the battery."
- Arc node role: Orientation.

---

### H2-03: How Do You Know If You Actually Need a Solar Battery?

- Section role in reader journey: Qualification. Forces the reader to self-sort into Path A, B, or C before discussing battery timing.
- Benchmark pattern to imitate: EnergySage "Why do you want a battery?" qualification ladder + Sujan Patel/Ann Handley empathetic-systematic framing.
- H2 70% SEO base: How do you know if you need a solar battery?
- H2 30% hook element: "Actually" — cuts through assumption-driven buying.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library + topic-card outline.
- Voice lens: Sujan Patel / Ann Handley.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Sujan Patel provides the structured 3-question qualifier; Ann Handley adds empathy for the homeowner who is being pressured by marketing or family. The "Actually" prompts the reader to ignore the hype and answer three practical questions.
- Allowed claims:
  - You need a battery if: frequent outages, time-of-use arbitrage value, weak net metering/export tariffs, or backup requirement.
  - You probably do not need a battery if: grid is stable, net metering is decent, budget is constrained, and storage is a future maybe.
  - The decision is situational, not universal.
- Evidence role (decision-critical / support / setup / transition): decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T2.3: Battery nearly triples system cost while roughly doubling savings; panels-only payback can be materially shorter.
  - T2.4: Homeowners often regret not getting a battery when export tariffs shrink or self-consumption is low.
  - T3.2: Net metering = retail credit; net billing = lower avoided-cost credit.
- Unique expertise contribution: Translates generic "do you need a battery?" advice into a 3-question flow that routes to Path A/B/C; uses rate-plan context (net metering vs. net billing).
- Borrowed/transmuted benchmark assets: EnergySage now-vs-later if/then logic; Ann Handley empathy for reader confusion.
- Target keywords/entities: `do I need a solar battery`, `solar battery worth it`, net metering, net billing, time-of-use rates, backup power.
- E-E-A-T asset: Uses realistic homeowner scenarios and rate-plan context; attributes trade-offs to market conditions, not opinion.
- Internal/external link requirements:
  - Internal: `/product/hs3-3k-6k-single-phase-all-in-one-energy-storage-system/` (if backup-now path is indicated)
  - External: CPUC NEM 3.0 / local utility context for net billing impact (conditional, with disclaimer).
- AIO / answerability instruction: Provide a 3-question checklist; each "yes" points toward Path B or C, each "no" points toward Path A or B.
- AIO extractability (direct answer / comparison / checklist / definition / question): checklist.
- Format type: prose + 3-question qualifier + path-routing bullets.
- Visual/table/checklist/HTML expression instruction: Decision checklist with three yes/no questions and path-routing outcomes.
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for a flowchart: 3 questions → Path A/B/C; alt text: "solar battery need qualifier flowchart".
- Forbidden claims or tone risks:
  - Do not give one-size-fits-all advice.
  - Do not state installer margin motive as fact.
  - Use conditional language for rate-plan/regulatory claims.
- Draft acceptance criteria:
  - [ ] Presents 3 clear yes/no questions.
  - [ ] Maps answers to Path A/B/C.
  - [ ] Includes the cost/payback caveat.
  - [ ] Ends with transition to H2-04 (retrofit economics).
- Transition signal (how it leads to next section): "Once you know which path you are on, the only remaining question is whether deferring the battery will cost you more later."
- Arc node role: Qualification.

---

### H2-04: Is It Really More Costly to Add a Battery to Solar Later?

- Section role in reader journey: Myth correction. Debunks the common assumption that "I can just add a battery later" without considering inverter swap, labor, compatibility, and installer availability.
- Benchmark pattern to imitate: JingSourcing debunked-assumption H2 + EnergySage retrofit-system-integration section.
- H2 70% SEO base: Is it more costly to add a battery to solar later?
- H2 30% hook element: "Really" / "Costly" — challenges the retrofit assumption with loss-aversion.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Josh Braun + field language.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Josh Braun's diagnostic sales voice calls out the hidden cost without being aggressive. "Really" asks the reader to doubt the easy assumption; "Costly" names the risk. Field language ("retrofit trap," "inverter swap," "AC-coupled patch") makes it sound like someone who has seen the bill.
- Allowed claims:
  - Adding a battery later is often more expensive because of inverter replacement or AC-coupled add-on hardware.
  - Starting with a battery-ready hybrid inverter (H2) avoids the inverter-swap cost.
  - AC-coupled retrofit is possible but adds hardware and commissioning complexity.
  - Original installer availability can affect retrofit feasibility and cost.
- Evidence role (decision-critical / support / setup / transition): decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T1.1: SAJ H2 DC-coupled hybrid inverter supports 180–800 V LiFePO4 batteries and dual 50 A battery ports; expandable with compatible SAJ B2 stacks.
  - T2.5: Retrofitting a battery can be harder than expected: original installer too busy, other installers refuse to touch systems they didn't install.
  - T3.3: AC coupling adds a battery via separate inverter; DC coupling connects battery directly to hybrid inverter.
- Unique expertise contribution: Explains the retrofit trap through inverter architecture (DC-coupled vs. AC-coupled) and installer-availability pain, anchored to SAJ H2's plug-and-play expansion.
- Borrowed/transmuted benchmark assets: EnergySage retrofit complexity section; JingSourcing "hidden cost" debunk pattern.
- Target keywords/entities: `add battery to solar later`, `AC-coupled battery`, `DC-coupled battery`, `retrofit solar battery`, `inverter swap`, `retrofit trap`.
- E-E-A-T asset: Field-language explanation of retrofit economics; cites compatibility and installer-availability constraints.
- Internal/external link requirements:
  - Internal: `/5-solar-battery-specs-to-avoid-solar-rush-mistake/` (red flag expansion)
  - External: industry guides on AC vs. DC coupling; Reddit r/solarenergy owner quotes on installer availability (anonymized).
- AIO / answerability instruction: Direct answer: "It can be, especially if the original inverter is not battery-ready." Then list the cost drivers.
- AIO extractability (direct answer / comparison / checklist / definition / question): direct answer + comparison.
- Format type: prose + scenario + cost-driver bullets.
- Visual/table/checklist/HTML expression instruction: Side-by-side cost-drivers list: "Path A retrofit" vs. "Path B expansion."
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for annotated diagram: string inverter → inverter swap → battery vs. hybrid inverter → plug-and-play battery expansion; alt text: "retrofit trap vs battery-ready expansion diagram".
- Forbidden claims or tone risks:
  - Do not state installer-margin motive as fact.
  - Do not claim every retrofit is prohibitively expensive; use conditional language.
  - Do not bash installers.
- Draft acceptance criteria:
  - [ ] Answers the H2 directly.
  - [ ] Explains inverter swap vs. plug-and-play expansion.
  - [ ] Cites SAJ H2 expansion specs.
  - [ ] Includes installer-availability caveat.
  - [ ] Ends with transition to H2-05 (path comparison).
- Transition signal (how it leads to next section): "The cheapest way to understand this is to lay the three paths side by side."
- Arc node role: Myth correction.

---

### H2-05: Grid-Tied vs. Hybrid Solar: Which Is Best If You Don't Want a Battery?

- Section role in reader journey: Framework confidence. Gives the reader the core decision table comparing the three hardware paths.
- Benchmark pattern to imitate: EnergySage conditional comparison table + This Old House taxonomy-first H2s.
- H2 70% SEO base: Grid-tied vs hybrid solar which is best without battery
- H2 30% hook element: "Which Is Best" — implicit choice tension; reader expects a recommendation.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Sujan Patel.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Sujan Patel's systematic voice delivers a clean comparison table and a conditional recommendation. The H2 promises "which is best," and the section answers with "it depends on your path" rather than a universal winner.
- Allowed claims:
  - Path A (R6 grid-tied): cheapest upfront, no backup, no DC-coupled battery expansion without inverter swap.
  - Path B (H2 hybrid without battery): mid-cost, battery-ready, future expansion via DC-coupled SAJ batteries.
  - Path C (HS3 all-in-one ESS): battery-now, full backup, highest upfront capital.
  - Best choice depends on budget, backup need, and storage timeline.
- Evidence role (decision-critical / support / setup / transition): decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T1.1: SAJ H2 DC-coupled hybrid inverter; supports 180–800 V LiFePO4 batteries; dual 50 A battery ports.
  - T1.2: SAJ H2 can run grid-tied without a battery.
  - T1.3: SAJ R6 pure three-phase on-grid/string inverter; 5–50 kW; up to 98.8% peak efficiency; 110% AC overload; IP65.
  - T1.4: SAJ HS3 6-in-one integrated ESS; 5–40 kWh modular LiFePO4; 5–12 kW; IP65; <10–20 ms UPS.
- Unique expertise contribution: Maps three specific SAJ product families (R6, H2, HS3) to buyer timing and need instead of generic grid-tied vs. hybrid advice.
- Borrowed/transmuted benchmark assets: EnergySage comparison table pattern; This Old House taxonomy structure.
- Target keywords/entities: `grid tied vs hybrid solar`, `solar inverter types`, `string inverter`, `hybrid inverter`, `all-in-one ESS`, `R6 inverter`, `H2 inverter`, `HS3 ESS`.
- E-E-A-T asset: Named product specs (efficiency, kW range, IP rating, battery voltage/port) from official sources.
- Internal/external link requirements:
  - Internal: `/product/r6-15k-25k-three-phase-on-grid-inverter/` (Path A), `/product/h2-3k-6k-single-phase-hybrid-inverter/` (Path B), `/product/hs3-3k-6k-single-phase-all-in-one-energy-storage-system/` (Path C), `/all-in-one-energy-storage-system-comparison/` (Path C detail)
  - External: SAJ official pages / datasheets for R6, H2, HS3.
- AIO / answerability instruction: Comparison table must be extractable as a snippet. Answer "which is best" conditionally in the lead paragraph.
- AIO extractability (direct answer / comparison / checklist / definition / question): comparison.
- Format type: comparison table + prose recommendation.
- Visual/table/checklist/HTML expression instruction: **Three-column comparison table with columns: R6 (Grid-Tied / Path A), H2 (Hybrid / Path B), HS3 (All-in-One ESS / Path C).** Rows: upfront cost, backup today, future battery cost, inverter replacement risk, best for.
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for the mandatory Path A/B/C comparison table; `/article-enrich` to build styled HTML table. Product photos of R6, H2, HS3 can be placed above columns.
- Forbidden claims or tone risks:
  - Do not claim the R6 can accept a DC-coupled battery later without an inverter swap.
  - Do not imply HS3 works without its internal battery.
  - Do not present one path as universally best.
- Draft acceptance criteria:
  - [ ] Comparison table has exactly three columns: R6 (Grid-Tied / Path A), H2 (Hybrid / Path B), HS3 (All-in-One ESS / Path C).
  - [ ] Table includes cost, backup, future battery cost, inverter replacement risk, and best-for rows.
  - [ ] Each path links to its Sunriver product page.
  - [ ] Lead paragraph gives conditional "best" answer.
  - [ ] Ends with transition to H2-06 (quote red flags).
- Transition signal (how it leads to next section): "Knowing the right path is only half the battle; the wrong quote can still lock you out of it."
- Arc node role: Framework confidence.

---

### H2-06: Which Solar Quote Red Flags Can Lock You Out of a Battery Later?

- Section role in reader journey: Defensive competence. Gives the reader quote-screening rules to avoid buying hardware that prevents future battery expansion.
- Benchmark pattern to imitate: JingSourcing red-flag catalog + CXL numbered-mistakes format.
- H2 70% SEO base: Solar quote red flags that prevent adding a battery later
- H2 30% hook element: "Lock You Out" — future-pain framing.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Josh Braun + field language.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Josh Braun's diagnostic voice turns quote screening into a buyer-empowerment exercise. "Lock You Out" is the feared future state; the section gives the reader the exact phrases and specs to watch for.
- Allowed claims:
  - A quote that does not specify battery-port voltage and capacity thresholds is incomplete.
  - A pure on-grid inverter without AC-coupled battery support will require an inverter swap for DC-coupled backup.
  - Some hybrid inverters require a battery to boot; verify "battery-optional" operation on the datasheet.
  - Generic "battery-compatible" claims without named protocols/voltage ranges are red flags.
- Evidence role (decision-critical / support / setup / transition): decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T1.1: SAJ H2 supports 180–800 V LiFePO4 batteries; dual 50 A battery ports.
  - T2.2: Some hybrid models require a battery to boot; buyers should confirm "battery-optional" operation on datasheet.
  - Technical trap #1 from evidence-opinion-pack.md: string-inverter retrofit trap.
  - Technical trap #5 from evidence-opinion-pack.md: incompatible battery risk.
- Unique expertise contribution: Transforms the 6 technical traps from the evidence pack into a quote-screening checklist tied to SAJ H2 specs and real quote language.
- Borrowed/transmuted benchmark assets: JingSourcing red-flag catalog; CXL numbered-mistakes format.
- Target keywords/entities: `solar quote red flags`, `battery-ready inverter checklist`, `hybrid inverter compatibility`, `inverter swap risk`, `solar installer questions`.
- E-E-A-T asset: Practitioner checklist based on verified compatibility constraints; names specific spec thresholds.
- Internal/external link requirements:
  - Internal: `/5-solar-battery-specs-to-avoid-solar-rush-mistake/` (red flag expansion)
  - External: SRNE / Savolture notes on hybrid inverters requiring a battery to boot (for the red-flag caveat).
- AIO / answerability instruction: Provide a numbered checklist; each item has a one-line "why it matters" tied to a verified fact.
- AIO extractability (direct answer / comparison / checklist / definition / question): checklist.
- Format type: checklist + prose explanation.
- Visual/table/checklist/HTML expression instruction: Numbered red-flag checklist with "Why it matters" and "What to ask" columns.
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for a printable/checklist-style block; alt text not applicable (text component).
- Forbidden claims or tone risks:
  - Do not bash installers.
  - Do not claim all installers are dishonest.
  - Do not state installer margin motive as fact.
- Draft acceptance criteria:
  - [ ] Lists at least 5 red flags.
  - [ ] Each red flag has a "why it matters" tied to a verified fact.
  - [ ] Includes the "battery-optional boot" caveat.
  - [ ] Ends with transition to H2-07 (single installer question).
- Transition signal (how it leads to next section): "If you only remember one thing from this checklist, make it the question in the next section."
- Arc node role: Defensive competence.

---

### H2-07: What Is the Number One Question to Ask Your Solar Installer Before Signing?

- Section role in reader journey: Action readiness. Converts the framework into a single, copy-paste action item the reader can use immediately.
- Benchmark pattern to imitate: EnergySage closing installer instruction ("ask your installer to build a storage-ready solar panel system") + Joe Sugarman single-action CTA.
- H2 70% SEO base: What question to ask solar installer before signing
- H2 30% hook element: "Number One" — singular action anchor.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Sujan Patel / Joe Sugarman.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Sujan Patel makes the question systematic and executable; Joe Sugarman makes it memorable. "Number One" tells the reader this is the only question they need to remember from the entire article.
- Allowed claims:
  - The single best question is: "If I add a battery in three years, what changes in this quote?"
  - A good installer can answer with specific inverter model, battery voltage/port thresholds, and labor scope.
  - A vague answer is a signal to pause.
- Evidence role (decision-critical / support / setup / transition): decision-critical.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - Expert stance #5 from evidence-opinion-pack.md: "Before signing, ask: 'If I add a battery in three years, what changes in this quote?'"
  - T1.1: SAJ H2 battery-port and voltage thresholds (what the answer should reference).
- Unique expertise contribution: Gives a single, supplier-vetted question that surfaces inverter replacement risk, compatibility, and future labor in one sentence.
- Borrowed/transmuted benchmark assets: EnergySage "ask your installer" closing; Joe Sugarman one-liner CTA.
- Target keywords/entities: `questions to ask solar installer`, `solar installer checklist`, `before signing solar contract`, `battery-ready solar quote`.
- E-E-A-T asset: Question is derived from field evidence and expert stance; not generic advice.
- Internal/external link requirements:
  - Internal: `/contact/` (conversion), `/faq/` (support)
  - External: none required.
- AIO / answerability instruction: Answer the H2 in the first sentence with the exact question in quotation marks; follow with why it works and what a good answer sounds like.
- AIO extractability (direct answer / comparison / checklist / definition / question): direct answer.
- Format type: prose + copy-paste question block.
- Visual/table/checklist/HTML expression instruction: Copy-paste callout block containing the exact question; secondary box with "Good answer should mention."
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for a styled quote/callout block; `/article-enrich` to render as highlight box.
- Forbidden claims or tone risks:
  - Do not imply Sunriver performs installation labor.
  - Do not make this the only CTA before the framework is complete (it is not—framework is complete by this point).
- Draft acceptance criteria:
  - [ ] States the single question in the first sentence.
  - [ ] Explains why the question surfaces hidden costs.
  - [ ] Describes what a strong answer includes.
  - [ ] Ends with transition to H2-08 (closing reframe).
- Transition signal (how it leads to next section): "That one question protects you because it forces the right inverter choice—which is what this whole article comes down to."
- Arc node role: Action readiness.

---

### H2-08: How Do You Choose an Inverter That Lets You Decide on a Battery Later?

- Section role in reader journey: Reframe / Close. Restates the core lesson, routes the reader to the right product page based on their path, and leaves a memorable phrase.
- Benchmark pattern to imitate: 饼干哥哥AGI lesson-pivot close + EnergySage launchpad conclusion.
- H2 70% SEO base: How to choose an inverter for future battery addition
- H2 30% hook element: "Lets You Decide" — agency/choice framing.
- H2 source (topic-card / intent-research / content-type-library / benchmark / user-input / synthesized): user-input + intent-research + content-type-library.
- Voice lens: Joe Sugarman.
- Voice-lens-to-H2 translation (how the lens shapes the wording): Joe Sugarman's memorable one-liner CTA voice turns the close into a single sticky idea: the inverter should preserve your optionality. "Lets You Decide" makes the reader feel in control rather than sold to.
- Allowed claims:
  - The right inverter is the one that matches your timing, not someone else's sales target.
  - If you never plan storage, R6 is the cost-effective path.
  - If storage is a future maybe, H2 is the battery-ready path.
  - If you need backup now, HS3 is the all-in-one path.
  - Sunriver does not bash batteries; it argues for right timing and right hardware path.
- Evidence role (decision-critical / support / setup / transition): transition + close.
- Required evidence / evidence anchors (reference specific Tier 1 facts from evidence-opinion-pack.md where applicable):
  - T1.3: SAJ R6 specs.
  - T1.1: SAJ H2 battery-ready specs.
  - T1.4: SAJ HS3 integrated ESS specs.
  - T1.7: Sunriver brand stance.
- Unique expertise contribution: Closes with the "battery-ready, not battery-required" reframe and path-specific product routing, reinforcing Sunriver's supply-partner role.
- Borrowed/transmuted benchmark assets: 饼干哥哥AGI lesson pivot; EnergySage launchpad conclusion.
- Target keywords/entities: `choose solar inverter`, `future battery ready inverter`, `battery-ready inverter`, `SAJ inverter`, `solar inverter decision`.
- E-E-A-T asset: Restates proprietary product routing and brand stance; links to official product pages.
- Internal/external link requirements:
  - Internal: `/product/r6-15k-25k-three-phase-on-grid-inverter/` (Path A), `/product/h2-3k-6k-single-phase-hybrid-inverter/` (Path B), `/product/hs3-3k-6k-single-phase-all-in-one-energy-storage-system/` (Path C), `/contact/` (conversion)
  - External: none required.
- AIO / answerability instruction: Answer the H2 with the conditional path rule; end with the core reframe phrase.
- AIO extractability (direct answer / comparison / checklist / definition / question): direct answer + CTA.
- Format type: prose + launchpad links.
- Visual/table/checklist/HTML expression instruction: Launchpad conclusion block with three path-specific buttons/links.
- Visual or HTML expression hint (for `/article-enrich`; do not place image or component here): Placeholder for a launchpad component with three path cards (R6 / H2 / HS3); alt text for any product lineup image: "SAJ inverter path options for solar without a battery".
- Forbidden claims or tone risks:
  - Do not end with generic "solar is the future" inspiration.
  - Do not imply Sunriver installs systems.
  - Do not bash batteries or installers in the close.
- Draft acceptance criteria:
  - [ ] Restates the core reframe in one punchy sentence.
  - [ ] Gives path-specific routing to product pages.
  - [ ] Includes the "battery-ready, not battery-required" phrase.
  - [ ] Ends with a soft CTA to contact/quote.
- Transition signal (how it leads to next section): N/A — final section.
- Arc node role: Reframe / Close.

---

## Rhythm Audit

| Check | Result |
|---|---|
| No two consecutive sections repeat the same format by default habit | ✅ H2-01 prose/takeaways → H2-02 prose/definition → H2-03 prose/qualifier → H2-04 prose/scenario → H2-05 table → H2-06 checklist → H2-07 prose/copy-paste → H2-08 prose/launchpad. |
| Heavy section followed by lighter section | ✅ H2-05 (spec-heavy table) → H2-06 (scannable checklist). H2-04 (economics scenario) → H2-05 (table). |
| Voice lens varies across neighboring sections | ✅ Josh Braun → Sujan Patel → Sujan Patel/Ann Handley → Josh Braun → Sujan Patel → Josh Braun → Sujan Patel/Joe Sugarman → Joe Sugarman. |
| Question ladder traces from arrival to CTA without jumps | ✅ Mistake? → What is battery-ready? → Do I need one? → Is later more costly? → Which path? → What red flags? → What to ask? → How to choose? |
| Each H2 can be answered in 1–2 sentences for AIO | ✅ All eight H2s have explicit one-sentence answers in the AIO / answerability instruction field. |
| Intentional repetition is justified by benchmark rhythm | ✅ "battery-ready," "Path A/B/C," and "retrofit trap" repeat as intentional anchors. |

---

## Secondary Heading Library Appendix

Raw candidates and sources retained for future FAQ expansion or content updates. All sources below were actually extracted, not inferred.

### Research methodology

- **Google PAA**: Live Playwright DOM extraction via `scripts/extract_google_paa.py` (persistent context) for "solar without a battery" and related queries; selector observed: `div[role='button'] / div[jsname]` within the PAA region. See `intent-research.md` §Research Execution Log.
- **Google Autocomplete**: Live extraction from `suggestqueries.google.com` for "solar without a battery" and "hybrid inverter without battery".
- **Reddit / forums**: Live extraction via Tavily `site:reddit.com` search for "solar no battery hybrid inverter".
- **Benchmark H2s**: From `benchmark-candidates.md` and `benchmarks/*-extraction.md`.
- **Topic-card outline**: From `topic-card.md` §Outline Sketch.
- **User input**: The 7:3 redesign provided by the operator.

### Raw candidate inventory

| # | Raw candidate | Source | Final disposition |
|---|---|---|---|
| 1 | Can you use solar panels without a battery? | topic-card outline + Google PAA | Absorbed into H2-01 |
| 2 | Are solar panels without a battery worth it? | **Google PAA** (live) | Absorbed into H2-01 + H2-04 |
| 3 | Can solar panels generate electricity without a battery? | **Google PAA** (live) | Absorbed into H2-02 |
| 4 | Do solar panels work at night without a battery? | **Google PAA** (live) | Absorbed into H2-01 + H2-05 |
| 5 | How do solar panels work if you don't have a battery? | **Google PAA** (live) | Absorbed into H2-02 |
| 6 | Why do so many guides push batteries and what do they leave out? | topic-card outline sketch | Absorbed into H2-01 + H2-02 |
| 7 | When no-battery makes sense | topic-card outline sketch | Absorbed into H2-03 |
| 8 | When battery-now makes sense | topic-card outline sketch | Absorbed into H2-03 + H2-08 |
| 9 | Should I install a solar battery now or add it later? | EnergySage H2 chain | Absorbed into H2-04 |
| 10 | Retrofit system integration / storage-ready solar panel system | EnergySage H2 chain | Absorbed into H2-02 + H2-04 |
| 11 | "Battery-ready" label ≠ any battery works | JingSourcing debunked-assumption | Absorbed into H2-06 |
| 12 | Low quotes that hide inverter swap costs | JingSourcing debunked-assumption | Absorbed into H2-06 |
| 13 | Can I use solar panels without battery storage? | Solar.com / EcoFlow competitor H2 | Absorbed into H2-01 |
| 14 | How does a solar system without a battery work? | Solar.com / EcoFlow competitor H2 | Absorbed into H2-02 |
| 15 | Are solar panels worth it without a battery? | Solar.com / EcoFlow competitor H2 | Absorbed into H2-01 + H2-04 |
| 16 | solar panels without a battery | **Google Autocomplete** | Absorbed into H2-01 |
| 17 | is solar without a battery worth it | **Google Autocomplete** | Absorbed into H2-01 + H2-04 |
| 18 | solar power without a battery | **Google Autocomplete** | Absorbed into H2-01 |
| 19 | solar system without a battery | **Google Autocomplete** | Absorbed into H2-01 + H2-05 |
| 20 | solar without battery inverter | **Google Autocomplete** | Absorbed into H2-02 + H2-05 |
| 21 | solar without battery storage | **Google Autocomplete** | Absorbed into H2-01 |
| 22 | solar without battery backup | **Google Autocomplete** | Absorbed into H2-01 + H2-05 |
| 23 | hybrid inverter without battery | **Google Autocomplete** | Absorbed into H2-05 |
| 24 | solar inverter without battery | **Google Autocomplete** | Absorbed into H2-05 |
| 25 | Hybrid inverter, backup without batteries | **Reddit r/SolarDIY** (live) | Absorbed into H2-05 |
| 26 | Is there a way for cheap solar, without batteries? | **Reddit r/SolarDIY** (live) | Absorbed into H2-04 |
| 27 | Getting a house with Solar, 1:1 credit, but no batteries | **Reddit r/SolarDIY** (live) | Absorbed into H2-03 |
| 28 | Solar without battery/inverter? | **Reddit r/SolarDIY** (live) | Absorbed into H2-02 |
| 29 | No batteries no grid tie with grid backup. Is a hybrid inverter the solution? | **Reddit r/SolarDIY** (live) | Absorbed into H2-05 |
| 30 | New Solar Installation - Hybrid Inverter - Turns Off during Load | **Reddit r/SolarPakistan** (live) | Absorbed into H2-06 |
| 31–38 | The 8 user-provided final H2s | user-input | Final H2-01 through H2-08 |
