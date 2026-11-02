# Repair & Escalation Chains (Apify-First)

For every search/scrape task type, **start with Apify (`scripts/apify_research.py` or `mcp__apify__*`)**.
Never bypass Apify without troubleshooting it first (Token slot → Actor selection → Input schema/params → Dataset inspection → `--browser` mode / timeout → Combinatorial tools).
Never stop at "nothing found." Pivot across:
`不同关键词 → 不同页面 → 不同数据源 → 不同 Actor → 不同抓取方式 → 不同技术路径`
combining Apify Actors, Scrapling, Scrapy, Crawl4AI, Firecrawl, Playwright real Chrome, Computer Use, and secondary search indexes (You.com, Tavily, Exa).

Runtime naming guardrail: `you-search` means `mcp__you__you_search`, `you-research` means `mcp__you__you_research`, and `you-contents` means `mcp__you__you_contents`. You.com is a dynamic MCP tool, not a `mcporter` server. Exa search is `web_search_exa` or `web_search_advanced_exa`; do not use `exa_search`. In mcporter CLI, call tools as `server.tool`, for example `exa.web_search_exa`, `crawl4ai.crawl_url`, `firecrawl.firecrawl_scrape`, and `scrapling.fetch`.

Agent-reach guardrail: do not trust `agent-reach doctor` alone. A platform is usable only after the actual command returns relevant results. Known current realities: `xhs search` may fail with `code=-104` under guest cookies; Bilibili can hit 412 on both yt-dlp and public API routes; local WeChat article reading requires the dedicated venv under `~/.agent-reach/tools/wechat-article-for-ai/.venv/`.

Marketplace guardrail: Alibaba and 1688 captcha pages are route failures, not platform failures. For visual material, use authenticated browser asset extraction when the operator is logged in, then escalate to cookie-session probing, You indexed/mobile pages, Scrapling stealth, and Apify specialized Actors before declaring the channel unavailable. Do not print or store cookie values. Codex `pageAssets` is one adapter, not a cross-agent requirement. Alibaba Actor runs may need a realistic per-run cap; if the Actor returns image URLs ending in duplicated extensions such as `.jpg.jpg`, normalize and verify the direct image URL before using it.

---

## Chain A — Search the Web

**Task**: Find articles, pages, or information about a topic.

```
Layer 0 (mandatory primary start — Apify-First):
  ├─ python3 scripts/apify_research.py run "<query>" --output <out.json>
  │   (or --preset google-serp / mcp__apify__apify__rag_web_browser)
  │   └─ Full Google SERP + markdown page extraction across 3 rotating monthly token slots.
  │   └─ IF EMPTY OR BLOCKED: troubleshoot token slot (`check`), switch to `--browser` mode,
  │      or discover a specialized Actor (`discover` + `schema` + `--input-json`).
  └─ mcp__apify__search_actors / call_actor (when a domain/platform-specific Actor fits better)

Layer 1 (complementary multi-index cross-check):
  └─ you-search(query, count=5)
      └─ You.com index with livecrawl option. High-quality snippets, fresh results, domain filters.
      └─ DETECT EMPTY: "No results found." or results object lacks web/news entries
      └─ DETECT WEAK: fewer than 3 relevant results

Layer 2 (parallel cross-check, different indexes):
  ├─ tavily_search(query, search_depth="advanced", max_results=5)
  │   └─ Google-based index. Good for keyword search, time ranges, domain filters.
  ├─ exa.web_search_exa(query, numResults=5) [via mcporter]
  │   └─ Semantic/neural search. Concept-based, not keyword-based.
  └─ WebSearch(query)
      └─ Built-in Bing-based search. Free fallback.
  If any two agree → you have independent confirmation.

Layer 3 (deep/specialized):
  ├─ you-research(query, research_effort="lite" or "standard")
  │   └─ Cited synthesis from multiple web sources.
  ├─ tavily_research(query)
  │   └─ Deep/authoritative sources on technical topics.
  ├─ exa.web_search_exa(rephrased query, numResults=10)
  │   └─ Semantic reframe.
  └─ crawl4ai.deep_crawl(url, max_depth=2, max_pages=20)
      └─ If you know the site but not the specific page.

Layer 4 (platform-specific voices):
  ├─ Apify specialized platform Actors (Reddit, YouTube, Alibaba, 1688)
  ├─ Reddit cookie script (real user questions)
  ├─ LinkedIn cookie search (professional discussions)
  ├─ 微信公众号 / miku_ai (Chinese market content)
  └─ B站 API (video/how-to content)
```

**Key principle**: Start with Apify (`scripts/apify_research.py` or `mcp__apify__*`). If an Actor or query returns empty/blocked, repair the Actor/parameters/browser-mode first, then combine with You.com + Tavily + Exa + WebSearch for multi-index verification.

---

## Chain B — Scrape a URL

**Task**: Extract content from a specific URL.

```
Layer 0 (mandatory primary start — Apify-First):
  ├─ python3 scripts/apify_research.py run "<URL>" --output <out.json>
  │   (add `--browser` for JS-heavy pages or `--preset website-crawler` for multi-page docs)
  └─ IF THIN OR BLOCKED: enable `--browser`, inspect dataset items, or combine with Layer 1–4 below.

Layer 1 (fast local/free extraction companions):
  └─ crawl4ai.crawl_url(URL, wait_for="main")
      └─ JS-capable, handles light bot protection.
      └─ DETECT EMPTY: extracted content is empty or < 200 characters
      └─ DETECT BLOCK: status non-200, anti-bot page, or only navigation links

Layer 2 (lightweight markdown extractors):
  ├─ WebFetch(URL)
  │   └─ Built-in simple fetch. Returns markdown.
  │   └─ DETECT EMPTY: body is empty or < 200 characters
  └─ Jina Reader — curl -s "https://r.jina.ai/URL"
      └─ Clean markdown from any URL.
      └─ DETECT EMPTY: response body is < 100 chars or only navigation
      └─ DETECT BLOCK: "Please enable JavaScript", "Checking your browser"

Layer 3 (secondary extraction backends):
  ├─ tavily_extract(urls=[URL], extract_depth="advanced")
  │   └─ Different user-agent/IP.
  ├─ firecrawl_scrape(url=URL, formats=["markdown"])
  │   └─ Secondary markdown/HTML scraper.
  └─ you-contents(urls=[URL], formats=["markdown"])
      └─ Full-page extraction when layout preservation is needed.

Layer 4 (real browser — interaction walls, heavy JS, CAPTCHA):
  ├─ scrapling.fetch(URL, extraction_type="markdown")
  │   └─ Local browser-backed fetch before escalating to interactive browser work.
  ├─ scrapling.stealthy_fetch(URL, extraction_type="markdown")
  │   └─ Use when a normal fetch hits light anti-bot or fingerprint checks.
  ├─ Playwright (primary real browser — passes Google anti-bot; agent-browser does not):
  │   browser_navigate(URL) → browser_snapshot() → browser_evaluate() / browser_get_html()
  │   For Google SERP/PAA use scripts/extract_google_paa.py (persistent context).
  │   DETECT EMPTY: snapshot shows only skeleton/spinner/no meaningful content
  │   DETECT LOGIN-WALL: snapshot shows "Sign in to continue" or login form
  │   DETECT CAPTCHA: snapshot shows "Verify you are human"
  ├─ crawl4ai.crawl_dynamic_content(URL, scroll=true)
  │   └─ For infinite scroll or lazy-loading pages.
  └─ agent-browser (secondary, non-Google pages only — its daemon trips Google /sorry):
      browser_navigate(URL) → browser_wait("5000") → browser_snapshot() → browser_get_html()
```

**Key principle**: Start with Apify (`scripts/apify_research.py run "<URL>"`, adding `--browser` when JS rendering is required), and combine with `crawl4ai`, `scrapling`, `firecrawl`, and Playwright real Chrome across different technical paths.

---

## Chain C — Verify a Factual Claim (2-Source Minimum)

**Task**: Verify a claim from at least 2 independent sources using different search tools.

```
Step 1 (search — start with Apify, then cross-check across independent indexes):
  ├─ python3 scripts/apify_research.py run "<claim keywords>" --output <out.json>
  │   └─ Primary search + full-page markdown extraction.
  ├─ you-search(claim keywords)
  │   └─ Independent index cross-check.
  └─ Run in parallel when additional independent confirmation is needed:
      ├─ tavily_search(claim keywords, search_depth="advanced")
      ├─ exa.web_search_exa(claim keywords, numResults=5)
      └─ WebSearch(claim keywords)

Step 2 (semantic reframe):
  └─ exa.web_search_exa(claim keywords, numResults=10)
      └─ Finds authoritative sources (industry standards, academic papers, certification bodies).

Step 3 (scrape the authoritative URL — cost-first extraction):
  If a promising authoritative URL was found, extract in this order:
  1. crawl4ai.crawl_url(url=authoritative_URL, wait_for="main")
  2. Jina Reader — curl -s "https://r.jina.ai/authoritative_URL"
  3. WebFetch(authoritative_URL)
  4. tavily_extract(urls=[authoritative_URL])
  5. firecrawl_scrape(url=authoritative_URL, formats=["markdown"])
  6. you-contents(urls=[authoritative_URL], formats=["markdown"])
  7. scrapling.fetch(url=authoritative_URL, extraction_type="markdown")
  8. Playwright / agent-browser (if JS-rendered or blocked)
  Read the actual source. Don't cite a search result — cite the page.

Step 4 (deep verification for complex claims):
  ├─ you-research(claim, research_effort="standard" or "deep")
  ├─ tavily_research(claim, model="pro")
  └─ exa.web_search_exa(claim concept, numResults=10)

IF at any point you have LESS than 2 independent sources → mark claim as "weak."
IF at any point you have ZERO sources → mark claim as "unverified" → BLOCK in Truth QA.
```

**Key principle**: Two sources from the SAME tool are NOT independent. Cross-tool = cross-index = genuinely independent.

---

## Chain D — Find Real Buyer Questions

**Task**: Find authentic questions and confusion from real buyers/specifiers.

```
Layer 1 (primary — people ask peers, not Google):
  ├─ Reddit (Python 3.12 + rookiepy cookie):
  │   Search old.reddit.com/r/architecture/search.json?q=query&restrict_sr=on
  │   Search old.reddit.com/r/InteriorDesign/search.json?q=query&restrict_sr=on
  │   Search old.reddit.com/search.json?q=query (all subreddits)
  │   DETECT EMPTY: no children in JSON response OR all results from unrelated subreddits
  │   DETECT AUTH-FAIL: 403 status → fall back to Layer 2
  ├─ LinkedIn (MCP; verify relevance because location filters can drift)
  ├─ 微信公众号 (Exa search, then local reader venv for full text)
  ├─ B站 route-dependent search after a real `yt-dlp` or API command succeeds
  └─ YouTube / yt-dlp (video transcripts)

Layer 2 (search fallback for forum content):
  └─ you-search(query + " site:reddit.com")
  └─ tavily_search(query + " site:reddit.com", search_depth="advanced")
  └─ WebSearch(query + " site:reddit.com/r/architecture")
  Lower quality than cookie auth, but works without auth.

Layer 3 (general forums):
  ├─ you-search(query + " forum OR discussion OR question")
  ├─ tavily_search(query + " forum OR discussion OR question", search_depth="advanced")
  ├─ exa.web_search_exa(query + " real questions")
  └─ WebSearch(query + " architect question OR specifier question")

IF ALL layers return empty: this is itself a signal. The information doesn't exist publicly. This validates the article's value proposition.
```

---

## Chain E — Deep Topic Research

**Task**: Build a cited, synthesized understanding of a topic before drafting or verification.

```
Layer 0 (mandatory primary start — Apify-First):
  └─ python3 scripts/apify_research.py run "<topic>" --max-results 8 --output <out.json>
      └─ Full-text markdown extraction from top authoritative pages + `.summary.md` digest.

Layer 1 (multi-source synthesis):
  ├─ you-research(input=topic, research_effort="standard")
  │   └─ Structured overview with citations and source URLs.
  └─ tavily_research(query)
      └─ Authoritative, technical, or academic depth.

Layer 2 (semantic gap fill):
  └─ exa.web_search_exa(topic concept, numResults=10)
      └─ Catches sources the synthesis tools missed.

Layer 3 (source extraction):
  └─ Scrape the most promising URLs with Apify (`--browser` / `--preset website-crawler`) → crawl4ai.crawl_url → scrapling.fetch → Jina Reader → WebFetch → tavily_extract → firecrawl_scrape → you-contents → Playwright real Chrome.
```

**Key principle**: Start with Apify full-page extraction and synthesis tools to map the territory, then extract deep technical sources across complementary pipelines.

---

## Chain F — Find Visual Material Candidates

**Task**: Find source-backed article images, product photos, project visuals, detail/process images, or platform media for `image-strategy`.

```
Step 1 (visual need):
  └─ Load visual-material-hunt after image-strategy defines image type and placement.

Step 2 (Apify-First + broad candidate pool):
  ├─ python3 scripts/apify_research.py (or mcp__apify__* specialized image/marketplace Actors)
  │   Primary discovery for supplier, project, and platform visual candidates.
  ├─ you-search(query, count=5)
  │   Use thumbnails, snippets, domain filters, and livecrawl only when needed.
  ├─ tavily_search(query, include_images=true)
  │   Direct image candidates and fast URL pool.
  └─ exa.web_search_exa(query, numResults=5)
      Case pages, project pages, and semantically related manufacturer pages.

Step 3 (extract source context):
  └─ crawl4ai / Jina / WebFetch / scrapling.fetch
      Keep only candidates with source URL + asset URL or source-backed media.

Step 4 (B2B marketplace routes):
  ├─ Made-in-China: scrapling.fetch or rendered browser extraction.
  ├─ Alibaba: authenticated browser asset extraction when available → cookie-session probe script → You indexed/mobile page → scrapling stealth → Apify Alibaba Actor; if using `getdataforme/alibaba-category-scraper`, set a realistic smoke-test cap and normalize/verify returned image URLs.
  └─ 1688: Apify 1688 Actor first for repeatable product/image data, then Chinese browser routes.

Step 5 (platform media):
  ├─ YouTube / yt-dlp for videos and thumbnails.
  ├─ WeChat reader venv for visual-rich Chinese articles.
  ├─ Weibo/X only when posts contain concrete media and strong relevance.
  └─ Reddit/Bilibili/XHS only after a real command succeeds for the current query.
```

IF a page is only a search page, profile page, captcha page, or placeholder image → reject it.
IF Alibaba/1688 headless browser hits captcha → change route; do not mark platform blocked.
IF all real-photo routes fail -> tell `image-strategy` the real-image route is unavailable and use backup, HTML, table, or no-visual routes honestly.

---

## Error Detection Reference

### What "empty result" looks like per tool

| Tool | Empty Pattern |
|---|---|
| `you-search` | "No results found." or `results` object has no `web`/`news` keys |
| `tavily_search` | `results` array is empty or all titles are unrelated |
| `exa.web_search_exa` | No results returned, or all results are from wrong domains |
| `WebSearch` | Returns generic results with no specific information about the query |
| `crawl4ai.crawl_url` | Extracted content is empty or < 200 characters |
| `WebFetch` | Body is empty or < 200 characters |
| `Jina Reader` | Response body is `< 100 chars` or contains only navigation |
| `tavily_extract` | Extracted text is empty or < 200 characters |
| `firecrawl_scrape` | Empty markdown, error object, or status non-200 |
| `you-contents` | Returned content is empty, < 200 characters, or mostly image markdown |
| `scrapling.fetch` | Non-200 status, empty content array, or only challenge/navigation text |
| `Playwright snapshot` | Snapshot shows only skeleton/spinner/no meaningful content |
| `agent-browser snapshot` | (Secondary) Snapshot empty — or, for Google, redirected to `/sorry/` (use Playwright instead) |
| `Reddit search` | Response `data.children` array is empty, or all children are from unrelated subreddits |
| `微信公众号` | Returns articles about unrelated topics (broad match on keywords) |
| `B站 API` | `data.result` is empty across all result_type categories |

### What "blocked" looks like per tool

| Tool | Block Pattern |
|---|---|
| `crawl4ai` | Status code non-200, or body contains anti-bot page |
| `WebFetch` | Status non-200 or redirect loop |
| `Jina Reader` | Response contains "Please enable JavaScript" or "Checking your browser" |
| `tavily_extract` | Status non-200, empty body, or body contains "Access Denied" |
| `firecrawl_scrape` | Status non-200, quota error, or anti-bot page |
| `you-contents` | "No results found." or error object indicating crawl failure |
| `scrapling.fetch` | Browser/session launch error, challenge page, or status non-200 |
| `Playwright` | Snapshot shows Cloudflare challenge, "Verify you are human", or login wall (for Google /sorry, switch to Apify SERP actor) |
| `agent-browser` | (Secondary) Same symptoms as Playwright; for Google it shows `/sorry/` — use Playwright instead |

### When to escalate vs. when to stop

- **ESCALATE**: result is empty, blocked, or has < 3 relevant items
- **ESCALATE**: all results come from the same domain or same type (e.g., all product pages)
- **STOP**: 3+ independent sources from 2+ tools all agree on the same information
- **STOP**: 3+ tools across different indexes all return "no information exists on this topic" (this is a real finding — the gap is confirmed)
