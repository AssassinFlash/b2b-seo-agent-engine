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
- **Primary CLI / Script Entry** (always available, auto-loads `.env.apify.local` and `~/.config/b2b-seo-agent/apify.env` with N-slot automatic failover, 15 built-in B2B Actor Store presets, and dynamic Actor Store schema introspection):
  ```bash
  # 1. Check all token slots & print the 15-preset B2B Actor Store matrix:
  python3 scripts/apify_research.py check
  python3 scripts/apify_research.py matrix

  # 2. Run any of the 15 verified B2B multi-angle Actor Store presets directly:
  python3 scripts/apify_research.py run --preset google-serp "custom stainless steel room divider" --output .scratch/apify/serp.json
  python3 scripts/apify_research.py run --preset reddit-search "stainless steel partition weld warping" --output .scratch/apify/reddit.json
  python3 scripts/apify_research.py run --preset reddit-fast "metal screen divider, laser cut panel installation" --output .scratch/apify/reddit-fast.json
  python3 scripts/apify_research.py run --preset youtube-search "laser cut metal screen installation" --output .scratch/apify/yt.json
  python3 scripts/apify_research.py run --preset youtube-transcript "https://www.youtube.com/watch?v=VIDEO_ID" --output .scratch/apify/yt-transcript.json
  python3 scripts/apify_research.py run --preset youtube-comments "https://www.youtube.com/watch?v=VIDEO_ID" --output .scratch/apify/yt-comments.json
  python3 scripts/apify_research.py run --preset linkedin-posts "architectural metalwork specification, PVD stainless steel" --output .scratch/apify/linkedin.json
  python3 scripts/apify_research.py run --preset google-maps-b2b "architectural metal fabricator @ Houston" --output .scratch/apify/maps-b2b.json
  python3 scripts/apify_research.py run --preset google-maps-reviews "https://www.google.com/maps/place/..." --output .scratch/apify/maps-reviews.json
  python3 scripts/apify_research.py run --preset alibaba-suppliers "316 stainless steel laser cut screen" --output .scratch/apify/alibaba.json
  python3 scripts/apify_research.py run --preset amazon-reviews "https://www.amazon.com/dp/B0..." --output .scratch/apify/amazon-failures.json
  python3 scripts/apify_research.py run --preset google-trends "metal room divider, perforated metal screen" --output .scratch/apify/trends.json

  # 3. Dynamic Actor Store Discovery + Auto-Schema Introspection (for Houzz, ArchDaily, Thomasnet, G2, Trustpilot, Pinterest, 1688, etc.):
  python3 scripts/apify_research.py discover "houzz" --limit 5 --with-schemas --output .scratch/apify/store-houzz.json
  python3 scripts/apify_research.py run --actor "<username/actor-name>" --input-json '<json-matching-compactSchema>' --output .scratch/apify/custom.json
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

## 3. The 15-Preset B2B Multi-Angle Intelligence Matrix & Per-Stage Assignments

Never treat Apify as a single generic web scraper (`rag-web-browser`). Every research stage MUST combine **at least 3 distinct Actor Store angles** (e.g., Search/SERP + Practitioner Community/Reddit/LinkedIn + Video/Transcript/Comments + Supplier/Maps/Review Teardown) so our articles capture real-world engineering friction that Google SERP pages never mention:

| Preset (`--preset`) | Verified Store Actor | B2B Intelligence Angle Unlocked | Primary Workflow Stages |
|---|---|---|---|
| `google-serp` | `apify/google-search-scraper` | Live Google Top 10, PAA, related queries, SERP Consensus audit | `/article-cluster`, `/article-intent-research`, `/article-benchmark` |
| `website-crawler` | `apify/website-content-crawler` | Deep multi-page clean Markdown crawl of exemplar or competitor guides | `/profile-research-deep`, `/article-benchmark-extract` |
| `reddit-search` | `trudax/reddit-scraper-lite` | Raw contractor, architect & engineer complaints and thread discussions | `/article-intent-research`, `/article-evidence-opinions`, `/article-faq` |
| `reddit-fast` | `fatihtahta/reddit-scraper-search-fast` | High-speed multi-query Reddit post + comment harvesting | `/article-intent-research`, `/article-evidence-opinions` |
| `youtube-search` | `streamers/youtube-scraper` | Jobsite installation walkthroughs, factory tours & subtitle metadata | `/article-intent-research`, `/article-benchmark`, `/article-visual` |
| `youtube-transcript` | `pintostudio/youtube-transcript-scraper` | Full spoken transcript extraction from technical/install videos | `/article-benchmark-extract`, `/article-evidence-opinions` |
| `youtube-comments` | `streamers/youtube-comments-scraper` | Unfiltered installer & buyer objections in video comment sections | `/article-intent-research`, `/article-faq` |
| `linkedin-posts` | `harvestapi/linkedin-post-search` | No-cookie LinkedIn posts by B2B specifiers, architects & EPC directors | `/article-intent-research`, `/article-benchmark`, `/article-evidence-opinions` |
| `google-maps-b2b` | `compass/crawler-google-places` | Regional B2B fabricators, contractors, distributors & service positioning | `/profile-discover`, `/profile-research-deep` |
| `google-maps-reviews` | `compass/Google-Maps-Reviews-Scraper` | 1–3 star B2B buyer complaints (late lead times, warping, bad crating) | `/profile-research-deep`, `/article-evidence-opinions`, `/article-faq` |
| `alibaba-suppliers` | `devcake/alibaba-products-scraper` | Wholesale FOB price bands, MOQ, lead-time claims & spec baselines | `/profile-research-deep`, `/article-evidence-opinions`, `visual-material-hunt` |
| `amazon-reviews` | `junglee/amazon-reviews-scraper` | 1–3 star failure teardowns of cheap off-the-shelf/B2C alternatives | `/article-evidence-opinions` (April Dunford Status-Quo Teardown) |
| `google-trends` | `apify/google-trends-scraper` | 12-month search demand trajectory & regional breakout queries | `/article-cluster`, `/article-review` |
| `tiktok-installs` | `clockworks/tiktok-scraper` | Short-form jobsite installation clips & workshop process visuals | `visual-material-hunt`, `/article-intent-research` |
| `rag-browser` | `apify/rag-web-browser` | General web search & single-URL Markdown extraction (`--browser` for JS) | All stages (baseline verification) |

### Beyond the 15 Presets: Dynamic Actor Store Exploration (`discover --with-schemas`)
Whenever a topic touches a specialized industry portal (e.g., **Houzz, ArchDaily, Thomasnet, G2, Trustpilot, Capterra, Pinterest, Instagram, Quora, 1688, Made-in-China, GitHub, Patent databases**), do NOT stop at the 15 presets. Run:
```bash
python3 scripts/apify_research.py discover "<platform or domain keyword>" --limit 5 --with-schemas --output .scratch/apify/discovered.json
```
This queries the live Apify Store, ranks Actors by `totalRuns` / `totalUsers`, and automatically embeds `compactSchema` (`required` + top `properties`) for the top 3 Actors so you can immediately invoke `python3 scripts/apify_research.py run --actor "<username/name>" --input-json '<payload>'`.

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
