# Narrative Arc — Solar Without a Battery

- Project: `sunriver-inverter`
- Article slug: `solar-without-a-battery`
- Stage: `/article-arc`
- Date: 2026-06-24
- Next skill: `/article-draft`
- Primary benchmark formula: EnergySage (residential buyer's guide) + 饼干哥哥AGI / woshipm (contrarian rant-with-lessons) + JingSourcing (risk-avoidance listicle)
- Imitate / Inject / Differentiate: 35% / 40% / 25%

## Purpose

A 3,000-word article without a pre-designed arc becomes "module stacking". This arc locks the reader's cognitive journey before a single paragraph is written. The arc follows the skeleton's cognitive sequence — it does not redesign the H2s.

## Upstream Consumption

| Upstream File | Extracted | Used For |
|---|---|---|
| `skeleton.md` | arc-node-role per H2 (8 roles); full H2 sequence + voice lens; Skeleton-Arc consistency check (no flags) | The arc maps these roles to the 6-node reader journey |
| `benchmark-success-formula.md` §2.2/2.3/2.4/2.14 | Reader state, opening tension, angle, human texture | Imitating how the 3 benchmarks handle narrative transitions |
| `evidence-opinion-pack.md` §5.2 | Voice lens per scene (Josh Braun / Sujan Patel / Ann Handley / Joe Sugarman) | Arc's emotional progression matches the voice intensity per section |
| `project-profile.md` §3 | Primary buyer = homeowner; secondary = distributor; tertiary = EPC/installer | Trust shift must land for the homeowner while staying credible to the installer |

### Skeleton-Arc Consistency Check

- ✅ Every H2 has an arc-node-role assigned (8/8).
- ✅ Opening Reframe appears in H2-01 first 150 words — early enough.
- ✅ Trust Shift is **progressive**, not a single mechanical "why choose us" section: H2-06 (red-flag competence) + H2-07 (single action item) jointly carry the trust transfer. This matches the JingSourcing risk-list arc rhythm — the same expertise that explains the complexity also helps the reader control it.
- ✅ Middle Build rhythm preserved: H2-05 (spec-heavy comparison table) → H2-06 (scannable checklist) — formats differ.
- No blocking flags. The skeleton uses 7 benchmark-native custom roles (Arrival/Reframe/Orientation/Qualification/Myth correction/Framework confidence/Defensive competence/Action readiness/Close) rather than the standard 6 nodes — this is allowed (the skill permits benchmark-native roles) and fits the JingSourcing+EnergySage hybrid arc better than forcing 6 visible beats.

---

## The 6-Node Arc (diagnostic; mapped to the skeleton's custom roles)

### Node 1 — Starting State (H2-01 opener)

The reader arrives after seeing battery-heavy marketing and assumes solar + storage is the default. They fear: missing backup power or incentives, buying an inverter that can't accept a battery later, looking cheap or shortsighted to an installer or spouse. They want a binary answer (battery or no battery) but actually need a **path decision framework** (Path A / B / C).

### Node 2 — Opening Reframe (H2-01)

The opener (first 150–250 words) reframes: "No — if your inverter is battery-ready." The reframe moves the question from "should I get a battery?" to "which inverter architecture lets me defer the battery without locking myself out?" Stack proof on top of the provocation within the first 150 words (a real SAJ H2 system running grid-tied without a battery, the anti-islanding caveat, the Path A/B/C preview). Borrowed from 饼干哥哥AGI: title contradicts the common assumption, opener reveals the real method.

### Node 3 — First Turn (H2-02 + H2-03)

The reader moves from "agonizing over the battery" to "self-diagnosing which path they are on".
- **H2-02** defines the central term "battery-ready" through SAJ H2 spec (dual 50 A battery ports, 180–800 V LiFePO4), not marketing copy. Orientation.
- **H2-03** is a 3-question self-qualification that routes the reader to Path A / B / C using rate-plan context (net metering vs. net billing, outage frequency, budget). Qualification.

This is where the Decision Framework enters. The turn must make the reader feel: "I was asking the wrong question — the question is which path I'm on."

### Node 4 — Middle Build (H2-04 + H2-05)

Judgment upgrades progressively — the middle is NOT a flat list of equivalent sections.
- **H2-04** debunks the retrofit trap: "I can just add a battery later" ignores inverter swap, AC-coupled hardware, labor, and installer availability. Myth correction.
- **H2-05** gives the core Path A/B/C comparison table (R6 grid-tied / H2 hybrid / HS3 all-in-one ESS) with a conditional "which is best" answer. Framework confidence.

Dependency chain: the reader first learns what battery-ready means (H2-02) → whether they need a battery (H2-03) → what deferring really costs (H2-04) → how the three paths compare (H2-05). Each section builds on the judgment established in the previous one.

### Node 5 — Trust Shift (H2-06 + H2-07) — progressive

The reader transitions from "I understand this product" to "I trust this supplier to help me control project risk". This shift is **split across two sections**, not forced into a single "why choose us" beat:
- **H2-06** — red-flag checklist: the exact quote phrases and spec gaps that lock a buyer out of a future battery. Defensive competence. The reader feels: the same expertise that explained the retrofit trap is now helping me screen quotes.
- **H2-07** — the single best question to ask an installer ("If I add a battery in three years, what changes in this quote?"). Action readiness. The reader feels: this supplier has distilled the whole article into one sentence I can use today.

Trust is earned because the expertise that explained the complexity is the same expertise that controls it. The shift lands in the latter third, matching benchmark rhythm.

### Node 6 — Arrival State (H2-08)

After finishing, the reader:
- Understands that "solar without a battery" is a viable hardware strategy, not a compromise — and that the real risk is buying an inverter that locks out future storage.
- Can self-identify their path (A / B / C) and route to the matching SAJ inverter (R6 / H2 / HS3).
- Knows what information affects pricing and what to send a supplier for an accurate recommendation.
- Has one concrete question to ask any installer before signing.

The natural next action is a path-specific product page / quote — this determines the CTA. H2-08 closes with the sticky reframe "battery-ready, not battery-required" and path-specific routing. Borrowed from 饼干哥哥AGI lesson-pivot + EnergySage launchpad conclusion.

---

## Arc-to-Skeleton Map

| Skeleton Section (full H2) | Arc Node(s) | Role in the Arc |
|---|---|---|
| H2-01 Is It a Mistake to Run Solar Panels Without a Battery? | Node 1 (Starting State) + Node 2 (Opening Reframe) | Answer the title immediately; reframe "should I get a battery" into "which inverter path"; preview Path A/B/C; state the no-backup caveat |
| H2-02 What Does "Battery-Ready" Solar Actually Mean—And Is It Worth It? | Node 3 (First Turn) | Define the central term via SAJ H2 spec; give the conditional "worth it" rule |
| H2-03 How Do You Know If You Actually Need a Solar Battery? | Node 3 (First Turn) | 3-question self-qualification; route reader to Path A/B/C |
| H2-04 Is It Really More Costly to Add a Battery to Solar Later? | Node 4 (Middle Build) | Debunk the retrofit trap; judgment upgrade |
| H2-05 Grid-Tied vs. Hybrid Solar: Which Is Best If You Don't Want a Battery? | Node 4 (Middle Build) | Path A/B/C comparison table; conditional "which is best" |
| H2-06 Which Solar Quote Red Flags Can Lock You Out of a Battery Later? | Node 5 (Trust Shift) | Red-flag checklist; defensive competence |
| H2-07 What Is the Number One Question to Ask Your Solar Installer Before Signing? | Node 5 (Trust Shift) | Single action item; trust → executable |
| H2-08 How Do You Choose an Inverter That Lets You Decide on a Battery Later? | Node 6 (Arrival) | Path-specific routing; "battery-ready, not battery-required" close; CTA |

---

## Key Transitions (the ones that decide whether the reader keeps going)

1. **H2-01 → H2-02** — from "the answer is No-if" to "wait, what does battery-ready actually mean?" If weak, the reader drops off after the reframe. Carried by H2-01's transition signal: "If 'battery-ready' is the key phrase, then we should define it before anyone sells it to you."
2. **H2-03 → H2-04** — from "I know whether I need a battery" to "will deferring it cost me more later?" This is the start of the trust shift; the reader must feel the hidden-cost reveal.
3. **H2-05 → H2-06** — from "I've picked a path" to "but a quote can still lock me out." From framework confidence to defensive competence — creates the "there are still traps" tension.
4. **H2-07 → H2-08** — from "one action item" to "choose the inverter for your path." The CTA must land naturally, not as a hard break.

---

## Voice Intensity Progression

Matches `evidence-opinion-pack.md` §5.2:

| H2 | Voice lens | Intensity |
|---|---|---|
| H2-01 | Josh Braun (contrarian-but-qualified) | High opener, then qualify |
| H2-02 | Sujan Patel (systematic, executable) | Measured, definitional |
| H2-03 | Sujan Patel / Ann Handley (empathy + structure) | Warm, diagnostic |
| H2-04 | Josh Braun + field language | Diagnostic, plain-spoken |
| H2-05 | Sujan Patel | Clean, comparative |
| H2-06 | Josh Braun + field language | Practitioner fatigue, red-flag tone |
| H2-07 | Sujan Patel / Joe Sugarman | Memorable, single-action |
| H2-08 | Joe Sugarman | Sticky one-liner close |

The emotional arc: provocative opener → measured definition → empathetic self-quiz → diagnostic myth-bust → clean comparison → defensive competence → single action → empowering close. Trust builds gradually, lands at H2-06/07, seals at H2-08.

---

## Expert Risk Flags (from independent SEO content-strategy review, 2026-06-24)

> An independent expert review (You.com deep research) flagged the following. These do NOT block the arc — they are recorded here as inputs for a possible `/article-skeleton` rework and for `/article-draft` content coverage. The arc is designed on the current 8 H2s; if the skeleton is reworked, re-run `/article-arc`.

### RF-1 — Missing definition + pros/cons H2 (AIO/PAA gap) — **highest priority**
The SERP for "solar without a battery" is dominated by articles with an explicit "What is a solar system without a battery / Advantages / Limitations" chunk. This outline jumps straight into decision psychology and installer dialogue, skipping the clean definition chunk Google AI Overview needs to extract. **Risk:** reduced AIO/PAA capture on the core definitional intent.
**Mitigation options (for skeleton rework):** add a definitional H2 after H2-01 (e.g. "What Is a Solar System Without a Battery — and How Does It Work?") with a tight pros/cons summary; OR fold a 3–5 bullet "what it is + pros + cons" key-takeaways box into H2-01's opener that AIO can extract as a standalone chunk.

### RF-2 — Micro-tension hooks slightly risky for B2B credibility
The 7:3 micro-tension words (Actually / Really / Mistake / Lock You Out) work for homeowners but can read as less technically rigorous to distributor/installer readers. **Risk:** secondary/tertiary buyers (distributor, EPC) may discount the article.
**Mitigation:** keep tension words but place the clean SEO question first and the hook second (already mostly the case); soften the most alarmist phrasing in H2-06 ("Lock You Out" is fine; ensure the body stays field-diagnostic, not fear-mongering). Note: this is consistent with the article-title skill's Level 2 (CTR hook + trust floor) — H2s stay measured, the article H1 title can carry the stronger hook.

### RF-3 — H2-06 + H2-07 could merge into one "installer conversation" H2 + H3
Both are installer-communication topics; splitting them into two H2s can feel clickbait-ish and slightly fragmented. **Risk:** minor structural redundancy.
**Mitigation:** considered and **deferred** — the skeleton's H2 count = 8 is intentional (fits the 3000-word decision-ladder arc), and splitting red-flags (screening) from the single question (action) serves different reader jobs. Do not merge unless word count forces it. Revisit at draft if H2-06/07 feel thin.

### Content-coverage gaps for `/article-draft` (not H2-structure issues)
The expert noted intent segments searchers expect that the current outline covers only implicitly. `/article-draft` should ensure these are addressed, likely as H3s, FAQ entries, or within existing H2 bodies:
- **Off-grid without a battery** — why it is almost always a poor choice for homes (distinguish from grid-tied battery-less, which is the article's actual scope). The primary keyword "solar system without battery" captures some off-grid-intent searchers; the article must not conflate the two.
- **"What appliances can it run?"** — a common PAA-style question; cover under H2-05 or an FAQ.
- **"Does it work during a power outage?"** — the anti-islanding caveat is in H2-01 but should be reinforced (high PAA intent).
- **H2-04 technical feasibility** — the retrofit section currently leads with cost; add the technical feasibility dimension (AC- vs DC-coupled, inverter-swap mechanics) so it is not cost-only.

---

## Draft Handoff Notes

- The arc is **progressive-trust**, not single-beat-trust. Draft H2-06 and H2-07 as a continuous trust-transfer unit, not two disconnected sections.
- H2-01 must answer the title in the first paragraph AND contain an AIO-extractable definition chunk (see RF-1) — do not make H2-01 pure provocation.
- The Path A/B/C framework is the spine: it is introduced in H2-01, applied in H2-03, cost-analyzed in H2-04, tabulated in H2-05, defended in H2-06, acted on in H2-07, routed in H2-08. Draft every section so the Path A/B/C thread is continuous — a reader who jumps to any H2 should still orient via the path labels.
- "battery-ready, not battery-required" is the sticky phrase — plant it in H2-01, echo in H2-02, seal in H2-08.
- Honor the Numeric Control Vector from skeleton.md: 8 AIO answerable moments (one per H2), 5–6 bold trade-off calls, opinion intensity 6/10, high evidence pressure (every claim tied to Tier 1/2 evidence).
- **Anti-Presupposition**: all specs/numbers in the arc (SAJ H2 dual 50 A ports, 180–800 V, R6 5–50 kW 98.8%, HS3 5–40 kWh) come from the locked profile / evidence pack — do not introduce new specs in the draft without evidence.

## Guardrails

- **Consistency**: every H2 has a clear reader-journey role (verified above).
- **Tone balance**: the Trust Shift feels earned in the JingSourcing risk-list rhythm, not introduced by formula.
- **Intent protection**: all paths lead commercial buyers to factory specification checkpoints (Path A/B/C → SAJ product routing); do not cater to DIY off-grid installers (see RF-1 off-grid note).
