# Channel Playbooks for `/article-intent-research`

Detailed extraction instructions per channel. Load the `search-toolbox` skill first to choose the right tool and fallback chain for the current runtime.

## Google PAA

- **Minimum:** 4 real questions.
- **Method:** Browser DOM extraction from `https://www.google.com/search?q=<query>&hl=en&gl=us`.
- **Tool choice — why Playwright, not agent-browser:** `mcp__agent-browser__*`'s daemon launches a browser whose fingerprint Google flags, redirecting every `/search` request to the `/sorry/` anti-bot wall (verified 2026-06-24). Use **Playwright with a persistent context** instead — `mcp__plugin_playwright_playwright__*` for one-off inspection, or the `scripts/extract_google_paa.py` helper for batch extraction. A persistent Chrome user-data dir (Playwright `launch_persistent_context`) is what passes Google's anti-bot; a fresh `launch()` context is still blocked.
- **Selector hint:** Google rotates PAA DOM frequently and no single selector is stable. The PAA questions live in the "People also ask" region, commonly on elements carrying `jsname` attributes or `role="button"`. **Record the exact selector you actually observe at extraction time** — `extract_google_paa.py` records `div[role='button'] / div[jsname] within the PAA region` as observed 2026-06-24; re-verify if the DOM changed. Never record a selector you did not observe.
- **Evidence:** exact query URL + the selector actually observed + ISO-8601 timestamp (date **and** time).
- **Tool route (Apify-First):** `python3 scripts/apify_research.py run --preset google-serp "<query>" --output <out.json>` or `python3 scripts/extract_google_paa.py "<query>"` (which automatically calls Apify `apify/google-search-scraper` across the 3 rotating token slots first, then complements with persistent real-Chrome Playwright for interactive PAA accordion expansion) → `mcp__plugin_playwright_playwright__*` (single-query interactive inspection) → search-API question cross-check (Tavily/You.com). Never record a selector you did not observe, and never fabricate PAA questions to meet the minimum.
- **Rate note:** `extract_google_paa.py` uses Apify's SERP actor pool first and paces any direct real-Chrome follow-up queries (5s gap with backoff). Pass `--browser-only` only when specifically testing local Chrome interactive PAA expansion.

## Google Autocomplete

- **Minimum:** 8 real suggestions.
- **Method:** HTTP GET to `https://suggestqueries.google.com/complete/search?client=firefox&q=<query>`.
- **Evidence:** exact API URL + timestamp.
- **Tool route:** Bash `curl` or `WebFetch`.

## Reddit / English Forums

- **Minimum:** 5 real thread titles.
- **Method:** Search `site:reddit.com <topic>` or direct subreddit search.
- **Evidence:** exact search query + thread URLs + timestamp.
- **Tool route:** `python3 scripts/apify_research.py run "site:reddit.com <topic>"` or Apify Reddit Actor → `agent-reach` Reddit → `mcp__tavily__*` / `you-search` / `WebSearch` cross-check.

## Chinese Social (Xiaohongshu / WeChat)

- **Minimum:** 3 posts when profile language/market includes Chinese.
- **Method:** Platform search via Apify / `agent-reach` (xhs / wechat) or equivalent.
- **Evidence:** platform + search query + post URL(s) + timestamp.
- **Tool route:** Apify Actor / `scripts/apify_research.py` → `agent-reach` → Scrapling / Playwright real Chrome.
- **Note:** Failure is acceptable if the channel is irrelevant; it must still be logged.

## Non-Text Question Sources

- **Minimum:** 3 video/podcast episode titles when relevant.
- **Method:** Platform search for titles that capture real buyer questions.
- **Evidence:** platform + search query + media URL(s) + timestamp.
- **Tool route:** Apify YouTube/Video Actor or `scripts/apify_research.py` → `yt-dlp` / `you-search` → transcript extraction only if it adds a unique question angle.

## Evidence Quality Rules

1. Do not paraphrase a candidate and label it as extracted. Copy the exact wording.
2. If a channel returns fewer candidates than the minimum, log the failure and state the workaround.
3. Never synthesize a "likely" PAA/Reddit question to fill the minimum.
