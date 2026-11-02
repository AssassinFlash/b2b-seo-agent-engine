# Benchmark Asset Ledger — Solar Without a Battery

**Project:** sunriver-inverter  
**Article:** solar-without-a-battery  
**Ledger date:** 2026-06-24  
**Policy:** benchmark-transmutation — copy structure, transform content, differentiate voice.

---

## Benchmark Sources

| Source | URL / File | Article Type | Why It Is a Benchmark |
|---|---|---|---|
| EnergySage | https://www.energysage.com/energy-storage/should-i-install-a-solar-battery-now-or-add-it-later/ | Residential buyer’s guide / risk-avoidance explainer | Best-in-class example of now-vs-later framing, conditional recommendation, technical specificity (coupling, storage-ready), and AIO-friendly key takeaways. |
| 饼干哥哥AGI / woshipm | https://www.woshipm.com/ (article by 饼干哥哥，微信公众号：饼干哥哥AGI) | Contrarian rant-with-lessons / live-demo tutorial | Demonstrates contradiction hook, proof-before-explanation opener, 青铜/黄金 wrong-way/right-way framing, and lesson-pivot conclusion. |
| JingSourcing | https://jingsourcing.com/is-alibaba-safe-legit/ | Risk-avoidance listicle / buyer’s guide | Best-in-class example of debunked-assumption H2 pattern, red-flag catalog, numbered prevention checklist, and B2B-vs-consumer framing. |

---

## Borrowed Assets

| Asset ID | Source / Origin | Borrowed Type | What Is Borrowed | Why It Works | Transformation Rule | Risk Label | Final Expression Rule | Section |
|---|---|---|---|---|---|---|---|---|
| BA-001 | EnergySage | Structure | Now-vs-later decision ladder: Do I need it? → What does it cost? → Is retrofitting hard? → What should I do? | Gives the reader a logical sequence that turns a binary worry into a qualified decision. | Replace residential-consumer battery timing with Sunriver supply-partner inverter-path timing (Path A/B/C). | safe | Use as the backbone information progression; final section names must be project-specific, not copied. | Whole-article arc |
| BA-002 | EnergySage | Structure | "Key takeaways" preview at the top of the article. | Captures AI Overview snippets and serves skimmers without spoiling the argument. | Compress the Path A/B/C promise + one action item into 3–5 bullets. | safe | Place immediately after the opener; bullets must be specific to SAJ inverter paths. | Opener / preview |
| BA-003 | EnergySage | Structure | Conditional recommendation structure ("if your priority is X, choose path Y"). | Avoids a hard verdict and respects reader context. | Map to Path A (cost now), Path B (future-proof), Path C (backup now). | safe | Use in the path-framework section; tie each condition to a SAJ product family. | Path framework |
| BA-004 | EnergySage | Data / concept | AC-coupled vs. DC-coupled distinction and "storage-ready" concept. | Explains why retrofitting can be expensive or inefficient. | Translate to SAJ H2 hybrid running grid-tied without battery and accepting SAJ battery later; verify voltage/capacity thresholds from current spec sheets. | transformed | Use only with current SAJ specs and a freshness disclaimer; do not copy EnergySage’s older percentages. | Path framework / technical debunk |
| BA-005 | EnergySage | Prose craft | Transition patterns: "That said," "When it comes down to it," "Above all," "After all." | Plain-English transitions that avoid academic filler. | Adopt the function (soft pivot, escalation, conclusion) but calibrate to Sunriver’s contrarian voice. | safe | Use 1–2 per section; avoid overuse. | Whole article |
| BA-006 | EnergySage | Brand stance | Information-first, platform-second credibility (data + named programs before CTA). | Builds trust before asking for action. | Lead with product specs and scenarios before any Sunriver CTA. | safe | CTA appears only after the educational framework is complete. | Whole article |
| BA-007 | 饼干哥哥AGI | Structure | Contradiction-title structure: title provokes, opener reframes. | Creates opening tension and earns attention. | Title already contradicts the "battery mandatory" assumption; opener reframes battery-less solar as strategy. | safe | Keep the title *Solar Without a Battery: The Battery Industry Hopes You Never Read This*; opener must immediately resolve the tension with proof. | Opener |
| BA-008 | 饼干哥哥AGI | Structure | Proof-before-explanation opener (show the end state first). | Lowers reader doubt before asking them to commit to a long explanation. | Open with a real system running without a battery, a spec, or a homeowner scenario — not a screenshot dump. | safe | First 150 words must contain concrete proof (spec, scenario, or system state). | Opener |
| BA-009 | 饼干哥哥AGI | Structure | 青铜 / 黄金 (Wrong-way / Right-way) tiered framing. | Makes the superior path feel earned after demonstrating the inferior path. | Map Bronze = non-battery-ready string-inverter path (retrofit trap); Gold = battery-ready hybrid path (H2). | transformed | Use the concept, not the Chinese labels; frame as "The retrofit trap" vs. "The battery-ready path." | Myth debunk / path framework |
| BA-010 | 饼干哥哥AGI | Structure | Rant → demonstration → lesson-pivot arc. | Emotional engagement + credibility + reframe. | Rant against "battery mandatory" → demonstrate with product evidence → pivot to "right battery-ready hardware path." | transformed | Keep the emotional arc but do not bash batteries; maintain diagnostic fairness. | Whole-article arc |
| BA-011 | 饼干哥哥AGI | Case pattern | Numbered protagonist case with specific quantities and failure modes. | Makes abstract claims concrete and memorable. | Create an anonymized homeowner/EPC scenario with realistic specs (e.g., 10 kW array, net-metering market) and specific failure mode (retrofit requires inverter swap). | transformed | Use hypothetical or anonymized scenarios only; label them clearly; no unverified client claims. | Path framework / proof |
| BA-012 | 饼干哥哥AGI | Prose craft | Colloquial emotional markers: "magic," "问题不大," "最后一公里的打磨." | Humanizes technical explanation. | Translate to English equivalents (e.g., "That is not magic — it is just the right inverter architecture," "the last mile of setup"). | safe | Use sparingly; avoid swearing or Chinese phrasing. | Whole article |
| BA-013 | 饼干哥哥AGI | Prose craft | Rhetorical questions as section hooks and lesson pivots. | Pulls the reader forward and crystallizes the reframe. | Use questions like "So is solar without a battery a bad idea?" and "What should you actually ask your installer?" | safe | 1–2 per major section; must be answered immediately. | Whole article |
| BA-014 | 饼干哥哥AGI | Editorial POV | Contrarian-but-qualified opinion that structures the piece. | Gives the article a stake and prevents generic explainer drift. | Stance: "Battery-less solar is a strategy, not a compromise — but only with a battery-ready inverter." | safe | Repeat the stance at opener, framework, and close. | Whole article |
| BA-015 | JingSourcing | Structure | Debunked-assumption H2 pattern: "X protects buyers — not Y." | Each H2 names a common belief then reframes it. | Translate to: "A hybrid inverter works without a battery — but not every hybrid is battery-ready in the same way." | transformed | Use for 1–2 myth-debunk H2s only; do not make every H2 a debunk. | Myth debunk |
| BA-016 | JingSourcing | Structure | Red-flag catalog with parallel H3s listing hidden risks. | Gives the reader fast diagnostic rules. | Apply to solar quote red flags: "battery mandatory" pressure, incompatible battery claims, vague warranty transfer. | transformed | Replace Alibaba-specific risks with solar procurement risks; keep the listicle format. | Red-flag catalog |
| BA-017 | JingSourcing | Structure | Numbered prevention sequence / checklist. | Converts risk awareness into action. | Use for "3 questions to ask before signing" or "Path A/B/C decision checklist." | safe | Numbered steps must be specific to SAJ inverter selection. | Action item / checklist |
| BA-018 | JingSourcing | Structure | Table of contents with jump-anchor bullets summarizing debunks. | Reduces skim abandonment and improves AIO capture. | TOC bullets must summarize Path A/B/C and red flags, not generic sections. | safe | Keep TOC short (5–7 bullets); anchor links optional. | Opener |
| BA-019 | JingSourcing | Viewpoint | B2B vs. consumer framing: "Homeowner expectations often come from B2C gadget reviews; solar hardware decisions work more like project procurement." | Reframes the reader’s mental model and justifies deeper technical scrutiny. | Apply to solar: contrast homeowner gadget expectations with EPC/installer procurement reality. | transformed | Do not copy Alibaba/B2C examples; use solar-specific contrasts. | Myth debunk / framework |
| BA-020 | JingSourcing | Prose craft | Plain-spoken, world-weary diagnostic voice: "learn these lessons the expensive way," "there’s no shortcut." | Signals practitioner experience without self-praise. | Calibrate to Sunriver voice: "That is the retrofit trap in plain English," "There is no shortcut around the inverter spec sheet." | safe | Use in myth-debunk and red-flag sections; avoid inspirational tone. | Myth debunk / red flags |
| BA-021 | JingSourcing | Data pattern | Specific parameter thresholds (5+ years, $500, 2.9%) with source-style framing. | Makes advice feel researched and actionable. | Translate to solar thresholds: inverter efficiency floors, battery expansion voltage, warranty terms, AHJ rules — all with current spec/source disclaimers. | transformed | Every threshold must be tied to a current SAJ spec or labeled "confirm with installer." | Path framework / specs |
| BA-022 | JingSourcing | Brand stance | Skeptical of platform marketing but fair to suppliers. | Builds trust by being diagnostic rather than inflammatory. | Apply to installers/battery marketing: skeptical of "battery mandatory" pitches, fair to installers who genuinely size for backup need. | safe | No installer bashing; focus on hardware facts and buyer education. | Whole article |

---

## Ownership Boundary

- **Owned proof:** SAJ inverter product specifications (R6, H2, HS3), compatibility claims, and warranty terms as published by SAJ / Sunriver.
- **Public source:** Federal/state incentive rules (if cited) must include source, year, region, and scope.
- **Industry pattern:** "battery-ready" concept, AC/DC coupling distinctions, and retrofit economics are industry-standard knowledge.
- **Hypothetical scenario:** Any homeowner/EPC scenario used for illustration must be labeled as hypothetical or anonymized, with realistic but non-proprietary numbers.
- **Must not claim as owned:** EnergySage’s proprietary data, 饼干哥哥AGI’s screenshots/Chinese phrasing, JingSourcing’s client cases, Alibaba-specific mechanics, or any competitor’s proprietary product claims.

---

## Risk Summary

| Risk Label | Count | Meaning |
|---|---|---|
| safe | 14 | Public-domain / industry-standard pattern; can be imitated directly. |
| transformed | 8 | Borrowed and adapted to Sunriver context; monitor in draft for source drift. |
| watch | 0 | Close to source material; needs operator review. |
| blocked | 0 | Cannot use; none in this ledger. |

**Drift guards:**
- Sunriver does not bash batteries.
- No paragraph should be able to appear on a competitor site unchanged.
- All tax/regulatory/financial claims must carry an "as of 2026 / confirm with a licensed professional" disclaimer.
- Product routing must remain explicit: R6 (on-grid, no battery now), H2 (hybrid, battery-ready), HS3 (all-in-one, battery now).
