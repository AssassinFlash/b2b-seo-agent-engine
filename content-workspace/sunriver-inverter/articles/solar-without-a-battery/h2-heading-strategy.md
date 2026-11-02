# H2 Heading Strategy

**Article:** `solar-without-a-battery`  
**Project:** `sunriver-inverter`  
**Stage:** `/article-skeleton`  
**Date:** 2026-06-24

---

## Strategy Summary

| Control | Chosen value | Justification |
|---|---|---|
| Target H2 count | 8 | Matches the article's decision-ladder length (arrival → orientation → qualification → myth correction → framework confidence → defensive competence → action readiness → reframe/close) without overwhelming the 2,500–3,500 word target. |
| 7:3 ratio | 70% clean SEO / 30% micro-tension | Primary keyword cluster (`solar without a battery`, `solar system without battery`) is question-heavy and AIO-friendly; 30% hook words (`Mistake`, `Actually`, `Really`, `Costly`, `Number One`, `Lock You Out`) preserve the contrarian Sunriver voice without breaking indexability. |
| AIO capture target | 8 answerable moments (one per H2) | Google PAA and AIO dominate this SERP; each H2 is a direct question that can be extracted as a snippet, comparison, checklist, or single-answer block. |
| Format repetition tolerance | Max 2 consecutive similar sections | Alternates prose → table → prose → list → prose → checklist → prose → close; prevents template-copy fatigue. |

**Core principle:** Every H2 is a search-facing question by default. Each H2 must be indexable by Google AIO/PAA (70% standard search entities) and clickable by humans (30% micro-tension hook).

---

## Upstream Research Reference

`/article-skeleton` does **not** perform live extraction. All candidates come from upstream artifacts. For each source, confirm it was read and record the key evidence location.

| Source artifact | What was extracted | Evidence location | Candidate count | Status |
|---|---|---|---|---|
| `intent-research.md` | Consolidated candidate pool (C-01 to C-17) + intent mapping | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/intent-research.md` | 17 | ✅ |
| `content-type-library.md` | Library categories + selected exemplar H2 patterns (LIB-01, LIB-04, LIB-06) | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/content-type-library.md` | 8 library entries, 3 selected | ✅ |
| `topic-card.md` Outline Sketch | Seed H2s and search intent | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/topic-card.md` §Outline Sketch | 8 outline items | ✅ |
| `benchmark-candidates.md` | Selected primary exemplars and H2 patterns | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/benchmark-candidates.md` | 3 selected | ✅ |
| `benchmarks/<source>-extraction.md` | Actual H2s from selected benchmarks | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/benchmarks/energysage-extraction.md`, `jingsourcing-extraction.md`, `woshipm-extraction.md` | 3 extractions | ✅ |
| User-provided external H2s | Operator-supplied heading optimizations | operator input during `/article-skeleton` | 8 final H2s | ✅ |

### Upstream gap log

| Source | Gap / issue | Workaround used |
|---|---|---|
| — | No gaps. All required upstream artifacts were present and sufficient. | — |

---

## Final H2 Table

| # | Final H2 | 70% SEO Base | 30% Hook | Source | Voice Lens | Format | AIO Answer Type | Arc Node |
|---|---|---|---|---|---|---|---|---|
| H2-01 | Is It a Mistake to Run Solar Panels Without a Battery? | Is it a mistake to run solar panels without a battery? | Mistake | intent-research C-01 + user-input | Josh Braun | prose + key-takeaways box | direct answer | Arrival / Opening Reframe |
| H2-02 | What Does "Battery-Ready" Solar Actually Mean—And Is It Worth It? | What does battery-ready solar mean and is it worth it? | Actually | intent-research C-05 + user-input | Sujan Patel | prose + definition | definition + comparison | Orientation |
| H2-03 | How Do You Know If You Actually Need a Solar Battery? | How do you know if you need a solar battery? | Actually | intent-research C-06 + C-07 + user-input | Sujan Patel / Ann Handley | prose + 3-question qualifier | checklist | Qualification |
| H2-04 | Is It Really More Costly to Add a Battery to Solar Later? | Is it more costly to add a battery to solar later? | Really / Costly | intent-research C-08 + C-09 + user-input | Josh Braun + field language | prose + scenario | direct answer + comparison | Myth correction |
| H2-05 | Grid-Tied vs. Hybrid Solar: Which Is Best If You Don't Want a Battery? | Grid-tied vs hybrid solar which is best without battery | (implicit choice tension) | intent-research C-10 + C-12 + user-input | Sujan Patel | comparison table + prose | comparison | Framework confidence |
| H2-06 | Which Solar Quote Red Flags Can Lock You Out of a Battery Later? | Solar quote red flags that prevent adding a battery later | Lock You Out | intent-research C-13 + C-17 + user-input | Josh Braun + field language | checklist + prose | checklist | Defensive competence |
| H2-07 | What Is the Number One Question to Ask Your Solar Installer Before Signing? | What question to ask solar installer before signing | Number One | intent-research C-14 + user-input | Sujan Patel / Joe Sugarman | prose + copy-paste block | direct answer | Action readiness |
| H2-08 | How Do You Choose an Inverter That Lets You Decide on a Battery Later? | How to choose an inverter for future battery addition | Lets You Decide | intent-research C-15 + user-input | Joe Sugarman | prose + launchpad links | direct answer + CTA | Reframe / Close |

**Micro-tension word bank (use sparingly):** Actually, Really, Mistake, Costly, Trap, Number One, Lock You Out, Sneaky, Hidden, Wrong.

---

## Raw Candidate Inventory

Upstream H2 assets integrated:
- [x] `intent-research.md` consolidated candidate pool
- [x] `content-type-library.md` selected exemplar H2 patterns
- [x] `topic-card.md` Outline Sketch
- [x] `benchmark-candidates.md` selected primary exemplars
- [x] `benchmarks/<source>-extraction.md` actual H2s
- [x] `benchmark-success-formula.md` Structural Blueprint / Question Ladder
- [x] User-provided external H2 optimization

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance | Final H2 # or discard |
|---|---|---|---|---|---|---|---|---|
| 1 | Can you use solar panels without a battery? | intent-research C-01 (from Google PAA) | `intent-research.md` §Raw Candidate Inventory #1 | Viability confirmation | Informational | Direct answer opener | High | absorbed into H2-01 |
| 2 | Are solar panels without a battery worth it? | intent-research C-02 (from Google PAA) | `intent-research.md` §Raw Candidate Inventory #2 | ROI / worth-it | Informational + consideration | Cost trade-off | High | absorbed into H2-01 + H2-04 |
| 3 | Can solar panels generate electricity without a battery? | intent-research (from Google PAA) | `intent-research.md` §Raw Candidate Inventory #3 | Mechanics | Informational | Explainer | Medium | absorbed into H2-02 |
| 4 | Do solar panels work at night without a battery? | intent-research (from Google PAA) | `intent-research.md` §Raw Candidate Inventory #4 | Safety / backup | Informational | Caveat delivery | High | absorbed into H2-01 + H2-05 |
| 5 | How do solar panels work if you don't have a battery? | intent-research (from Google PAA) | `intent-research.md` §Raw Candidate Inventory #5 | Mechanics | Informational | Explainer | Medium | absorbed into H2-02 |
| 6 | Why do so many guides push batteries and what do they leave out? | topic-card outline sketch | `topic-card.md` §Outline Sketch item 2 | Skepticism / trust | Informational | Contrarian reframe | Medium | absorbed into H2-01 + H2-02 |
| 7 | When no-battery makes sense | topic-card outline sketch | `topic-card.md` §Outline Sketch item 4 | Self-qualification | Informational + consideration | Path qualification | High | absorbed into H2-03 |
| 8 | When battery-now makes sense | topic-card outline sketch | `topic-card.md` §Outline Sketch item 5 | Self-qualification | Informational + consideration | Path qualification | High | absorbed into H2-03 + H2-08 |
| 9 | Should I install a solar battery now or add it later? | EnergySage benchmark H2 chain | `content-type-library.md` LIB-01 + `benchmarks/energysage-extraction.md` | Timing decision | Informational + consideration | Now-vs-later framework | High | absorbed into H2-04 |
| 10 | Retrofit system integration / storage-ready solar panel system | EnergySage benchmark H2 chain | `content-type-library.md` LIB-01 + `benchmarks/energysage-extraction.md` | Retrofit mechanics | Informational | Future-proofing proof | High | absorbed into H2-02 + H2-04 |
| 11 | "Battery-ready" label ≠ any battery works | JingSourcing debunked-assumption | `content-type-library.md` LIB-04 + `benchmarks/jingsourcing-extraction.md` §Debunked-Assumption H2 Pattern | Assumption debunk | Informational + defensive | Red-flag framing | High | absorbed into H2-06 |
| 12 | Low quotes that hide inverter swap costs | JingSourcing debunked-assumption | `content-type-library.md` LIB-04 + `benchmarks/jingsourcing-extraction.md` | Quote screening | Defensive | Red-flag framing | High | absorbed into H2-06 |
| 13 | Can I use solar panels without battery storage? | Solar.com / EcoFlow competitor H2 | `content-type-library.md` LIB-02 + prior research-deep/serp-competitor-research.md | Viability confirmation | Informational | Direct answer | High | absorbed into H2-01 |
| 14 | How does a solar system without a battery work? | Solar.com / EcoFlow competitor H2 | `content-type-library.md` LIB-02 + prior research-deep/serp-competitor-research.md | Mechanics | Informational | Explainer | Medium | absorbed into H2-02 |
| 15 | Are solar panels worth it without a battery? | Solar.com / EcoFlow competitor H2 | `content-type-library.md` LIB-02 + prior research-deep/serp-competitor-research.md | ROI / worth-it | Informational + consideration | Cost trade-off | High | absorbed into H2-01 + H2-04 |
| 16 | solar panels without a battery | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #6 | Viability confirmation | Informational | Direct answer variant | High | absorbed into H2-01 |
| 17 | is solar without a battery worth it | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #7 | ROI / worth-it | Informational + consideration | Cost trade-off | High | absorbed into H2-01 + H2-04 |
| 18 | solar power without a battery | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #8 | Viability confirmation | Informational | Direct answer variant | Medium | absorbed into H2-01 |
| 19 | solar system without a battery | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #9 | Viability confirmation | Informational | Direct answer variant | High | absorbed into H2-01 + H2-05 |
| 20 | solar without battery inverter | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #10 | Hardware path | Informational + consideration | Product routing | High | absorbed into H2-02 + H2-05 |
| 21 | solar without battery storage | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #11 | Viability confirmation | Informational | Direct answer variant | Medium | absorbed into H2-01 |
| 22 | solar without battery backup | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #12 | Safety / backup | Informational | Caveat delivery | High | absorbed into H2-01 + H2-05 |
| 23 | hybrid inverter without battery | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #13 | Hardware path | Informational + consideration | Product routing | High | absorbed into H2-05 |
| 24 | solar inverter without battery | Google Autocomplete (via intent-research) | `intent-research.md` §Raw Candidate Inventory #14 | Hardware path | Informational + consideration | Product routing | High | absorbed into H2-05 |
| 25 | Hybrid inverter, backup without batteries | Reddit r/SolarDIY (via intent-research) | `intent-research.md` §Raw Candidate Inventory #15 | Safety / backup | Informational + consideration | Path comparison | High | absorbed into H2-05 |
| 26 | Is there a way for cheap solar, without batteries? | Reddit r/SolarDIY (via intent-research) | `intent-research.md` §Raw Candidate Inventory #16 | Cost / budget | Informational + consideration | Cost trade-off | High | absorbed into H2-04 |
| 27 | Getting a house with Solar, 1:1 credit, but no batteries | Reddit r/SolarDIY (via intent-research) | `intent-research.md` §Raw Candidate Inventory #17 | Self-qualification | Informational + consideration | Path qualification | High | absorbed into H2-03 |
| 28 | Solar without battery/inverter? | Reddit r/SolarDIY (via intent-research) | `intent-research.md` §Raw Candidate Inventory #18 | Mechanics | Informational | Explainer | Medium | absorbed into H2-02 |
| 29 | No batteries no grid tie with grid backup. Is a hybrid inverter the solution? | Reddit r/SolarDIY (via intent-research) | `intent-research.md` §Raw Candidate Inventory #19 | Path comparison | Informational + consideration | Product-routing framework | Medium | absorbed into H2-05 |
| 30 | New Solar Installation - Hybrid Inverter - Turns Off during Load | Reddit r/SolarPakistan (via intent-research) | `intent-research.md` §Raw Candidate Inventory #20 | Warning / malfunction | Defensive | Red-flag / installer issue | Medium | absorbed into H2-06 |
| 31 | Is It a Mistake to Run Solar Panels Without a Battery? | user-provided 7:3 redesign | Operator input | Framed viability | Informational + consideration | Contrarian direct answer | High | H2-01 |
| 32 | What Does "Battery-Ready" Solar Actually Mean—And Is It Worth It? | user-provided 7:3 redesign | Operator input | Definition / worth | Informational + consideration | Terminology + value | High | H2-02 |
| 33 | How Do You Know If You Actually Need a Solar Battery? | user-provided 7:3 redesign | Operator input | Self-qualification | Informational + consideration | Need diagnostic | High | H2-03 |
| 34 | Is It Really More Costly to Add a Battery to Solar Later? | user-provided 7:3 redesign | Operator input | Retrofit economics | Informational + consideration | Myth correction | High | H2-04 |
| 35 | Grid-Tied vs. Hybrid Solar: Which Is Best If You Don't Want a Battery? | user-provided 7:3 redesign | Operator input | Path comparison | Informational + consideration | Product-routing framework | High | H2-05 |
| 36 | Which Solar Quote Red Flags Can Lock You Out of a Battery Later? | user-provided 7:3 redesign | Operator input | Quote screening | Defensive | Red-flag catalog | High | H2-06 |
| 37 | What Is the Number One Question to Ask Your Solar Installer Before Signing? | user-provided 7:3 redesign | Operator input | Action readiness | Transactional | Single action item | High | H2-07 |
| 38 | How Do You Choose an Inverter That Lets You Decide on a Battery Later? | user-provided 7:3 redesign | Operator input | Product selection | Informational + consideration | Closing framework | High | H2-08 |

**Required evidence format for live channels:**
- Google PAA: exact query URL + DOM selector used (recorded in `intent-research.md` §Research Execution Log).
- Google Autocomplete: exact API URL used (recorded in `intent-research.md` §Research Execution Log).
- Reddit: exact search query + thread URL(s) (recorded in `intent-research.md` §Research Execution Log).

---

## External Input Absorption (if applicable)

| External H2 | Source | Reverse-engineered SEO base | Reverse-engineered hook | Conflict with benchmark/profile? | Absorbed as-is / adapted / rejected |
|---|---|---|---|---|---|
| Is It a Mistake to Run Solar Panels Without a Battery? | user-input | Is it a mistake to run solar panels without a battery? | "Mistake" — loss-aversion framing | None; matches Josh Braun opener lens and contrarian project voice. | absorbed as-is |
| What Does "Battery-Ready" Solar Actually Mean—And Is It Worth It? | user-input | What does battery-ready solar mean and is it worth it? | "Actually" — debunks vague marketing | None; aligns with Sujan Patel systematic explanation lens and EnergySage "storage-ready" reframe. | absorbed as-is |
| How Do You Know If You Actually Need a Solar Battery? | user-input | How do you know if you need a solar battery? | "Actually" — forces self-qualification | None; matches EnergySage need-qualification ladder and Sujan Patel/Ann Handley empathetic-systematic lens. | absorbed as-is |
| Is It Really More Costly to Add a Battery to Solar Later? | user-input | Is it more costly to add a battery to solar later? | "Really" / "Costly" — challenges retrofit assumption | None; aligns with JingSourcing debunked-assumption pattern and Josh Braun + field-language lens. | absorbed as-is |
| Grid-Tied vs. Hybrid Solar: Which Is Best If You Don't Want a Battery? | user-input | Grid-tied vs hybrid solar which is best without battery | Implicit choice tension in "Which Is Best" | Minor: benchmark-success-formula requires Path C (HS3) coverage. Resolved by making the comparison table explicitly three columns: R6 (Grid-Tied / Path A), H2 (Hybrid / Path B), HS3 (All-in-One ESS / Path C). | absorbed as-is with Path C caveat |
| Which Solar Quote Red Flags Can Lock You Out of a Battery Later? | user-input | Solar quote red flags that prevent adding a battery later | "Lock You Out" — future-pain framing | None; matches JingSourcing red-flag catalog and Josh Braun + field-language lens. | absorbed as-is |
| What Is the Number One Question to Ask Your Solar Installer Before Signing? | user-input | What question to ask solar installer before signing | "Number One" — singular action anchor | None; matches EnergySage closing installer instruction and Sujan Patel/Joe Sugarman action lens. | absorbed as-is |
| How Do You Choose an Inverter That Lets You Decide on a Battery Later? | user-input | How to choose an inverter for future battery addition | "Lets You Decide" — agency/choice framing | None; closes the Path A/B/C framework and matches Joe Sugarman memorable CTA lens. | absorbed as-is |

---

## Rhythm Audit

| Check | Result |
|---|---|
| No two consecutive sections repeat the same format by default habit | ✅ H2-01 prose/takeaways → H2-02 prose/definition → H2-03 prose/qualifier → H2-04 prose/scenario → H2-05 table → H2-06 checklist → H2-07 prose/copy-paste → H2-08 prose/launchpad. No back-to-back identical formats. |
| Heavy section followed by lighter section | ✅ H2-05 (spec-heavy comparison table) is followed by H2-06 (scannable checklist). H2-04 (economics scenario) is followed by H2-05 (table). |
| Voice lens varies across neighboring sections | ✅ Josh Braun → Sujan Patel → Sujan Patel/Ann Handley → Josh Braun → Sujan Patel → Josh Braun → Sujan Patel/Joe Sugarman → Joe Sugarman. Neighboring sections shift voice register. |
| Question ladder traces from arrival to CTA without jumps | ✅ Arrival (mistake?) → Orientation (what is battery-ready?) → Qualification (do I need one?) → Myth correction (is later more costly?) → Framework (which path?) → Defense (what red flags?) → Action (what to ask?) → Close (how to choose?). Logical escalation. |
| Each H2 can be answered in 1–2 sentences for AIO | ✅ Every H2 has a direct one-sentence answer anchored in the evidence pack (e.g., H2-01: "No—if the inverter is battery-ready"; H2-07: "Ask whether adding a battery later requires replacing the inverter"). |
| Intentional repetition is justified by benchmark rhythm | ✅ "battery-ready" and Path A/B/C labels repeat across opener, framework, and close as intentional-rhythm anchors per benchmark-success-formula §3.5. |

---

## Benchmark Alignment Check

| Benchmark pattern | Where it appears in final H2s | Transformed for project role? |
|---|---|---|
| EnergySage now-vs-later decision ladder | H2-04 (add battery later), H2-07 (installer question before signing) | ✅ Transmuted from generic solar timing to SAJ inverter-path economics and a single pre-sign question. |
| EnergySage "storage-ready" framing | H2-02 (battery-ready definition), H2-08 (choose inverter that lets you decide later) | ✅ Translated to "battery-ready inverter" and SAJ H2 plug-and-play expansion path. |
| 饼干哥哥AGI contradiction hook + lesson pivot | H2-01 (mistake framing), H2-08 (reframe/close) | ✅ English register; no anti-battery bashing—contrarian-but-qualified supply-partner stance. |
| JingSourcing debunked-assumption H2 pattern | H2-02 (actually mean), H2-04 (really more costly), H2-06 (red flags) | ✅ Solar buyer assumptions instead of Alibaba supplier assumptions. |
| JingSourcing red-flag catalog | H2-06 (quote red flags that lock you out) | ✅ Mapped to inverter/battery retrofit risks and installer-quote warning signs. |
| Solar.com / EcoFlow direct-answer question pattern | H2-01, H2-02, H2-03 | ✅ Answered immediately, then qualified with SAJ product routing. |

---

## Phase 1 Completion Checklist

- [x] `topic-card.md` Outline Sketch read and candidates extracted
- [x] `benchmark-candidates.md` H2 patterns read and candidates extracted
- [x] `benchmarks/<source>-extraction.md` actual H2s read and candidates extracted
- [x] `intent-research.md` read and candidate pool extracted
- [x] `content-type-library.md` read and exemplar patterns extracted
- [x] Upstream Research Reference completed
- [x] Upstream gap log completed (or explicitly empty)
- [x] All user-provided external H2s reviewed
- [x] Failure log completed (or explicitly empty)
- [x] 7:3 rewrite applied to all kept candidates
- [x] Final H2s approved by operator before skeleton section contracts

---

## Output Handoff

This strategy feeds directly into `skeleton.md` section contracts. Each final H2 must be embedded as the section heading in the corresponding contract.

- [x] All H2s are questions
- [x] Each H2 has documented 70% SEO base + 30% hook
- [x] Each H2 has voice lens + format + AIO answer type assigned
- [x] Path C / all-in-one ESS coverage confirmed (if applicable)
- [x] Rhythm audit passed
- [x] Research Execution Log proves Phase 1 was actually executed
