---
name: article-benchmark
description: "Use when: a topic card and intent-research.md are ready and you need to build a broad content-type library, then select the 3 primary exemplars for success-formula extraction."
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

# /article-benchmark

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before benchmark work, verify:
- `project-profile.md` exists, `project-profile.json` exists, `state.json` indicates `lockedProfile: true`
- `articles/<article-slug>/topic-card.md` exists
- `articles/<article-slug>/intent-research.md` exists

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `articles/<article-slug>/topic-card.md` | All 14 fields (primary keyword, search intent, SERP landscape, recommended content format, benchmark article URL, funnel stage, content pillar) plus scoring, evidence notes, benchmark prep, information gain check, outline sketch, and E-E-A-T strategy | Article type classification |
| `articles/<article-slug>/intent-research.md` | Consolidated candidate pool, intent clusters, question types, handoff notes | Matching library categories to what users ask |
| `project-profile.md` §3 | Target buyers table and key buyer motivations | Matching benchmark article types to buyer decision stage |
| `project-profile.md` §6 | Competitor set | Ensuring we do NOT search competitor domains as benchmark sources |
| `project-profile.md` §7 | Benchmark Policy | Knowing which borrowable asset types are allowed and blocked |

## Purpose

Find the best content in the world to learn from — NOT competitor SERP pages. Study how great writers and content producers structure, pace, and voice answers to the same user intent across industries, domains, and formats.

This stage produces two artifacts:
1. A broad **content-type library** (`content-type-library.md`) spanning same-industry, cross-industry, unrelated-domain, Chinese social, and non-text formats.
2. **3 selected primary exemplars** (`benchmark-candidates.md`) that will receive full 21-dimension extraction in `/article-benchmark-extract`.

## Skills to Load

- `search-toolbox` — choose the right search/extraction tool per library category (**Mandatory Apify-first**: use `python3 scripts/apify_research.py` or `mcp__apify__*` as the primary entry point for searching and scraping candidate benchmarks; troubleshoot and combine with Crawl4AI/Firecrawl/Playwright rather than bypassing if an Actor fails).
- `benchmark-transmutation` — apply borrowable-asset rules and risk labels when assessing library entries.

## Phase 0 — Plan Preview

Before any search, present a plan:

1. **Upstream Consumption Report**: confirm what was read from `topic-card.md` and `intent-research.md`.
2. **Article Type Classification**: proposed type from the 10-type taxonomy, with justification.
3. **Library Search Plan**: which categories will be searched, with sample queries and tool routes.
4. **Success Criteria**: what "good library" and "good selected 3" look like.
5. **Tool Strategy**: which research channels will be used per category.

Output the plan, then use the unified stop language and wait for explicit approval.

## Instructions

**Main context work**: read upstream files, classify the article type, define the library search plan, validate library entries, select the 3 primary exemplars.

**Subagent-appropriate work**: search each library category in parallel. Let each subagent use `search-toolbox` to choose tools and fallbacks.

---

### Phase 1 — Article Type Classification

Based on the topic-card and locked profile, classify this article into one of 10 types:

| # | Type | Core Job | Typical Benchmark Sources |
|---|---|---|---|
| 1 | Definition / Concept Guide | Help users understand what something is, how it works, its variants | Investopedia, Moz, HubSpot, Metal Supermarkets |
| 2 | Application Guide | Help users understand how a product applies across different scenarios | ArchDaily, Dezeen, Forms+Surfaces, Armstrong Ceilings |
| 3 | Buyer's Guide / Procurement Guide | Help users buy right, select right, ask suppliers the right questions | Thomasnet, Xometry, Protolabs, JingSourcing, PakFactory, EnergySage |
| 4 | Technical Deep-Dive | Explain a technical problem; prove you genuinely understand it | Xometry, Protolabs, Fictiv, The Fabricator, Metal Supermarkets, Fractory |
| 5 | Comparison / X vs Y | Help users choose between options | NerdWallet, EnergySage, G2, Capterra, Wirecutter |
| 6 | Cost Guide | Help users understand what drives price, not give a fixed number | EnergySage, NerdWallet, The Zebra, This Old House, Xometry |
| 7 | Process Walkthrough / How-To | Show users how a project progresses; reduce uncertainty | Protolabs, Xometry, SendCutSend, PakFactory, iFixit |
| 8 | Case Study / Project Story | Prove you can solve a specific problem with real project evidence | ArchDaily, Dezeen, Zahner, Banker Wire, Cambridge Architectural, BŌK Modern |
| 9 | Mistakes / Risk-Avoidance | Make users aware of the cost of wrong choices; show how to avoid them | JingSourcing, CXL, EnergySage, This Old House, Protolabs |
| 10 | Opinion / Thought Leadership | Propose an industry viewpoint that changes how the reader sees the problem | Animalz, CXL, Intercom, Zahner, Dezeen opinion pieces |

---

### Phase 2 — Content-Type Library Build

Search for candidate content across the `config/workflow-spec.yaml` `content_type_library_categories` (6) categories below. Not every category needs a final entry, but every category must be searched and logged.

| Category | What to find | Why it matters |
|---|---|---|
| Same-industry direct | Same topic, same industry | Proves the baseline answer shape and expected proof types |
| Same-industry adjacent | Same industry, adjacent topic or format | Supplies angle variation and unexpected structures |
| Cross-industry parallel | Same buyer intent in a different industry | Imports proven decision frameworks from mature markets |
| Unrelated-domain craft | High-quality publications outside the industry | Borrowable opener hooks, pacing, and voice moves |
| Chinese social long-form | Xiaohongshu / WeChat posts (if relevant) | Captures Chinese-market question framing and proof styles |
| Non-text formats | Video, podcast, infographic, interactive tool (if relevant) | Reveals how the same intent is answered without long-form prose |

For each library entry, record: category, source, URL, content type, why relevant, structural pattern, prose craft notes, question-intent it answers, and transmutation notes. Use `templates/content-type-library.md`.

**Library size guardrail:** cap each category at 2–3 entries and the total library at ~12 entries to avoid dilution.

---

### Phase 3 — Select Primary Exemplars

From the library, select exactly `config/workflow-spec.yaml` `benchmark_selected_count` (3) primary exemplars. The final 3 must:

- Cover at least two distinct problem-solving models:
  - **Logical Command** — step-by-step imperative instructions
  - **Strategic Workflow** — phased narrative with why-before-how teaching
  - **Risk-Avoidance Listicle** — debunked assumptions and red-flag catalogs
  - **Contrarian / Rant-with-Lessons** — provocation → teardown → demonstration → reframe
  - **Comparison / Decision Framework** — structured option comparison
- Map to different question-intent clusters from `intent-research.md`.
- Not be direct competitors with thin product listings.

Record the selected exemplars in `templates/benchmark-candidates.md`.

---

## Output

Create:
- `articles/<article-slug>/content-type-library.md`
- `articles/<article-slug>/benchmark-candidates.md`

Update `state.json`: `currentStage: article-benchmark`, `nextCommand: /article-benchmark-extract`, `benchmarkStatus: awaiting-user-selection`, `contentTypeLibrary: articles/<article-slug>/content-type-library.md`.

## Examples

### Example 1: Building a content-type library
输入: `/article-benchmark content-workspace/steel-screen`
输出: `content-type-library.md created with 10 entries across 6 categories; benchmark-candidates.md records 3 selected exemplars.`

## Guardrails

- **No Competitor SERP Cloning**: do not select direct competitors with thin product listings.
- **Metrics Verification**: confirm each candidate ranks high or exhibits outstanding authority on technical subjects.
- **Multi-Model Mix**: the final 3 selected benchmarks must cover at least two distinct problem-solving models.
- **Library entries are not benchmarks**: only the selected 3 receive full 21-dimension extraction.

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

Present the library and selected 3, then wait for explicit approval before `/article-benchmark-extract`.
