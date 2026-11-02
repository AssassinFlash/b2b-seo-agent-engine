# Source Routing For Visual Material Hunt

Use this file when deciding where to search for article visual assets.

## Primary Discovery (Apify-First)

| Need | Start with | Why |
|---|---|---|
| Broad source & page discovery | `python3 scripts/apify_research.py run` / `mcp__apify__*` | Mandatory Apify-first entry; full markdown + metadata extraction |
| Platform & image candidates | Apify specialized Actors (`discover` / `run`) + Tavily `include_images: true` | Direct high-res product, project, and social media assets |
| Case/project pages | Apify + Exa `web_search_exa` / `mcp__you__you_search` | Multi-index discovery of manufacturer and project case pages |
| Known source page extraction | Apify (`--browser` when needed) → Scrapling / Crawl4AI / Firecrawl / Playwright real Chrome | Combinatorial extraction across anti-bot barriers |

`mcp__you__you_search` and `mcp__you__you_contents` are dynamic MCP tools, not `mcporter` servers. Do not test them with `mcporter list you`.

## B2B Marketplace Routes

| Platform | Preferred route | Recovery route |
|---|---|---|
| Made-in-China | `scrapling.fetch` or rendered Playwright extraction | Tavily/You indexed image URLs, then product detail page extraction |
| Alibaba | Authenticated browser asset extraction | Cookie-session probe, You indexed/mobile pages, Scrapling stealth, then Apify Alibaba Actor; use a realistic smoke-test cap because low caps can abort before output |
| 1688 | Apify 1688 Actor first for repeatable product data | Chinese keyword, GBK/URL-encoded query, real browser state, Scrapling stealth |

Do not mark Alibaba or 1688 as blocked just because a headless Playwright search page shows a slider captcha. For this project, captcha means "change route", not "give up".

## Apify Actor Layer

Use Apify when a platform-specific Actor is stronger than generic browser automation.

Verified useful Actor families from live discovery:

| Platform | Example Actor / Preset | Use |
|---|---|---|
| Alibaba (`--preset alibaba-suppliers`) | `devcake/alibaba-products-scraper` | Product listings, supplier signals, MOQ/price, high-res image URLs (`python3 scripts/apify_research.py run --preset alibaba-suppliers "<query>"`) |
| Alibaba | `getdataforme/alibaba-category-scraper` | Verified with `maxTotalChargeUsd: 1`, returned product URLs, supplier data, MOQ, price, `mainImage`, and `additionalImages` |
| YouTube (`--preset youtube-search`) | `streamers/youtube-scraper` | Installation walkthroughs, factory tours, timestamps & subtitles (`python3 scripts/apify_research.py run --preset youtube-search "<query>"`) |
| TikTok (`--preset tiktok-installs`) | `clockworks/tiktok-scraper` | Short-form jobsite installation clips & workshop process visuals (`python3 scripts/apify_research.py run --preset tiktok-installs "<hashtag>"`) |
| 1688 | `zen-studio/1688-wholesale-scraper` | Rich 1688 product records, galleries, supplier data |
| 1688 | `devcake/1688-com-products-scraper` | Simpler 1688 product search |
| Reverse image | `dev00/alibaba-1688-aliexpress-reverse-image-search-api` | Find similar supplier listings from an existing image |
| Any vertical portal (Houzz, Pinterest, Instagram) | `python3 scripts/apify_research.py discover "<platform>" --with-schemas` | Auto-discover top Store Actors and inspect `compactSchema` in one call |

Before calling a new Actor, run `fetch_actor_details` and inspect the input schema. Keep `maxResults`, `max_pages`, or equivalent low for smoke tests.

Alibaba image URLs from Actors may need normalization. In the 2026-06-18 smoke test, `getdataforme/alibaba-category-scraper` returned some `s.alicdn.com` image URLs ending in `.jpg.jpg`; those direct URLs returned 404 placeholders, while the normalized `.jpg` URL returned real JPEG files. Always run an access check before promoting Alibaba images.

## Authenticated Alibaba Route

Use this route when the operator has logged in to Alibaba in Chrome or another persistent browser profile. Do not print, save, or expose cookie values. Treat Codex `pageAssets` as one adapter, not the canonical workflow.

1. Open or claim the real product page in the logged-in browser when the agent has browser control.
2. Verify the page is not a login, captcha, or anti-bot page by checking URL, title, product title, supplier, price, and MOQ.
3. Use rendered page assets when available, or run a bounded DOM image/video probe such as `document.images` plus `video, source` extraction.
4. Prefer `product-img` or large `s.alicdn.com/@sc01/kf/` detail images over logos, icons, payment badges, and tracking pixels.
5. Run `curl -I -L` or browser access checks on selected media URLs before recording them as candidates.

Agent adapters:

- Codex: use Chrome tab control and `pageAssets` when available.
- Any shell-capable local agent: run `python3.12 .claude/skills/visual-material-hunt/scripts/alibaba_cookie_probe.py URL` after the operator logs in to Chrome. The script keeps cookies in memory and prints only page/media metadata.
- Generic Playwright: use a persistent profile that the operator has logged into, then query rendered DOM images/videos.
- No browser or cookie access: use Apify Actor fallback and normalize/verify returned media URLs.

In the 2026-06-18 smoke test, Codex Chrome `pageAssets` exposed 106 image assets and 1 product video for an Alibaba product page. The portable `python3.12 + rookiepy + requests` adapter also read the logged-in product HTML and extracted Alibaba media URLs without printing cookie values.

## Platform Media

| Platform | Use when | Caveat |
|---|---|---|
| YouTube | Factory tours, installation videos, product demos | Thumbnail is not the main asset unless the request asks for thumbnails |
| WeChat | Chinese industry articles and visual-rich posts | Discover URL first, then use local reader venv |
| Weibo | Chinese public posts with image galleries | Relevance varies; filter hard |
| X | Real-time media posts | High noise for B2B material queries |
| Reddit | Buyer questions and peer context | Usually weak for direct product imagery |
| XiaoHongShu | Visual inspiration | Current local `xhs search` may fail under restricted/guest cookies |
| Bilibili | Factory/tutorial videos | Can hit 412; use only after real command succeeds |

## Rejection Rules

Reject candidates with:

- Captcha/search/profile pages instead of actual material.
- Logos, watermarks, social UI, unrelated text overlays, or platform chrome.
- Blurry, tiny, cropped, incomplete, or misleading product views.
- Semantically wrong scenes, such as insect screen mesh when the article needs architectural divider proof.
- AI/mockup feel when the article moment needs real proof.
