---
name: search-toolbox
description: "Use when: (1) choosing which search, scrape, or browser tool to use for a task, (2) a primary search or scrape returns empty or incomplete, (3) verifying a claim across multiple independent backends, (4) deciding fallback order when a tool fails. Enforces the mandatory Apify-First rule for all search, external fact verification, competitor research, industry rule checks, and material gathering, combined with Scrapling, Scrapy, Crawl4AI, Firecrawl, Playwright real Chrome, and Computer Use."
user-invocable: false
compatibility: Requires Apify (via scripts/apify_research.py and/or mcp__apify__*) as the mandatory primary entry point, plus Crawl4AI, Scrapling, Firecrawl, You.com, Tavily, Exa, Playwright real Chrome, and agent-reach where needed as supporting/combinatorial tools.
allowed-tools:
  - Bash
  - Read
  - WebSearch
  - WebFetch
---

## Purpose

Use when: (1) choosing which search, scrape, or browser tool to use for a task, (2) a primary search or scrape returns empty or incomplete, (3) verifying a claim across multiple independent backends, (4) deciding fallback order when a tool fails.

This skill enforces the **Apify-First Search & External Information Iron Law** across the entire B2B SEO Agent System.

# Search Toolbox (Apify-First Iron Law)

## 1. Mandatory Apify-First Principle (铁律)

Whenever any workflow step requires **search, external fact verification, competitor research, industry rule confirmation, SERP/PAA harvesting, or material gathering**, **Apify MUST be used first**.

### Credentials & Entry Point
- Three rotating monthly Apify API tokens are pre-configured in `.env.apify.local` (and `~/.config/b2b-seo-agent/apify.env`) as `APIFY_TOKEN`, `APIFY_TOKEN_FALLBACK_1`, and `APIFY_TOKEN_FALLBACK_2`.
- Tokens are rotated monthly (purchased via low-cost monthly plans); **do not question token rotation and do not throttle or avoid Actor calls to "save money"** — unused monthly quota expires anyway.
- **Primary CLI / Script Entry** (always available, auto-loads `.env.apify.local` and `~/.config/b2b-seo-agent/apify.env` with N-slot automatic failover and persistent token management):
  ```bash
  # Check all slots & remaining monthly USD quota:
  python3 scripts/apify_research.py check
  # First-time setup or full replacement of persistent Apify token pool (writes 0600 to local & global env):
  python3 scripts/apify_research.py set-tokens <apify_api_...> [<apify_api_...>]
  # Mid-workflow hot-swap: prepend new token(s) to Slot #1 and prune dead/exhausted tokens:
  python3 scripts/apify_research.py add-token <apify_api_...> --prepend --prune-dead
  # Actor discovery, schema inspection, and execution:
  python3 scripts/apify_research.py discover "<keyword>" --limit 8 --output .scratch/apify/candidates.json
  python3 scripts/apify_research.py schema "<username/actor-name>" --output .scratch/apify/schema.json
  python3 scripts/apify_research.py run "<search query or URL>" --max-results 5 --output .scratch/apify/result.json
  python3 scripts/apify_research.py run "<URL>" --browser --output .scratch/apify/rendered.json
  python3 scripts/apify_research.py run --actor "<username/actor-name>" --input-json '<json>' --output .scratch/apify/custom.json
  ```
- **Native MCP Entry** (when loaded in the session): `mcp__apify__search_actors`, `mcp__apify__fetch_actor_details`, `mcp__apify__call_actor`, `mcp__apify__get_dataset_items`, `mcp__apify__apify__rag_web_browser`.

### Apify Broken → Fix It Until It Works (修到能用，绝不绕开)
You are **strictly forbidden** from falling back to ordinary search without troubleshooting Apify first, or from skipping search / reducing research depth / declaring "unable to find" because a first Apify call failed.

When an Apify call fails or returns empty, actively diagnose and fix:
1. **API Token configuration**: run `python3 scripts/apify_research.py check` to verify slot authentication; switch slots if one is exhausted or expired.
2. **Actor selection**: if `apify/rag-web-browser` is not suited for a platform (e.g., Google SERP/PAA, Reddit, Alibaba, 1688, YouTube, LinkedIn), run `discover` to find a dedicated Actor.
3. **Actor parameters & input schema**: run `schema <actor>` to inspect the exact required fields before calling `--input-json`.
4. **Dataset & output parsing**: inspect the raw dataset JSON (`defaultDatasetId`), check `crawl.httpStatusCode`, detect anti-bot challenge pages, and read the right fields.
5. **Request format, permissions, network, page rules, timeout, rate limit**: switch `--browser` (`browser-playwright`) on for JS-rendered pages, increase timeout/memory, or adjust concurrency.

### Combinatorial Escalation & Never Accepting "Not Found" Lightly
If a target website restricts a specific crawler, Actor, or fetch method, **do not stop**. Combine Apify with supporting extraction tools:
- **Apify Actors** (primary search & platform scrapers)
- **Playwright Real Chrome** (`scripts/extract_google_paa.py` with persistent profile)
- **Scrapling** (`scrapling.fetch`, `scrapling.stealthy_fetch`)
- **Scrapy / local Python extractors**
- **Crawl4AI** (`crawl4ai.crawl_url`, `crawl4ai.deep_crawl`)
- **Firecrawl** (`firecrawl_scrape`, `firecrawl_search`)
- **Computer Use** / authenticated browser sessions
- **You.com / Tavily / Exa** (cross-index verification alongside Apify)

Never conclude "no data", "cannot find", or "unable to confirm" merely because one crawler was blocked, one page failed, or one request timed out. Actively pivot across:
```text
不同关键词 → 不同页面 → 不同数据源 → 不同 Actor → 不同抓取方式 → 不同技术路径
```
Only after exhausting multiple queries, sources, Actors, and extraction paths may a bounded gap be recorded.

---

## 2. Quick Routing Reference by Task Type

### Search the web / SERP / Competitor Research
```text
Apify (scripts/apify_research.py run / mcp__apify__apify__rag_web_browser / Google Search Actor)
  → repair Actor/params/browser-mode if needed
  → cross-check with You.com / Tavily / Exa / WebSearch for multi-index verification
```

### Scrape a URL
```text
Apify (scripts/apify_research.py run "<URL>" [--browser] or specialized Actor)
  → Scrapling (stealthy_fetch) / Crawl4AI (crawl_url) / Firecrawl (firecrawl_scrape)
  → Playwright real Chrome / Computer Use
```

### Verify a claim (2-source minimum)
```text
Source 1: Apify search + full-page Actor extraction of primary authoritative URL
Source 2: Independent index (Exa / Tavily / You.com) + full-page extraction (Apify / Crawl4AI / Scrapling / Firecrawl)
```

### Find real buyer questions & intent (`/article-intent-research`)
```text
Apify Google Search / Reddit / Forum / Social Actors + scripts/extract_google_paa.py (Playwright real Chrome)
  → agent-reach platforms (Reddit / LinkedIn / 微信公众号 / B站 / YouTube)
  → You.com / Tavily / Exa cross-check
```

### Find visual material candidates (`/article-visual` & `visual-material-hunt`)
```text
Apify specialized Actors (Google Images, Alibaba, 1688, Pinterest, Instagram, YouTube)
  → Scrapling stealth / Crawl4AI / Firecrawl
  → Playwright real Chrome / authenticated browser state
```

---

## 3. Per-Workflow-Stage Assignments

| Stage | Task Type | Primary Entry (Mandatory) | Combinatorial / Secondary Support |
|---|---|---|---|
| `/profile-discover` & `/profile-research-deep` | Competitor & industry deep research | `scripts/apify_research.py` (`rag-web-browser` + specialized Actors) | Crawl4AI / Firecrawl / Scrapling / Exa / You.com |
| `/article-cluster` | SERP & competitor gap analysis | Apify Google SERP / Web Browser Actor | You.com + Tavily + Exa cross-check |
| `/article-intent-research` | Live PAA, Autocomplete, Reddit/forum intent | Apify Actors + `scripts/extract_google_paa.py` (real Chrome) | `agent-reach` Reddit/B站/微信 + Tavily/Exa |
| `/article-benchmark` | Best-in-class content discovery | Apify search + Actor discovery | Exa semantic search + You.com + Tavily |
| `/article-benchmark-extract` | Full-text benchmark extraction | Apify (`--browser` when needed) | Crawl4AI → Scrapling → Firecrawl → Jina |
| `/article-evidence-opinions` | Verify technical/regulatory claims (2-source min) | Apify primary extraction + 2nd independent index | Exa / Tavily / You.com + Crawl4AI / Scrapling / Firecrawl |
| `/article-visual` | External visual asset hunting | Apify platform Actors (Alibaba/1688/Images) | Scrapling stealth → Playwright real Chrome |
| `/article-truth-qa` | Strict external fact & safety verification | Apify authoritative source extraction | Independent 2nd backend (Exa / Tavily / Firecrawl) |

---

## 4. Complete Tool Inventory & Fallback Chains

- Detailed tool invocation names and parameters: `references/tool-inventory.md`
- Step-by-step repair and multi-path escalation chains: `references/fallback-chains.md`

## Instructions

1. Run or verify Apify first (`scripts/apify_research.py` or `mcp__apify__*`).
2. If an Apify call fails or returns thin/blocked data, follow the 6-step repair sequence (Token slot → Actor choice → Schema/params → Dataset check → Browser/timeout mode → Combinatorial tool) before switching tools.
3. For factual verification, always confirm across at least 2 independent sources.

## Examples

### Example 1: Apify-First Competitor & Spec Research
输入: `/search-toolbox "UL 1741 SB hybrid inverter rapid shutdown requirement"`
输出: `Executed scripts/apify_research.py with apify/rag-web-browser, cross-checked authoritative UL/NREL documents via second index, and verified 2 independent sources.`

## Guardrails

- **Apify First, Repair Before Bypass**: Never skip Apify or downgrade to shallow search without diagnosing and fixing the Apify call first.
- **No Fake "Not Found"**: Never report a fact or source as missing until you have pivoted across different keywords, pages, data sources, Actors, and extraction methods.
- **Never Leak Tokens**: Never print raw `apify_api_...` tokens into markdown artifacts or commit `.env.apify.local`.
