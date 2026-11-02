---
name: article-title
description: "Use when: the draft is approved and you need to generate, score, and select the H1 article title and SEO title tag for a B2B article before publishing. Produces spontaneous, non-quota title candidates with a scored recommendation, optimized for SERP click-through, forward pull, and AIO citation under a performance-first, truth-bounded doctrine."
argument-hint: '[content-workspace/project-slug] [article-slug]'
user-invocable: true

allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - WebSearch
  - WebFetch
  - Agent
  - mcp__you__*
  - mcp__tavily__*
  - mcp__exa__*
  - mcp__crawl4ai__*
  - mcp__firecrawl__*
  - mcp__plugin_playwright_playwright__*
  - mcp__apify__*
  - mcp__agent-reach__*
  - mcp__douyin__*
  - mcp__linkedin__*
  - mcp__mcp-server-chart__*
---

# /article-title

## Purpose

Generate the H1 article title and the SEO `<title>` tag for a B2B article by producing **spontaneous, non-quota candidates**: as many as the article naturally supports, stopping when the next candidate would only repeat an existing click mechanism. This is a **dedicated title strategy** stage — titles are too important to CTR and AIO citation to be written as an afterthought inside `/article-publish-pack`.

This skill optimizes for **search-intent match, SERP click-through, and AIO citability**. CTR is the gate — a title nobody clicks is dead — so every title carries a genuine CTR hook (number, loss, reframe, info-gap, list, comparison, timeliness). But trust is the floor: hooks are built from real facts in the draft, never invented, and the title must pass voice-and-humanization. The goal is a title that earns the click *and* keeps the reader, not emotional clickbait that bounces.

## Methodology Credit

The structure of this skill — data-backed style rules, spontaneous candidate generation, a scored checklist, and a hard fact-boundary rule — is adapted from the qiaomu-xinzhiyuan-title skill (joeseesun/qiaomu-xinzhiyuan-title), which extracted title rules from a 2688-article corpus, plus self-media prompt patterns for click-mechanism analysis (structure, keyword, emotional trigger, value promise, SEO base). The methodology is reused; the style rules themselves are rewritten for English B2B SEO (the original is Chinese AI-media for WeChat — a different language, platform, reader, and goal function). See `references/title-style.md` for the B2B-specific rules.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before title work, verify:
- `project-profile.md` exists and `state.json` indicates `lockedProfile: true`.
- `articles/<article-slug>/draft.md` exists (the draft must be written so the title reflects actual content, not a presupposed angle).
- `articles/<article-slug>/skeleton.md` and `h2-heading-strategy.md` exist (the title must align with the approved H2 sequence and 7:3 heading strategy).

### Handoff Read (MANDATORY — complete before generating candidates)

| Upstream File | Extract | Used For |
|---|---|---|
| `topic-card.md` | Primary keyword, search intent, reader promise | Seeding the keyword-first title spine |
| `intent-research.md` | Top live PAA questions, intent clusters | Matching the title to real searcher questions |
| `h2-heading-strategy.md` | The 7:3 H2 plan + micro-tension hook vocabulary | Title must not out-promise or contradict the H2s |
| `skeleton.md` | Article scope and section functions | Title scope = article scope, no overclaim |
| `draft.md` | Actual claims, numbers, and conclusions | Hard facts the title may reference |
| `project-profile.md` §3/§7 | Buyer persona, benchmark/voice policy | Title register (trustworthy vs. punchy) must fit the buyer |

## Skills to Load

- `voice-and-humanization` — the title must pass the same anti-AI-writing, anti-hype filters as the body. No hype verbs (`unleash`, `revolutionize`, `skyrocket`, etc. — see the avoid list in `references/title-style.md`).
- `benchmark-led-answerability` — the title must promise an answer the body actually delivers.

## Phase 0 — Plan Preview (output first, do NOT execute)

Before generating candidates, present:

1. **Upstream Consumption Report**: what was read from each handoff file.
2. **Primary Keyword + Intent**: the exact primary keyword and the searcher's dominant intent (informational / comparison / cost / process / risk).
3. **Title Spine**: the keyword-first spine the candidates will share (e.g. `Can You Use Solar Panels Without a Battery?`).
4. **Fact Inventory**: every hard number, spec, or ranking the title is *allowed* to reference (drawn from the draft). Nothing outside this list may appear in a title.
5. **Candidate Plan**: which distinct click mechanisms the article naturally supports (number / loss / reframe / info-gap / list / comparison / timeliness / positive-vs-negative stimulus). Do not plan a fixed candidate count.

Output the plan, then use the unified stop language and wait for explicit approval.

---

## Phase 1 — Generate Spontaneous Candidate Variants (no quota)

All candidates share the keyword-first spine and respect the 40–60 / 50–60 character targets in `references/title-style.md`. **Every serious candidate must carry a distinct click mechanism** from the hook library (number / loss / reframe / info-gap / list / comparison / timeliness / positive stimulus / negative stimulus). Do **not** generate titles to hit a quota. Generate until the set has covered the distinct click mechanisms the article naturally supports, then stop. If the next candidate is only a weaker wording of an existing mechanism, drop it.

For each candidate, record:

| Field | What to capture |
|---|---|
| Click mechanism | What makes a reader click: loss, curiosity gap, number specificity, comparison, future cost, positive/negative stimulus |
| Curiosity gap | What unresolved question makes the reader continue? |
| Emotional trigger | Loss aversion, self-protection, money saved, future regret, status/confidence, relief |
| Value promise | What concrete payoff the reader expects after clicking |
| SEO base | Primary keyword / PAA question / entity alignment |
| Fact boundary | Which draft/profile/evidence fact supports the hook; if none, reject or soften |

Common candidate families (use only when natural):

| Variant | CTR hook used | When to use |
|---|---|---|
| **CTR-optimized (default)** | number / reframe / list | Most articles. One strong hook + keyword + fact. |
| **Number-anchored** | number (specific or counter-intuitive) | Draft has a true spec, count, or surprising metric. |
| **Decision/comparison** | comparison | Buyer's guide or X-vs-Y. |
| **Risk/mistake** | loss / risk | Mistakes or risk-avoidance articles. |
| **Reframe/contrarian** | reframe | Article overturns a common assumption. |
| **Information-gap** | info-gap | Article delivers insider/authority knowledge. |
| **Positive stimulus** | gain / speed / certainty | Article offers a strong upside the reader wants. |
| **Negative stimulus** | missed opportunity / future bill / lock-out | Article reveals a cost of not reading. |
| **Restrained/E-E-A-T** | (none — Level 1) | Trust-sensitive technical buyer only. |
| **AIO-citable** | (declarative, hook optional) | AIO/featured-snippet capture priority. |

Default recommendation = **CTR-optimized (Level 2)** or **truth-bounded high-tension (Level 3)** when the article's thesis is risk/loss. Drop to Restrained/E-E-A-T (Level 1) only when the buyer distrusts hooks. Hooks must be built from the Fact Inventory; never invent a number, loss claim, or "what X won't tell you" the article doesn't deliver.

## Phase 2 — Model-Driven Evaluation (No Mechanical Regex Scoring)

Evaluate each candidate directly using model judgment against the principles in `references/title-style.md` (never use a hardcoded character-count or regex scoring script, as optimal title length and tension vary by search intent, industry, and SERP competition):

- **Search-Intent & Keyword Spine**: Does it front-load or naturally anchor the primary keyword and match the dominant SERP intent?
- **Click Mechanism & Curiosity Gap**: Does it carry one clean, unmistakable CTR driver (loss frame, specific number, contrarian reframe, comparison, or decision hook) without stacking multiple hooks into clickbait?
- **B2B Buying Committee Resonance**: Would both a technical specifier (engineer/architect) and a commercial approver (procurement/owner) respect and click this title?
- **Trust Register & Fact Boundary**: Zero hype words, and every number or claim traces strictly to the Fact Inventory.
- **Qualitative Verdict**: Assign `strong` / `usable` / `weak` with a 1-sentence editorial rationale explaining why a real B2B buyer on Google SERP would click this over the top 5 competitors.

## Phase 3 — Recommend and Hand Off

1. Recommend one title, with the score and the reason it beat the alternatives.
2. Provide the matching SEO `<title>` tag (may differ slightly from H1 — SEO title can add the brand suffix and sit in the 50–60 char SERP band).
3. State the **fact boundary**: which claims in the title are sourced from the draft, and confirm none are presupposed.
4. Write `articles/<article-slug>/title-options.md` with all candidates, scores, and the recommendation, so the choice is auditable.

## Hard Rules

- **Every title carries a CTR hook** (default), built from a real fact. "No hook" is allowed only at Level 1 for trust-sensitive buyers. A hook-less Level 2 title is a failure — go back and add a genuine hook.
- **One hook, not a stack.** A number hook already counts as the tension element. Do not pile a loss hook AND a reframe AND a micro-tension word into one title — that is hype, and it fails voice-and-humanization.
- **Hooks must be true.** `5 Things to Check` requires 5 things in the article. `What Installers Won't Tell You` requires insider info. `98% Uptime` requires that number in the Fact Inventory. A false hook earns the click and the bounce — worse than no hook.
- **Do not invent facts.** No specific number, spec, price, ranking, "first", "best", or named competitor unless it is in the Fact Inventory (sourced from the draft or locked profile).
- **Keyword-first.** The primary keyword appears in every candidate, front-loaded when natural.
- **Trust is the floor.** The title earns the click AND keeps the reader. No hype words (the avoid list in `references/title-style.md`). The title must pass voice-and-humanization and Reader QA.
- **Do not out-promise the H2s.** If the title implies a comparison or list the article doesn't deliver, rewrite the title, not the article.
- **Length**: H1 40–60 chars preferred (24–42 is the tight band for questions); SEO `<title>` 50–60 chars to fit SERP display.
- **Anti-Presupposition**: titles are generated *after* the draft exists, so claims are grounded. Never generate titles before the draft.

## Output

Create `articles/<article-slug>/title-options.md` using `templates/title-options.md`.

Update `state.json`: no stage advance (this runs inside `/article-publish-pack`); set `lastUpdated` and record `titleOptions: articles/<article-slug>/title-options.md`.

## Examples

### Example 1: Standard question default
Input: draft on solar-without-a-battery, primary keyword "solar without a battery"
Output: `Can You Use Solar Panels Without a Battery? (2026 Buyer's Guide)` — score 8.1, recommended, fact boundary: "2026" sourced from draft currency; "buyer's guide" matches article type.

### Example 2: Restrained/E-E-A-T for a technical buyer
Input: spec-heavy inverter article
Output: `SAJ Hybrid Inverters Without a Battery: What Works and What Doesn't` — score 7.6, recommended over a punchier variant because the buyer is an installer who distrusts hype.

## Guardrails

- **No clickbait**: if a candidate would not pass Reader QA, drop it before scoring.
- **One hook max**: a B2B title carries one tension element, not a stack.
- **Brand suffix only in SEO title**: H1 stays clean; `<title>` appends the project's canonical separator and entity name per profile (e.g., ` — ArchMetal` on `archmetal-screens.example.com` per SEOPress `%%post_title%% %%sep%% %%sitetitle%%`, or ` | Brand` when specified).
- **AIO-first when relevant**: for definitional intent, prefer the AIO-citable declarative form.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval before handing the selected title to `/article-publish-pack`.
