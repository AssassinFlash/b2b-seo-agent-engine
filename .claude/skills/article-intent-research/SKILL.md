---
name: article-intent-research
description: "Use when: a topic card is locked and you need to build a verifiable search-intent/H2 candidate pool from live channels before selecting content-type benchmarks."
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

# /article-intent-research

## Purpose

Build the **"what users ask"** dimension for an article. Produce a durable `intent-research.md` artifact containing a verifiable pool of real user questions and search-intent candidates before any H2 design or benchmark selection happens.

This skill does **not** write final H2s, section contracts, or benchmark analysis. It only extracts, consolidates, and maps intent.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before intent research, verify:
- `project-profile.md` exists and `state.json` indicates `lockedProfile: true`
- `articles/<article-slug>/topic-card.md` exists with an approved Outline Sketch

If the locked-profile gate fails, stop and route to `/profile-lock`.

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `project-profile.md` §2/§5/§10 | Product scope, target buyers, red lines, voice | Gating and filtering candidates |
| `topic-card.md` | Primary keyword, search intent, Outline Sketch, reader promise, E-E-A-T strategy | Seeding the candidate pool and intent clusters |
| `templates/intent-research.md` | Research execution log schema, consolidated pool table, handoff sections | Producing the artifact |

## Skills to Load

- `search-toolbox` — read the per-workflow-stage assignments and choose the right tool/fallback chain for each channel.
- `evidence-policy` — to label candidate reliability where a candidate might become a future claim.

## Phase 0 — Plan Preview

Before extracting anything, present:

1. **Upstream Consumption Report**: confirm exactly what was read from `topic-card.md` and `project-profile.md`.
2. **Search Intent Clusters**: list the major intent clusters (e.g., definition, comparison, cost/risk, process) derived from the topic card.
3. **Channel Plan**: which channels will be extracted, target queries, tools, and minimum counts.
4. **Chinese / Non-Text Decision**: whether Chinese social or non-text sources are relevant for this topic.
5. **Subagent Plan**: which channels will run in parallel subagents.
6. **Success Criteria**: what "candidate pool complete" looks like.

Use the unified stop language. Wait for explicit approval before Phase 1.

## Instructions

**Main context**: orchestrate the research plan, validate extraction evidence, synthesize the consolidated pool, and write `intent-research.md`.

**Subagent-appropriate work**: spawn parallel channel subagents for Google PAA, Google Autocomplete, Reddit/English forums, Chinese social (if relevant), and non-text sources (if relevant). Each subagent returns extracted candidates with evidence.

**No inferred candidates.** A candidate can only be tagged as coming from a live channel if it was actually extracted from that source.

---

### Phase 1 — Research Plan Approval

Present target queries for each channel. The minimum number of required live channels is `config/workflow-spec.yaml` `intent_research_minimum_channels` (3), covering Google PAA, Google Autocomplete, and Reddit/English forums.

- **Google PAA**: ≥ 3 queries.
- **Google Autocomplete**: ≥ 3 queries.
- **Reddit / forums**: ≥ 3 subreddits or search queries.
- **Chinese social** (if relevant): ≥ 2 queries.
- **Non-text** (if relevant): ≥ 2 queries.

Wait for operator approval or modification before any extraction.

---

### Phase 2 — Live Channel Extraction

Use `search-toolbox` to select tools. See `references/channel-playbooks.md` for detailed per-channel methods and evidence requirements.

| Channel | Minimum | Evidence required |
|---|---|---|
| Google PAA | 4 real questions | exact query URL + selector + timestamp |
| Google Autocomplete | 8 real suggestions | exact API URL + timestamp |
| Reddit / English forums | 5 real thread titles | exact search query + thread URLs + timestamp |
| Chinese social (if relevant) | 3 posts | platform + query + post URL(s) + timestamp |
| Non-text (if relevant) | 3 media titles | platform + query + media URL(s) + timestamp |

If a channel cannot meet its minimum, proceed immediately to Phase 4 Failure Logging. Do not silently reduce the minimum.

---

### Phase 3 — Candidate Pool Consolidation

Combine upstream and live-channel candidates into one master table with these columns:

| # | Consolidated candidate | Source | Extraction evidence | Intent cluster | Reader question type | Buyer intent | Priority for H2 |
|---|---|---|---|---|---|---|---|

Where:
- **Source** = `intent-research` channel name or upstream file path.
- **Extraction evidence** = URL + method + timestamp for live channels; file path + section for upstream files.
- **Reader question type** = Problem / Safety / Solution / Help / Prevention / Comparison / Cost / Trust / Process.
- **Buyer intent** = Informational / Comparison / Transactional / Risk-avoidance.
- **Priority for H2** = high / medium / low / discard.

The consolidated pool should generally contain 15+ distinct candidates. Fewer is acceptable only if documented in the Failure log.

### Phase 3.5 — Golden Keywords and User Language Bank

Extract the self-media layer from the live research: not just what people ask, but the exact language that makes people click, stop, and keep reading.

Create two additional sections in `intent-research.md`:

1. **Golden Keyword / Phrase Map** — 3-10 phrases with unusual pulling power. For each phrase, record:
   - source (PAA / Autocomplete / Reddit / comment thread / benchmark title)
   - why it matters (attention, uniqueness, demand satisfaction, timeliness)
   - search intent
   - click / dwell mechanism
   - where it should be reused (title / H2 / opener / body / FAQ)

2. **User Language Bank** — raw reader wording and objection language. For each item, record:
   - raw wording
   - source URL / channel
   - emotion (confusion, fear, skepticism, regret, greed, urgency)
   - underlying anxiety
   - reusable wording for title / H2 / opener / FAQ

Use real user language when available. Do not invent "raw user wording." If comments/forums are thin, label the row as `search-surface wording` rather than `user comment`.

### Phase 3.6 — SERP Table-Stakes Entities, Consensus Target & Incremental Gain (实体防漏网 + 同行共识靶子)

To align with Google's Information Gain patent (`US20200349181A1`) while ensuring we never miss foundational concepts that searchers expect, include two structured tables in `intent-research.md`:

1. **SERP Consensus Target (《SERP 同行套话共识靶子》)** — Using Apify to inspect the current top 5 ranking pages for the primary keyword, extract the 3–5 standard platitudes/claims that every competitor repeats in unison. For each consensus claim, define **Our Contrarian / Deeper Counter-Move**: where the consensus is incomplete, what hidden premise it ignores, or what real-world engineering/cost trap it hides.
2. **Table-Stakes vs. Incremental Entities (必含基础实体 vs 我方增量实体)** —
   - `table-stakes`: Concepts, standards, hardware categories, or baseline trade-offs covered across top-ranking pages that we MUST cover to satisfy baseline relevance.
   - `incremental`: Proprietary frameworks, hidden cost traps, specific engineering tolerances, or field failure modes that SERP pages miss.
3. **Co-Research Blind-Spot Prompt (对等共研讨论焦点)** — Explicitly list 2–3 open questions or suspect search angles for peer debate with the operator at the pause point.

---

### Phase 4 — Failure Logging

If any channel cannot meet its minimum:

1. Log the failure reason (tool error, rate limit, no results, anti-bot block, irrelevant topic).
2. State the workaround (alternative query, fallback tool, expanded search, or explicit exclusion).
3. Never silently omit the channel.

---

### Phase 5 — Intent Mapping & Handoff

Map each major intent cluster from `topic-card.md` to candidate numbers in the consolidated pool. Flag coverage gaps.

Write handoff notes for `/article-benchmark` and `/article-skeleton`:
- Top question types the content-type library should cover.
- Candidates most likely to become final H2s.
- Red-line or buyer-persona constraints.

---

## Output

Create `articles/<article-slug>/intent-research.md` using `templates/intent-research.md`.

Update `state.json`: `currentStage: article-intent-research`, `nextCommand: /article-benchmark`, `intentResearch: articles/<article-slug>/intent-research.md`.

## Examples

### Example 1: Building intent research
输入: `/article-intent-research content-workspace/steel-screen how-to-choose-a-metal-screen`
输出: `intent-research.md created with 22 candidates from PAA, Autocomplete, Reddit, and the topic-card outline.`

## Guardrails

- **No invented candidates**: inferred or "style" candidates are prohibited.
- **Silent omission is a blocking error**: every channel must be attempted or explicitly logged as failed.
- **Minimums are minimums**: do not reduce them without operator approval.
- **Apify-First Iron Law**: always start live channel research with Apify (`scripts/apify_research.py` / `mcp__apify__*`) and `scripts/extract_google_paa.py` (real Chrome); if an Actor or query fails, repair and pivot across keywords, pages, Actors, and tools rather than bypassing or reducing depth.
- **Cross-check uncertain channels**: if one tool returns thin results, try a second independent index.

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

Wait for explicit approval before advancing to `/article-benchmark`.
