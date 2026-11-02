# Content-Type Library

**Article:** `solar-without-a-battery`  
**Project:** `sunriver-inverter`  
**Stage:** `/article-benchmark`  
**Date:** 2026-06-24

---

## Library Search Plan

| Category | Search strategy | Tool route | Target entries |
|---|---|---|---|
| Same-industry direct | Google search for "solar without battery", "should I install solar battery now or later" | search-toolbox → tavily / you-search / browser | 2–3 |
| Same-industry adjacent | Search for home backup power / generator buyer guides that map to solar system configuration decisions | search-toolbox → tavily / you-search | 1–2 |
| Cross-industry parallel | Search for risk-avoidance buyer's guides and contrarian "don't do this" explainers in unrelated B2C/B2B niches | search-toolbox → tavily / you-search / agent-reach for Chinese long-form | 2–3 |
| Unrelated-domain craft | Find a contrarian rant-with-lessons piece in a completely different domain (AI, productivity, tech) to borrow voice arc | agent-reach / tavily for 人人都是产品经理 mirror of WeChat posts | 1 |
| Chinese social long-form | Search WeChat public accounts / 人人都是产品经理 for contrarian Chinese-language explainers; use mirror due to WeChat walls | agent-reach / tavily | 1 |
| Non-text formats | YouTube search for solar no-battery explainer titles | search-toolbox → you-search | 0–1 |

---

## Library Entries

| ID | Category | Source / URL | Content type | Why relevant | Structural pattern | Prose craft notes | Question intent answered | Transmutation notes |
|---|---|---|---|---|---|---|---|---|
| LIB-01 | same-industry-direct | https://www.energysage.com/energy-storage/should-i-install-a-solar-battery-now-or-add-it-later/ | Solar-industry direct-answer buyer's guide | Matches primary keyword intent almost exactly; builds a decision framework around incentives, retrofit complexity, and storage-ready design. | Question-as-title → key-takeaways box → decision-chain H2s: Why do you want a battery? → Pricing/incentives → Installation costs → Retrofit integration → Bottom line → installer instruction. | Short paragraphs, one data point per section; honest "it depends" tone; inline definitions for net metering, TOU rates, AC/DC coupling. | Now-vs-later timing, retrofit complexity, storage-ready design. | Borrow retrofit-trap argument and "storage-ready" framing; apply to SAJ hybrid inverters and battery-later expansion. |
| LIB-03 | same-industry-adjacent | https://www.thisoldhouse.com/electrical/generator-buying-guide | Cross-industry buyer's guide (home backup power) | Homeowner audience, high-stakes purchase, taxonomy-heavy structure maps cleanly to solar system configurations. | Taxonomy-first H2s: Types → Power needs → Operation → Fuel → Cost → AC vs. DC → Other features. | Magazine-style authority via expert attribution; "Pro Tip" callouts; reference tables. | Path taxonomy, power/backup needs, safety checklist. | Replace generator types with inverter/system types; keep power-requirement table and safety checklist formats. |
| LIB-04 | cross-industry-parallel | https://jingsourcing.com/is-alibaba-safe-legit | Cross-industry risk-avoidance listicle | Excellent model for risk-first buyer's guide: each section debunks a common assumption and replaces it with a practical screening rule. | Numbered risk list intro → each H2 debunks an assumption → real-case references → screening checklist → honest conclusion. | Direct, slightly informal B2B voice; bullet-heavy but balanced; no fearmongering. | Red-flag identification, assumption debunking, quote screening. | Map Alibaba supplier risks to solar battery/retrofit risks: meaningless "battery-ready" labels, hidden inverter-swap costs, compatibility claims. |
| LIB-05 | cross-industry-parallel | https://cxl.com/blog/12-ab-split-testing-mistakes-i-see-businesses-make-all-the-time | Cross-industry mistakes/opinion piece | Strong practitioner voice and numbered-mistakes format transmutable into "solar buyer mistakes." | Numbered mistakes anchored in TOC → what people do wrong → why it costs them → what to do instead → real example. | Expert-first voice; short punchy paragraphs; bold judgment; willing to say unpopular things. | Buyer mistakes, hidden costs, expert warnings. | Convert A/B testing mistakes into solar-buying mistakes: battery-first pressure, incompatible inverter assumptions, waiting too long for prices to drop. |
| LIB-06 | unrelated-domain-craft | https://www.woshipm.com/ai/6280845.html (mirror of WeChat public account 饼干哥哥AGI) | Contrarian / rant-with-lessons (AI workflow domain) | Closest match to project profile's "conversational, contrarian, rant-with-lessons" voice; demonstrates provocation → failure → lesson pivot. | Provocative claim title → bold evidence-backed opener → walk through failed/common solution → real client case → lesson pivot: old skill is dead, new skill is higher-level architecture. | Casual first-person narrator; exclamations/rhetorical questions; screenshots as proof; tiered bronze/gold headings. | Contrarian hook, demonstration arc, lesson pivot, voice calibration. | Use arc for battery question: "Everyone says you need a battery. I say not yet. Here's what actually happens when you add one later." |
| LIB-07 | chinese-social | https://www.woshipm.com/ai/6280845.html (人人都是产品经理 mirror of 饼干哥哥AGI WeChat public account) | Chinese-language contrarian long-form | WeChat public pages were walled; mirror preserved the long-form voice and contradiction structure useful for voice calibration. | Same as LIB-06. | Casual, first-person, exclamatory; uses Chinese internet register; strong opinion emerges from demonstration. | Voice calibration, contrarian hook, lesson pivot. | English register only; no anti-battery bashing — keep manufacturer-credible supply-partner stance. |
| LIB-08 | non-text | — | — | No non-text source provided unique question phrasing beyond text channels. | — | — | — | Omitted from primary exemplar selection; text channels saturated the intent space. |

---

## Primary Exemplar Selection

Select exactly 3 exemplars from the library. Ensure they represent at least two distinct problem-solving models.

| # | Library ID | Source / URL | Selected model | Why selected | Question intents covered |
|---|---|---|---|---|---|
| 1 | LIB-01 | EnergySage — "Should I install a solar battery now or later?" | Decision framework / buyer's guide | Strongest structural fit for the solar no-battery question; provides now-vs-later ladder and retrofit complexity framing. | Now-vs-later timing, retrofit economics, storage-ready design, installer question. |
| 2 | LIB-06 | 饼干哥哥AGI / woshipm mirror — "劝退：n8n等 AI工作流不要学了，已经过时了" | Contrarian / rant-with-lessons | Project profile explicitly requested contrarian/rant-with-lessons voice; this piece demonstrates provocation → proof → lesson pivot. | Contrarian opener, demonstration arc, closing reframe. |
| 3 | LIB-04 | JingSourcing — "Alibaba Safe? 8 Real Risks Beginners Face (2026)" | Risk-avoidance listicle / debunked-assumption | Best model for red-flag and debunked-assumption H2s; maps cleanly to solar buyer myths and installer-quote risks. | Red-flag catalog, assumption debunking, quote screening. |

---

## Pattern Notes (optional)

Use this section for library entries that shape the success formula but are not selected as primary exemplars.

| Library ID | Borrowable pattern | How it could transmute to this article | Risk label |
|---|---|---|---|
| LIB-03 (This Old House) | Taxonomy-first H2s + power-requirement table + safety checklist | Map generator types to inverter/system types; keep reference-table format. | Low — structure is generic enough to adapt, but avoid over-extending the generator analogy. |
| LIB-05 (CXL) | Numbered-mistakes format with what-wrong → why-costs → what-to-do-instead | Could become a standalone "solar buyer mistakes" section if H2-06 expands. | Medium — do not turn the article into a listicle; keep within the decision-ladder arc. |

---

## Handoff Summary

- Selected primary exemplars: `LIB-01`, `LIB-06`, `LIB-04`.
- Problem-solving models represented: Decision framework / buyer's guide; Contrarian rant-with-lessons; Risk-avoidance listicle / debunked-assumption.
- Key cross-industry / unrelated-domain patterns to carry into skeleton: JingSourcing debunked-assumption H2 pattern; 饼干哥哥AGI contradiction hook + lesson pivot; This Old House taxonomy table (optional).
- Any category searched but not represented: Non-text — text search channels already saturated the question space; no unique non-text phrasing was found.
