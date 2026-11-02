# Complete Tool Inventory

Search, scrape, and browser automation tools for this project. **Apify is the mandatory Tier 0 primary entry point** for all search and external research; do not hold Apify back to "save cost" (tokens are rotated monthly and unused quota expires).

---

## Tier 0 — Mandatory Primary Entry: Apify

| Tool / Command | Mode | Best At | Use when... |
|---|---|---|---|
| `python3 scripts/apify_research.py check` | Local CLI (3-slot failover) | Verify token slots (`.env.apify.local` / `~/.config/b2b-seo-agent/apify.env`) | Diagnosing auth or slot status |
| `python3 scripts/apify_research.py run "<query/URL>"` | Local CLI (`apify/rag-web-browser`) | Web search + full markdown page extraction (`--browser` for Playwright mode) | **Default starting point for any search or URL extraction** |
| `python3 scripts/apify_research.py discover "<query>"` | Local CLI (Actor Store) | Discover specialized Actors (SERP, Reddit, Alibaba, 1688, YouTube, Maps, etc.) | Default browser Actor is blocked or a platform-native scraper fits better |
| `python3 scripts/apify_research.py schema "<actor>"` | Local CLI | Inspect exact Actor input schema before calling `--input-json` | Running any specialized Actor |
| `mcp__apify__apify__rag_web_browser` | Apify MCP | Direct MCP call to RAG web browser | Native MCP alternative to `scripts/apify_research.py run` |
| `mcp__apify__search_actors` / `call_actor` / `get_dataset_items` | Apify MCP | Search, run, and fetch datasets from any Apify Actor | Native MCP workflow |

---

## Invocation Mapping

Use friendly names for planning, but call the concrete runtime tools:

| Friendly name | Concrete callable name |
|---|---|
| `you-search` | `mcp__you__you_search` dynamic MCP tool |
| `you-research` | `mcp__you__you_research` dynamic MCP tool |
| `you-contents` | `mcp__you__you_contents` dynamic MCP tool |
| `exa search` | `web_search_exa` or `web_search_advanced_exa`; mcporter form: `exa.web_search_exa` |
| `exa fetch` | `web_fetch_exa`; mcporter form: `exa.web_fetch_exa` |
| `crawl4ai` | mcporter form: `crawl4ai.<tool_name>` |
| `firecrawl` | mcporter form: `firecrawl.<tool_name>` |
| `scrapling` | mcporter form: `scrapling.fetch`, `scrapling.stealthy_fetch`, `scrapling.screenshot` |
| `apify actor search` | `mcp__apify__search_actors` |
| `apify actor details` | `mcp__apify__fetch_actor_details` |
| `apify actor run` | `mcp__apify__call_actor` |
| `apify dataset read` | `mcp__apify__get_dataset_items` |

Do not call `exa_search`; it is not the current Exa tool name.
Do not test You.com with `mcporter list you`; in this environment You.com is exposed through dynamic MCP tools, not mcporter.

Agent-reach is a router, not proof of platform availability. Treat `agent-reach doctor` / `agent-reach watch` as hints only. Before using any platform result in an article workflow, run the real platform command and inspect relevance.

---

## Tier 1 — Complementary Multi-Index Search (Cross-Check After Apify Tier 0)

| Tool | Server/CLI | Cost | Best At | Use when... |
|---|---|---|---|---|
| `you-search` | You.com MCP | Paid | High-quality web/news search with livecrawl, freshness, domain filters | Cross-checking Apify results across a second independent search index |
| `tavily_search` | tavily MCP | Paid | Configurable search depth, domain filtering, time range, news | Second/third independent index verification alongside Apify and You.com |
| `exa.web_search_exa` | exa MCP (via mcporter) | Paid | Semantic/neural search — finds conceptually related pages regardless of keyword match | Concept-level discovery or a second independent index |
| `WebSearch` | Built-in | Free | Fast, broad web search from Bing index | Quick second source or fallback |
| `WebFetch` | Built-in | Free | Simple URL fetch, returns markdown | Lightweight fetch companion |

---

## Tier 2 — Deep Search & Complementary Local/Standard Extraction

| Tool | Server | Cost | Best At | Use when... |
|---|---|---|---|---|
| `you-research` | You.com MCP | Paid | Synthesized, cited research with configurable effort (lite / standard / deep / exhaustive) | You need a concise multi-source synthesis alongside Apify extraction |
| `tavily_research` | tavily MCP | Paid | Deep multi-source research on a topic (auto breadth/depth) | Verifying complex technical claims |
| `tavily_extract` | tavily MCP | Paid | Clean content extraction from known URLs | Secondary extractor when cross-checking page text |
| `tavily_crawl` | tavily MCP | Paid | Multi-page crawl from a starting URL | You need to map an entire site section or knowledge base |
| `tavily_map` | tavily MCP | Paid | Discover all URLs under a domain | You don't know which page has the information — map first, then scrape |
| `crawl4ai.crawl_url` | crawl4ai MCP | Free | Single-page crawl with JS rendering, screenshot, PDF export, overlay removal | Fast local extraction companion alongside Apify `rag-web-browser` |
| `crawl4ai.deep_crawl` | crawl4ai MCP | Free | Multi-page crawl with BFS/DFS strategy, keyword focus, domain filtering | You need comprehensive coverage of a site section |
| `crawl4ai.extract_structured_data` | crawl4ai MCP | Free | CSS/XPath-based structured extraction | Spec tables, comparison charts, pricing data |
| `crawl4ai.extract_with_llm` | crawl4ai MCP | Free | LLM-powered extraction with natural language instructions | Unstructured content needing interpretation |
| `crawl4ai.batch_crawl` | crawl4ai MCP | Free | Crawl 5+ URLs in parallel | You have a list of URLs to process |
| `crawl4ai.crawl_with_filter` | crawl4ai MCP | Free | Crawl with BM25/pruning/LLM filtering | Large pages where only specific sections are relevant |
| `crawl4ai.extract_links` | crawl4ai MCP | Free | Extract and preview all links from a page | You need a site's link structure |

---

## Tier 3 — Real Browser (interaction, heavy JS, anti-bot bypass)

Use only when free crawlers returned empty or a login/Captcha wall blocks them.

> **Browser choice — Playwright over agent-browser (verified 2026-06-24):** `mcp__agent-browser__*`'s daemon launches a browser whose fingerprint Google flags — every `google.com/search` request is redirected to the `/sorry/` anti-bot wall, so it cannot extract Google SERP/PAA. Playwright (via `mcp__plugin_playwright_playwright__*` or the `scripts/extract_google_paa.py` helper using `launch_persistent_context`) passes Google's anti-bot and renders the real SERP. **Prefer Playwright as the primary real-browser tool.** Keep agent-browser only as a secondary option for non-Google pages where its daemon is convenient.

| Tool | Server | Cost | Best At | Use when... |
|---|---|---|---|---|
| `mcp__plugin_playwright_playwright__browser_navigate` | Playwright MCP | Paid | Full Chromium navigation, passes Google anti-bot | **Default real-browser tool**, including Google SERP/PAA |
| `mcp__plugin_playwright_playwright__browser_snapshot` | Playwright MCP | Paid | Accessibility tree of current page | You need to see interactive elements |
| `mcp__plugin_playwright_playwright__browser_evaluate` | Playwright MCP | Paid | Execute arbitrary JavaScript in the page | Extract PAA questions / data only available via JS |
| `mcp__plugin_playwright_playwright__browser_get_html` | Playwright MCP | Paid | Full rendered HTML after JS execution | Page is an SPA |
| `mcp__plugin_playwright_playwright__browser_take_screenshot` | Playwright MCP | Paid | Visual page capture | Visual confirmation or design analysis |
| `mcp__plugin_playwright_playwright__browser_click` | Playwright MCP | Paid | Click elements | "Load More", pagination, tabs |
| `scripts/extract_google_paa.py` | Local Playwright script | Free | Batch Google PAA extraction with persistent context + retries | `/article-intent-research` PAA channel — produces verifiable candidates with real selector + timestamp |
| `scrapling.fetch` | scrapling MCP via mcporter | Free/local | Rendered fetch with session-capable browser tooling | crawl4ai returned thin content and you need a local browser-backed extractor before paid/browser escalation |
| `scrapling.stealthy_fetch` | scrapling MCP via mcporter | Free/local | Anti-bot-oriented fetch with fingerprint spoofing | A normal fetch hits light anti-bot or returns a challenge page |
| `scrapling.screenshot` | scrapling MCP via mcporter | Free/local | Screenshot from an existing scrapling session | You need visual evidence while harvesting or auditing page assets |
| `mcp__agent-browser__*` | agent-browser MCP | Paid | Secondary browser for non-Google pages | Playwright unavailable; **do not use for Google SERP/PAA** (redirects to /sorry) |

---

## Tier 4 — Platform-Specific / Agent-Reach (social, video, Chinese web, forums)

These access platforms that general search engines can't reach or index well.

| Tool | Method | Cost | Best At | Use when... |
|---|---|---|---|---|
| **Reddit** | Python 3.12 + `rookiepy` + old.reddit search JSON | Free | Real buyer/specifier questions | Searching for pain points and peer questions |
| **微信公众号** | Exa search + local reader venv: `~/.agent-reach/tools/wechat-article-for-ai/.venv/bin/python main.py URL` | Free/local + Exa | Chinese competitor content, industry articles | Chinese manufacturer content strategy |
| **B站 (Bilibili)** | `yt-dlp "bilisearch3:关键词"` or B站 search API only after the real command succeeds | Free | Chinese tutorials, reviews, factory tours | Can hit 412; do not treat docs or prior success as current availability |
| **LinkedIn** | Python 3.12 + `rookiepy` + `li_at` cookie | Free (auth) | Professional discussions, company pages | Architecture/design professional content |
| **Jina Reader** | `curl -s "https://r.jina.ai/URL"` | Free | Quick clean markdown from any URL | Free extraction fallback after crawl4ai/WebFetch |
| **YouTube** | Homebrew `yt-dlp` via `yt-dlp` symlink | Free | Video transcripts, walkthroughs, demos | Installation/factory tour videos |
| **微博** | `mcporter call weibo.search_content` | Paid | Chinese social discussions | Market research in Chinese |
| **Twitter** | `twitter search` CLI | Free | Real-time discussions, brand mentions | Rarely useful for B2B metal fabrication |
| **小红书** | `xhs search` only after it returns non-guest results | Auth required | Chinese visual/social material | Do not rely on doctor; current guest status can return `code=-104` |
| **Made-in-China** | `scrapling.fetch` or rendered browser extraction | Free/local | Product cards, supplier pages, B2B product images | Good source for concrete visual candidates |
| **Alibaba** | Authenticated browser asset extraction → cookie-session probe → You indexed/mobile pages → Scrapling stealth → Apify Alibaba Actor | Mixed | Product listings, supplier images, detail-page media, and product videos | Do not print cookie values; Codex `pageAssets` is only one adapter. Shell agents can use `.claude/skills/visual-material-hunt/scripts/alibaba_cookie_probe.py`; Apify `getdataforme/alibaba-category-scraper` also worked with a realistic cost cap |
| **1688** | Apify 1688 Actor first, then Chinese browser/search routes | Paid/local | Chinese wholesale product galleries and supplier verification | Headless page captcha is expected; use specialized Actors |

---

## Tier 5 — Additional Secondary Extractors

Use these to complement Apify (`Tier 0`), Scrapling, Crawl4AI, and Playwright real Chrome when multi-backend extraction or layout preservation is needed.

| Tool | Server | Cost | Use when... |
|---|---|---|---|
| `firecrawl_search` | firecrawl MCP | Paid | You need an additional search backend to cross-check Apify / You.com / Tavily / Exa |
| `firecrawl_scrape` | firecrawl MCP | Paid | Secondary page extractor when combining multiple scraping pipelines |
| `you-contents` | You.com MCP | Paid | Full-page markdown/HTML extraction when HTML layout preservation is needed |
| `crawl4ai.crawl_with_auth` | crawl4ai MCP | Free | Page is behind login and you have credentials |
| `crawl4ai.crawl_dynamic_content` | crawl4ai MCP | Free | Page uses infinite scroll or lazy loading |
| `crawl4ai.crawl_with_js_execution` | crawl4ai MCP | Free | Page needs specific JavaScript before content appears |

> Note: All Apify tools (`scripts/apify_research.py` and `mcp__apify__*`) belong exclusively to **Tier 0 (Mandatory Primary Entry)** above — never hold Apify back as a Tier 5 fallback.
