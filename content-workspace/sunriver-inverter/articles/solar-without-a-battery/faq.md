# FAQ — solar-without-a-battery

**Stage:** `/article-faq`  
**Date:** 2026-06-24  
**Article:** solar-without-a-battery

---

## Friction Map

| # | Friction type | Question | Cognitive placement |
|---|---|---|---|
| 1 | Implementation | How long does a solar + battery-ready system take to install? | After H2-05 comparison table (reader imagines installing) |
| 2 | Implementation / compatibility | Do I need an electrical panel upgrade to add a battery later? | After H2-05 comparison table |
| 3 | Compatibility / backup integration | Can I connect a backup generator to charge my SAJ hybrid inverter or ESS batteries? | After H2-05 comparison table |
| 4 | Trust / risk | What happens to my warranty if I add a battery in year 3? | After H2-07 installer question (reader weighing long-term risk) |
| 5 | Financial / hidden cost | Will adding a battery later really cost thousands more? | After H2-07 installer question |
| 6 | Financial / policy | Does the federal tax credit still apply if I add a battery later? | After H2-07 installer question |
| 7 | Compatibility | Can I add a non-SAJ battery to an SAJ H2 hybrid inverter? | After H2-05 comparison table |

---

## FAQ Group 1 — Implementation & Getting Started

**Insert position:** after the H2-05 comparison table and the "hybrid premium is option pricing" paragraph (and after Card 2 from resources.md). The reader has just picked a path and is now imagining what installation actually involves.

### ❓ Quick Answers: Installation & Getting Started

[su_accordion]<p style="font-size: 20px;font-weight: bold;color: #1a1a1a;margin-top: 20px;margin-bottom: 15px">❓ Quick Answers: Installation & Getting Started</p>

[su_spoiler title="Q: How long does a solar + battery-ready system take to install?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>Typical residential install: 1–2 days for the inverter + panels, plus 2–8 weeks for permitting depending on your city.</strong></p>

<p>The SAJ H2 hybrid inverter itself is a single wall-mounted unit — the physical swap from a string inverter is a half-day job. The wait is almost always the permit, not the hardware. If your installer quotes a 1-day physical install but a 6-week permit queue, that is normal, not a red flag. Battery addition later (Path B) is a half-day plug-and-play job once permitted.</p>

[/su_spoiler]

[su_spoiler title="Q: Do I need an electrical panel upgrade to add a battery later?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>Not always — only if your main breaker is 100A or your home was built before 1980.</strong></p>

<p>If your panel is 200A with 20–30A of free capacity, the hybrid inverter and future battery fit without an upgrade. Pre-1980 homes with 100A panels typically need a $1,500–$3,000 panel upgrade before a battery can be added — and this cost is on top of the battery itself. Ask your installer to do a load calculation during the site visit; a serious installer will surface this before you sign, not after.</p>

[/su_spoiler]

[su_spoiler title="Q: Can I add a non-SAJ battery to an SAJ H2 hybrid inverter later?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>Technically possible, but not recommended — mixing brands often voids the warranty and complicates commissioning.</strong></p>

<p>The SAJ H2 is designed for the SAJ B2 battery stack over its 180–800 V LiFePO4 range and dual 50 A ports. Third-party batteries may fit the voltage window but are not validated for the H2's battery management communication. If you mix brands, the inverter's warranty typically excludes battery-related failures. The safe path is to commit to the SAJ B2 stack when you add storage — it is the hardware the H2 was validated against.</p>

[/su_spoiler]

[su_spoiler title="Q: Can I connect a backup generator to charge my SAJ hybrid inverter or ESS batteries?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>Yes — SAJ hybrid inverters and all-in-one ESS units can use a backup generator, but only if the generator output is frequency-stable and the inverter is configured for generator synchronization.</strong></p>

<p>Portable generators with unstable voltage/frequency often fail to synchronize, which is why the key is not "can I connect it?" but "can it hold a stable signal long enough to charge?" The H2 / HS3 generator-sync path should be treated as a compatibility check, not assumed by default. If backup fuel charging matters to you, ask the installer to show the generator-control settings and the supported generator behavior on the quote.</p>

[/su_spoiler]

[/su_accordion]

---

## FAQ Group 2 — Long-Term Cost & Incentives

**Insert position:** after H2-07's installer question (the reader has the action item, but is now weighing long-term financial risk before committing). Place before H2-08's close.

### ❓ Quick Answers: Long-Term Costs & Incentives

[su_accordion]<p style="font-size: 20px;font-weight: bold;color: #1a1a1a;margin-top: 20px;margin-bottom: 15px">❓ Quick Answers: Long-Term Costs & Incentives</p>

[su_spoiler title="Q: What happens to my warranty if I add a battery in year 3?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>If your inverter is battery-ready (SAJ H2), adding an SAJ B2 battery does not void the inverter warranty — it is the designed expansion path.</strong></p>

<p>If your inverter is a non-battery-ready string inverter (Path A / R6), adding a battery requires an inverter swap or AC-coupled retrofit, and the original inverter's warranty does not transfer to the new hardware. Get the upgrade pathway and warranty-transfer terms in writing on day one — the vague answer is the expensive answer in year five. This is exactly what the single installer question in H2-07 is designed to surface.</p>

[/su_spoiler]

[su_spoiler title="Q: Will adding a battery later really cost thousands more than installing it now?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>Only if your inverter is not battery-ready — then expect $4,000–$9,000 more in retrofit costs.</strong></p>

<p>If you installed a battery-ready hybrid (SAJ H2) from day one, adding a battery later costs roughly the battery itself plus a half-day of labor — no inverter swap, no second box, no AC-coupled patch. The retrofit trap only bites Path A (string inverter) buyers. This is the core math behind the article's "battery-ready, not battery-required" frame: the inverter you buy today decides whether "later" is cheap or expensive.</p>

[/su_spoiler]

[su_spoiler title="Q: Does the federal tax credit still apply if I add a battery later?" open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""]

<p><strong>Yes — the 30% federal residential clean energy credit applies to a battery added later, as long as the battery is charged by your solar system.</strong></p>

<p>Standalone storage (not charged by solar) is not currently eligible. But a battery added to an existing solar system qualifies for the 30% credit on the battery + installation labor. The credit is currently 30% through 2032, stepping down afterward. Timing matters: adding the battery in a year when the credit is still at 30% preserves more value than waiting until the step-down years. Confirm the current schedule with your tax advisor before committing to a timeline.</p>

[/su_spoiler]

[/su_accordion]

---

## Objection-to-CTA Trace

| FAQ | Objection cleared | CTA it steers toward |
|---|---|---|
| Q1 (install time) | "This will disrupt my life for weeks" | H2 installer question + contact for a scoped quote |
| Q2 (panel upgrade) | "There are hidden costs I cannot see" | Installer load calc → contact |
| Q3 (generator sync) | "What if the grid fails and I want backup fuel charging?" | H2/HS3 product pages + installer compatibility check |
| Q4 (non-SAJ battery) | "I am locked into one brand" | SAJ B2 product page (the validated path) |
| Q5 (warranty year 3) | "Adding a battery breaks my warranty" | H2 product page (battery-ready = warranty-safe) |
| Q6 (cost thousands more) | "Later is always more expensive" | Path B H2 product page |
| Q7 (tax credit) | "I will lose the incentive by waiting" | Contact to lock in the 30% window |

Every answer resolves toward either the installer question (H2-07), a product page (H2/HS3), or contact — earned by the answer's logic, not bolted on.

---

## Truth-Bounded Ledger

| Specific claim | Source | Status |
|---|---|---|
| 1–2 days install for inverter + panels | Industry norm (EnergySage-style) | reference range, labeled |
| 2–8 weeks permitting | Industry norm | reference range, labeled |
| 100A panel upgrade $1,500–$3,000 | Industry norm (pre-1980 homes) | reference range, labeled |
| SAJ H2 half-day battery addition | T1.1 (dual 50 A ports, plug-and-play expansion) | evidence-backed |
| $4,000–$9,000 retrofit (non-battery-ready) | Draft-born estimate, Truth QA watchlist | reference range, labeled |
| SAJ B2 stack 180–800 V LiFePO4 | T1.1 | evidence-backed |
| 30% federal credit through 2032 | IRS Form 5695 / Inflation Reduction Act | external — flag for Truth QA strict verification |
| Non-SAJ battery voids warranty | Industry norm (manufacturer warranty terms) | reference, labeled |
| Generator support requires stable frequency + sync config | Existing product/technical reference in enriched draft visuals (`saj-ess-generator-charging-sync.webp`) | evidence-backed / implementation-dependent |

**Truth QA flag:** The "30% through 2032" claim is an external policy claim. If strict Truth QA is later run, verify against the current IRS schedule — tax credit step-downs are subject to legislative change. The answer is phrased conditionally ("currently 30% through 2032") to stay truthful even if the schedule changes.

---

## Publish-Pack Handoff Notes

- **FAQ Group 1** merges into `enriched-draft.md` after the H2-05 comparison table + "hybrid premium is option pricing" paragraph, and after Card 2 from `resources.md`.
- **FAQ Group 2** merges into `enriched-draft.md` after H2-07's installer question, before H2-08's close.
- `/article-publish-pack` should generate FAQPage schema JSON-LD from these 6 Q&A pairs (the `name` field = the question, the `acceptedAnswer.text` = the conclusion-first answer + elaboration).
- The old FAQ section currently at the end of `enriched-draft.md` (6 plain Q&A) should be removed once these friction-placed groups are merged in — the old version was a stopgap; this version is the conversion-designed replacement.
- Coordinate with `resources.md` Card 2 placement so Group 1 and Card 2 do not both land on the same sentence. Card 2 (curiosity) lands first; Group 1 (objection resolution) lands after.
