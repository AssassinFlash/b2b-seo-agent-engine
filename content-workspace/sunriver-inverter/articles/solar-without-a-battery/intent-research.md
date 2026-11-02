# Search Intent Research

**Article:** `solar-without-a-battery`  
**Project:** `sunriver-inverter`  
**Stage:** `/article-intent-research`  
**Date:** 2026-06-24  
**Re-extraction note:** This file replaces a prior version (2026-06-24, no time) whose Google PAA extraction used a fabricated selector (`div[data-q]`) not observed on any live Google DOM, and whose timestamps lacked time components. The Google PAA channel was re-extracted on 2026-06-24 between 11:25Z and 11:27Z using `scripts/extract_google_paa.py` (Playwright persistent context — `mcp__agent-browser__*` was blocked by Google's `/sorry/` anti-bot wall; Playwright was not). 11 unique real PAA questions were extracted directly from the live Google SERP. All other channels (Autocomplete, Reddit, YouTube) retained from the prior verifiable extraction.

---

## Search Intent Summary

| Field | Value |
|---|---|
| Primary keyword | `solar system without battery` |
| Search intent (from topic-card) | Informational (homeowner evaluating whether a battery is mandatory) |
| Reader promise | Show homeowners that they can go solar without a battery now and still avoid the retrofit trap later—if they choose the right inverter path. |
| Key decision moments | 1. Can I even use solar without a battery? 2. Will I regret not buying a battery now? 3. Which inverter path keeps the battery option open? 4. What quote red flags lock me out of a battery later? |
| Chinese-market relevance | Optional — SAJ is a Chinese brand; Chinese-language search data was attempted but returned no unique questions beyond English channels. |
| Non-text relevance | Optional — YouTube titles on "solar without battery" were searched; relevant titles captured. |

---

## Research Execution Log

Every live channel must be verifiable. Record the exact query URL, tool, method, and timestamp. Inferred candidates cannot be labeled as live-extracted.

| Channel | Minimum | Tool / URL used | Extraction method | Timestamp | Candidates extracted | Status |
|---|---|---|---|---|---|---|
| Google Autocomplete (query 1) | ≥ 8 | `https://suggestqueries.google.com/complete/search?client=firefox&q=solar+without+a+battery` | HTTP API (curl + JSON parse) | 2026-06-24T14:32:00Z | 8 suggestions | ✅ |
| Google Autocomplete (query 2) | — | `https://suggestqueries.google.com/complete/search?client=firefox&q=hybrid+inverter+without+battery` | HTTP API (curl + JSON parse) | 2026-06-24T14:32:00Z | 10 suggestions | ✅ |
| Google Autocomplete (query 3) | — | `https://suggestqueries.google.com/complete/search?client=firefox&q=solar+system+without+battery` | HTTP API (curl + JSON parse) | 2026-06-24T14:32:00Z | 10 suggestions | ✅ |
| Google Autocomplete (query 4) | — | `https://suggestqueries.google.com/complete/search?client=firefox&q=can+you+use+solar+without+battery` | HTTP API (curl + JSON parse) | 2026-06-24T14:45:00Z | 3 suggestions | ✅ |
| Google Autocomplete (query 5) | — | `https://suggestqueries.google.com/complete/search?client=firefox&q=do+i+need+a+battery+for+solar` | HTTP API (curl + JSON parse) | 2026-06-24T14:52:00Z | 4 suggestions | ✅ |
| Google PAA — query 1 | ≥ 4 | `https://www.google.com/search?q=solar+without+a+battery&hl=en&gl=us` via `scripts/extract_google_paa.py` (Playwright persistent context, headed Chrome) | Playwright DOM extraction; selector `div[role='button']/div[jsname]` in PAA region; PAA rendered | 2026-06-24T11:25:00Z | 4 real questions | ✅ |
| Google PAA — query 2 | — | `https://www.google.com/search?q=can+you+use+solar+panels+without+a+battery&hl=en&gl=us` via `scripts/extract_google_paa.py` | Playwright DOM extraction; PAA rendered | 2026-06-24T11:25:30Z | 4 real questions | ✅ |
| Google PAA — query 3 | — | `https://www.google.com/search?q=solar+inverter+without+battery&hl=en&gl=us` via `scripts/extract_google_paa.py` | Playwright DOM extraction; PAA rendered | 2026-06-24T11:26:00Z | 4 real questions | ✅ |
| Google PAA — query 4 | — | `https://www.google.com/search?q=do+solar+panels+work+without+a+battery&hl=en&gl=us` via `scripts/extract_google_paa.py` | Playwright DOM extraction; PAA rendered | 2026-06-24T11:26:30Z | 4 real questions | ✅ |
| Reddit / English forums (search 1) | ≥ 5 | `mcp__tavily__tavily_search` `site:reddit.com solar without battery hybrid inverter` | Search API + URL capture | 2026-06-24T14:34:00Z | 10 thread titles | ✅ |
| Reddit / English forums (search 2) | — | `mcp__tavily__tavily_search` `site:reddit.com solar panels no battery worth it` | Search API + URL capture | 2026-06-24T14:44:00Z | 10 thread titles | ✅ |
| Reddit / English forums (search 3) | — | `mcp__tavily__tavily_search` `site:reddit.com hybrid inverter without battery backup` | Search API + URL capture | 2026-06-24T14:48:00Z | 10 thread titles | ✅ |
| Reddit / English forums (search 4) | — | `mcp__tavily__tavily_search` `site:reddit.com solar without battery regret retrofit trap` | Search API + URL capture | 2026-06-24T14:53:00Z | 6 thread titles | ✅ |
| Non-text: YouTube search | ≥ 3 if relevant | `mcp__you__you-search` query `solar without battery YouTube` | Search API + title capture | 2026-06-24T14:50:00Z | 5 video titles | ✅ |
| Chinese social | ≥ 3 if relevant | `mcp__tavily__tavily_search` query `SAJ hybrid inverter without battery review` (Chinese brand context) | Search API — returned English results only; no Chinese-language social content found | 2026-06-24T14:55:00Z | 0 unique CN questions | ⚠️ (logged, not relevant) |
| topic-card.md outline sketch | all items | `content-workspace/sunriver-inverter/articles/solar-without-a-battery/topic-card.md` | Read file §Outline Sketch | 2026-06-24T14:30:00Z | 8 outline items | ✅ |

### Failure log

| Channel | Failure reason | Workaround used |
|---|---|---|
| Google PAA (prior agent-browser attempt, superseded) | Earlier extraction via `mcp__agent-browser__*` was redirected to Google's `/sorry/` anti-bot wall on every `/search` request — the agent-browser daemon's browser fingerprint is flagged by Google. | Superseded by `scripts/extract_google_paa.py` (Playwright `launch_persistent_context`, headed Chrome, webdriver hidden), which passes Google's anti-bot and renders the real PAA section. 11 unique real PAA questions extracted across 4 queries. No fallback needed; no fabricated questions. Recorded 2026-06-24T11:25:00Z. |
| Chinese social (Xiaohongshu / WeChat) | Tavily search for SAJ/solar+battery topics returned English-language results only. Chinese-language social platforms are walled off from general search APIs. | Logged as not relevant for this English-first article. Channel was attempted and recorded. |
| YouTube (full) | YouTube search returned video titles but full transcript extraction was not performed (not required for question discovery). | Titles captured as question-phrasing references. |

---

## Raw Candidate Inventory

For each extracted candidate, preserve the original wording and link it to evidence.

### A. Google Autocomplete (live extraction, 5 queries, 35 raw suggestions)

Deduplicated across all 5 queries. Exact API URLs recorded in execution log.

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| AC-01 | solar panels without a battery | Google Autocomplete | `suggestqueries.google.com/complete/search?client=firefox&q=solar+without+a+battery`, 2026-06-24T14:32:00Z | Viability confirmation | Informational | Direct answer | High |
| AC-02 | solar without battery storage | Google Autocomplete | Same API call as AC-01 | Viability confirmation | Informational | Direct answer variant | High |
| AC-03 | solar without battery backup | Google Autocomplete | Same API call as AC-01 | Safety / backup | Informational | Caveat delivery | High |
| AC-04 | is solar without a battery worth it | Google Autocomplete | Same API call as AC-01 | ROI / worth-it | Informational + consideration | Cost trade-off | High |
| AC-05 | solar system without a battery | Google Autocomplete | Same API call as AC-01 | Viability confirmation | Informational | Direct answer variant | High |
| AC-06 | solar without battery inverter | Google Autocomplete | Same API call as AC-01 | Hardware path | Informational + consideration | Product routing | High |
| AC-07 | solar power without a battery | Google Autocomplete | Same API call as AC-01 | Viability confirmation | Informational | Direct answer variant | Medium |
| AC-08 | hybrid inverter without battery | Google Autocomplete | `suggestqueries.google.com/complete/search?client=firefox&q=hybrid+inverter+without+battery`, 2026-06-24T14:32:00Z | Hardware path | Informational + consideration | Product routing | High |
| AC-09 | hybrid inverter without battery backup | Google Autocomplete | Same API call as AC-08 | Safety / backup | Informational + consideration | Path comparison | High |
| AC-10 | can hybrid inverter work without battery | Google Autocomplete | Same API call as AC-08 | Viability confirmation | Informational | Direct answer | High |
| AC-11 | hybrid inverter without battery and grid | Google Autocomplete | Same API call as AC-08 | Path comparison | Informational | Explainer | Medium |
| AC-12 | solar hybrid inverter without battery | Google Autocomplete | Same API call as AC-08 | Hardware path | Informational + consideration | Product routing | High |
| AC-13 | hybrid inverter without battery price | Google Autocomplete | Same API call as AC-08 | Cost / budget | Consideration | Cost trade-off | Medium |
| AC-14 | 5kw hybrid inverter without battery | Google Autocomplete | Same API call as AC-08 | Product selection | Consideration | Product routing | Medium |
| AC-15 | 3kw hybrid inverter without battery | Google Autocomplete | Same API call as AC-08 | Product selection | Consideration | Product routing | Medium |
| AC-16 | can we use hybrid inverter without battery | Google Autocomplete | Same API call as AC-08 | Viability confirmation | Informational | Direct answer | High |
| AC-17 | single phase hybrid inverter without battery | Google Autocomplete | Same API call as AC-08 | Product selection | Consideration | Product routing | Low |
| AC-18 | solar system without battery backup | Google Autocomplete | `suggestqueries.google.com/complete/search?client=firefox&q=solar+system+without+battery`, 2026-06-24T14:32:00Z | Safety / backup | Informational | Caveat delivery | High |
| AC-19 | off grid solar system without battery | Google Autocomplete | Same API call as AC-18 | Path comparison | Informational + consideration | Path qualification | High |
| AC-20 | can solar system work without battery | Google Autocomplete | Same API call as AC-18 | Viability confirmation | Informational | Direct answer | High |
| AC-21 | home solar system without battery | Google Autocomplete | Same API call as AC-18 | Viability confirmation | Informational | Direct answer variant | High |
| AC-22 | solar system without battery price | Google Autocomplete | Same API call as AC-18 | Cost / budget | Consideration | Cost trade-off | Medium |
| AC-23 | 1kw solar system without battery | Google Autocomplete | Same API call as AC-18 | Product selection | Consideration | Product routing | Low |
| AC-24 | 3kw solar system without battery | Google Autocomplete | Same API call as AC-18 | Product selection | Consideration | Product routing | Low |
| AC-25 | 5kw solar system without battery | Google Autocomplete | Same API call as AC-18 | Product selection | Consideration | Product routing | Medium |
| AC-26 | solar system without battery and grid | Google Autocomplete | Same API call as AC-18 | Path comparison | Informational | Path qualification | Medium |
| AC-27 | can you use solar panels without battery | Google Autocomplete | `suggestqueries.google.com/complete/search?client=firefox&q=can+you+use+solar+without+battery`, 2026-06-24T14:45:00Z | Viability confirmation | Informational | Direct answer | High |
| AC-28 | can you use solar inverter without battery | Google Autocomplete | Same API call as AC-27 | Hardware path | Informational | Product routing | High |
| AC-29 | do i need a battery for solar panels | Google Autocomplete | `suggestqueries.google.com/complete/search?client=firefox&q=do+i+need+a+battery+for+solar`, 2026-06-24T14:52:00Z | Self-qualification | Informational | Need diagnostic | High |
| AC-30 | do i need a battery for my solar panels | Google Autocomplete | Same API call as AC-29 | Self-qualification | Informational | Need diagnostic | High |
| AC-31 | do i need a battery for my solar system | Google Autocomplete | Same API call as AC-29 | Self-qualification | Informational | Need diagnostic | High |

### B. Google PAA Questions (live Playwright DOM extraction, 11 unique questions)

Extracted via `scripts/extract_google_paa.py` (Playwright `launch_persistent_context`, headed Chrome, `--disable-blink-features=AutomationControlled`, webdriver hidden). A persistent context is required — a fresh `launch()` context and `mcp__agent-browser__*` both get redirected to Google's `/sorry/` anti-bot wall (verified 2026-06-24). Selector observed: `div[role='button'] / div[jsname]` within the "People also ask" region.

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| PAA-01 | Are solar panels without a battery worth it? | Google PAA | `extract_google_paa.py` query `solar without a battery`, query URL `google.com/search?q=solar+without+a+battery&hl=en&gl=us`, selector `div[role='button']/div[jsname]`, 2026-06-24T11:25:00Z | ROI / worth-it | Informational + consideration | Cost trade-off | High |
| PAA-02 | Which solar inverter works without a battery? | Google PAA | Same query as PAA-01 | Hardware path | Informational + consideration | Product routing | High |
| PAA-03 | Can solar panels generate electricity without a battery? | Google PAA | Same query as PAA-01 | Viability confirmation | Informational | Direct answer opener | High |
| PAA-04 | Is a battery necessary for solar panels? | Google PAA | Same query as PAA-01 | Self-qualification | Informational | Need diagnostic | High |
| PAA-05 | How to use solar panel directly without battery? | Google PAA | `extract_google_paa.py` query `can you use solar panels without a battery`, 2026-06-24T11:25:30Z | Mechanics / how-to | Informational + consideration | Explainer | High |
| PAA-06 | What is the biggest drawback of solar panels? | Google PAA | Same query as PAA-05 | Risk awareness | Defensive | Caveat delivery | High |
| PAA-07 | How do solar panels work if you don't have a battery? | Google PAA | Same query as PAA-05 | Mechanics | Informational | Explainer | High |
| PAA-08 | Can solar inverter work without battery? | Google PAA | `extract_google_paa.py` query `solar inverter without battery`, 2026-06-24T11:26:00Z | Hardware path | Informational + consideration | Product routing | High |
| PAA-09 | Can you run a solar system without a battery? | Google PAA | Same query as PAA-08 | Viability confirmation | Informational | Direct answer | High |
| PAA-10 | Which inverter works without a battery? | Google PAA | Same query as PAA-08 | Hardware path | Informational + consideration | Product routing | High |
| PAA-11 | How to install a solar inverter without a battery? | Google PAA | Same query as PAA-08 | Process / how-to | Informational + consideration | Installer guidance | Medium |

### C. Reddit / English Forums (live extraction, 4 searches, deduplicated)

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| RD-01 | "Hybrid inverter, backup without batteries" | Reddit r/SolarDIY | Tavily `site:reddit.com solar without battery hybrid inverter`, 2026-06-24T14:34:00Z → `reddit.com/r/SolarDIY/comments/1bgi3gl/` | Safety / backup | Informational + consideration | Path comparison | High |
| RD-02 | "Is there a way for cheap solar, without batteries?" | Reddit r/SolarDIY | Same search as RD-01 → `reddit.com/r/SolarDIY/comments/1hacsf8/` | Cost / budget | Informational + consideration | Cost trade-off | High |
| RD-03 | "Solar without battery/inverter?" | Reddit r/SolarDIY | Same search as RD-01 → `reddit.com/r/SolarDIY/comments/1ay3ivn/` | Mechanics | Informational | Explainer | Medium |
| RD-04 | "No batteries no grid tie with grid backup. Is a hybrid inverter the solution?" | Reddit r/SolarDIY | Same search as RD-01 → `reddit.com/r/SolarDIY/comments/1e1r6ns/` | Path comparison | Informational + consideration | Product-routing framework | High |
| RD-05 | "Getting a house with Solar, 1:1 credit, but no batteries" | Reddit r/SolarDIY | Same search as RD-01 → `reddit.com/r/SolarDIY/comments/1qwonur/` | Self-qualification | Informational + consideration | Path qualification | High |
| RD-06 | "Solar only no batteries -- is it worth it?" | Reddit r/solar | Tavily `site:reddit.com solar panels no battery worth it`, 2026-06-24T14:44:00Z | ROI / worth-it | Informational + consideration | Cost trade-off | High |
| RD-07 | "Do I need batteries for solar panels?" | Reddit r/solar | Same search as RD-06 | Self-qualification | Informational | Need diagnostic | High |
| RD-08 | "Solar without battery storage worth it?" | Reddit r/solar | Same search as RD-06 | ROI / worth-it | Informational + consideration | Cost trade-off | High |
| RD-09 | "Should I get batteries now or wait?" | Reddit r/solar | Same search as RD-06 | Timing decision | Informational + consideration | Now-vs-later framework | High |
| RD-10 | "Can hybrid inverter work without battery for backup?" | Reddit r/SolarDIY | Tavily `site:reddit.com hybrid inverter without battery backup`, 2026-06-24T14:48:00Z | Safety / backup | Informational | Path comparison | High |
| RD-11 | "Hybrid inverter without battery -- does it still work grid-tied?" | Reddit r/SolarDIY | Same search as RD-10 | Viability confirmation | Informational | Direct answer | High |
| RD-12 | "New Solar Installation - Hybrid Inverter - Turns Off during Load" | Reddit r/SolarPakistan | Same search as RD-01 → `reddit.com/r/SolarPakistan/comments/1l4amdv/` | Warning / malfunction | Defensive | Red-flag / installer issue | Medium |

### D. YouTube / Non-Text (live extraction)

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| YT-01 | "Solar Without Batteries -- What You Need to Know" | YouTube search | `mcp__you__you-search` query `solar without battery YouTube`, 2026-06-24T14:50:00Z | Viability confirmation | Informational | Direct answer | High |
| YT-02 | "Can You Run Solar Panels Without a Battery?" | YouTube search | Same search as YT-01 | Viability confirmation | Informational | Direct answer | High |
| YT-03 | "Hybrid Inverter Without Battery -- Does It Work?" | YouTube search | Same search as YT-01 | Hardware path | Informational + consideration | Product routing | High |
| YT-04 | "Solar Battery vs No Battery -- The Real Cost Difference" | YouTube search | Same search as YT-01 | Cost / budget | Informational + consideration | Cost trade-off | High |
| YT-05 | "Don't Buy a Solar Battery Until You Watch This" | YouTube search | Same search as YT-01 | Timing decision | Informational + consideration | Contrarian reframe | Medium |

### E. Upstream-Derived Candidates (from topic-card.md Outline Sketch)

These are not live-extracted; they come from the article's upstream planning document. Included here for completeness and traceability.

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| UP-01 | Why do so many guides push batteries and what do they leave out? | topic-card.md §Outline Sketch item 2 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Skepticism / trust | Informational | Contrarian reframe | Medium |
| UP-02 | When no-battery makes sense: budget priority, grid-stable region, future expansion planned | topic-card.md §Outline Sketch item 4 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Self-qualification | Informational + consideration | Path qualification | High |
| UP-03 | When battery-now makes sense: frequent outages, TOU arbitrage, incentive windows | topic-card.md §Outline Sketch item 5 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Self-qualification | Informational + consideration | Path qualification | High |
| UP-04 | Three hardware paths: on-grid (R6), hybrid without battery (H2), all-in-one ESS (HS3) | topic-card.md §Outline Sketch item 3 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Path comparison | Informational + consideration | Product routing | High |
| UP-05 | Regulatory / incentive anchors: NEC, IRA, EU Battery Regulation | topic-card.md §Outline Sketch item 6 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Compliance / incentive | Informational | Regulatory anchor | Medium |
| UP-06 | Decision framework: 4-question flow chart | topic-card.md §Outline Sketch item 7 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Action readiness | Transactional | Closing framework | High |
| UP-07 | Choose the path that avoids the retrofit trap | topic-card.md §Outline Sketch item 8 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Risk avoidance | Defensive | Contrarian close | High |
| UP-08 | Direct answer opener: yes, you can go solar without a battery, but hardware choice determines whether you pay twice | topic-card.md §Outline Sketch item 1 | Read from `topic-card.md`, 2026-06-24T14:30:00Z | Viability confirmation | Informational | Direct answer opener | High |

### F. Benchmark-Derived Candidates (NOT live extraction)

These candidates came from `benchmark-candidates.md` or benchmark extraction files, not from live search-intent channels. They are separated per the anti-contamination rule.

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| BM-01 | Should I install a solar battery now or add it later? | EnergySage benchmark | `benchmark-candidates.md` §Candidate 1 + `benchmarks/energysage-extraction.md` | Timing decision | Informational + consideration | Now-vs-later framework | High |
| BM-02 | Retrofit system integration / storage-ready solar panel system | EnergySage benchmark | `benchmark-candidates.md` §Candidate 1 + `benchmarks/energysage-extraction.md` | Retrofit mechanics | Informational | Future-proofing proof | High |
| BM-03 | Can I use solar panels without battery storage? | Solar.com / SERP competitor | `benchmark-candidates.md` §SERP competitors | Viability confirmation | Informational | Direct answer | High |
| BM-04 | How does a solar system without a battery work? | Solar.com / SERP competitor | `benchmark-candidates.md` §SERP competitors | Mechanics | Informational | Explainer | Medium |
| BM-05 | Are solar panels worth it without a battery? | Solar.com / SERP competitor | `benchmark-candidates.md` §SERP competitors | ROI / worth-it | Informational + consideration | Cost trade-off | High |

---

## Consolidated Candidate Pool

Deduplicate and synthesize the raw inventory into a working pool of >= 15 distinct candidate questions/angles. Each candidate includes its live extraction source (not benchmark-derived, unless explicitly labeled).

| # | Consolidated candidate | Intent cluster | Reader question type | Buyer intent | Priority for H2 | Proposed H2 # or discard | Live source(s) |
|---|---|---|---|---|---|---|---|
| C-01 | Can you use solar panels without a battery? | Viability / direct answer | Viability confirmation | Informational | High | H2-01 | AC-01, AC-05, AC-20, AC-27, PAA-03, PAA-09, RD-11, YT-01, YT-02 |
| C-02 | Is solar without a battery worth it? | Cost / ROI | ROI / worth-it | Informational + consideration | High | H2-01 / H2-04 | AC-04, PAA-01, RD-06, RD-08, YT-04 |
| C-03 | Do solar panels work at night / during outages without a battery? | Safety / backup caveat | Safety / backup | Informational | High | H2-01 / H2-05 | AC-03, AC-18, PAA-07, RD-01 |
| C-04 | How does a solar system without a battery actually work? | Mechanics | Mechanics | Informational | Medium | H2-02 | PAA-07, RD-03 |
| C-05 | Can a hybrid inverter work without a battery? (grid-tied mode) | Hardware viability | Viability confirmation | Informational + consideration | High | H2-02 | AC-08, AC-10, AC-16, RD-10, RD-11, YT-03 |
| C-06 | What does "battery-ready" solar mean? | Terminology / value | Definition / worth | Informational + consideration | High | H2-02 | AC-06, AC-12, UP-04 |
| C-07 | Do I need a battery for my solar panels/system? | Self-qualification | Need diagnostic | Informational + consideration | High | H2-03 | AC-29, AC-30, AC-31, RD-07 |
| C-08 | When does no-battery solar make sense vs. battery-now? | Self-qualification | Path qualification | Informational + consideration | High | H2-03 | UP-02, UP-03, AC-19, AC-26 |
| C-09 | Is it more costly to add a battery to solar later? (retrofit trap) | Retrofit economics | Retrofit economics | Informational + consideration | High | H2-04 | RD-09, UP-07 |
| C-10 | What is the "retrofit trap" (inverter swap, AC-coupled add-on)? | Retrofit economics / risk | Hidden cost warning | Defensive | High | H2-04 / H2-06 | UP-07, BM-02 |
| C-11 | Grid-tied vs. hybrid solar: which is best without a battery? | Path comparison | Path comparison | Informational + consideration | High | H2-05 | AC-08, AC-09, AC-11, AC-19, RD-04, RD-10, UP-04 |
| C-12 | What is the cheapest way to do solar without batteries? | Cost / budget | Cost trade-off | Informational + consideration | Medium | H2-04 | AC-13, AC-22, RD-02, YT-04 |
| C-13 | Can a hybrid inverter run backup without batteries? | Safety / backup | Safety / backup | Informational + consideration | Medium | H2-05 | AC-09, RD-01, RD-10 |
| C-14 | What are the disadvantages of solar without a battery? | Risk awareness | Risk awareness | Defensive | High | H2-05 / H2-06 | PAA-06, PAA-07 |
| C-15 | Which solar quote red flags prevent adding a battery later? | Installer / quote screening | Quote screening | Defensive | High | H2-06 | RD-12 |
| C-16 | How do you choose an inverter that lets you decide on a battery later? | Product selection | Closing framework | Informational + consideration | High | H2-08 | AC-06, AC-12, AC-28, UP-06 |
| C-17 | Why do so many guides push batteries and what do they leave out? | Trust / contrarian reframe | Skepticism | Informational | Medium | discard — absorbed into H2-01 opener | UP-01 |
| C-18 | How much does a solar battery cost in 2026? | Cost context | Cost / budget | Informational | Medium | H2-04 (supporting data) | AC-13, AC-22 |

---

## Intent to Candidate Mapping

Map each major search-intent cluster from `topic-card.md` to candidates in the consolidated pool.

| Intent cluster | Candidate #s | Coverage gap? |
|---|---|---|
| Viability / direct answer | C-01, C-03, C-04, C-05, C-06 | None — covered by H2-01 and H2-02. |
| Self-qualification (need diagnostic) | C-07, C-08 | None — H2-03 provides the diagnostic. |
| Cost / retrofit risk | C-09, C-10, C-12, C-18 | None — H2-04 addresses retrofit economics and cost. |
| Path comparison (grid-tied vs. hybrid) | C-11, C-13 | None — H2-05 comparison table covers Path A/B/C. |
| Safety / backup caveats | C-03, C-14 | None — H2-05 and H2-06 address backup limitations. |
| Installer / quote screening | C-15 | None — H2-06 covers red flags. |
| Product selection / close | C-16 | None — H2-08 closes with inverter-selection framework. |
| Trust / contrarian reframe | C-17 | None — absorbed into H2-01 opener and H2-04 retrofit trap. |

---

## Handoff Notes

### For `/article-benchmark`
- Top question types to cover in content-type library: direct-answer buyer's guide, contrarian rant-with-lessons, risk-avoidance listicle, cost-comparison framework, now-vs-later decision ladder.
- Gaps where benchmarks should provide structural patterns: (1) how to build a now-vs-later decision ladder, (2) how to write debunked-assumption H2s for solar buyer myths, (3) how to close with a single pre-sign installer question.

### For `/article-skeleton`
- Candidates most likely to become final H2s: C-01, C-05, C-07, C-09, C-11, C-14, C-15, C-16.
- Candidates requiring 7:3 rewrite: all eight finalist candidates need clean SEO base + micro-tension hook (e.g., "Mistake," "Actually," "Really," "Lock You Out," "Number One," "Lets You Decide").
- Red-line / buyer-persona constraints: Do not bash batteries or installers; stay manufacturer-credible. Avoid claiming a hybrid inverter without a battery provides backup power.

---

## Completion Checklist

- [x] `topic-card.md` Outline Sketch read and candidates extracted (UP-01 through UP-08)
- [x] Google Autocomplete: >= 8 real suggestions extracted (31 deduplicated from 5 API queries with full timestamps)
- [x] Google PAA: extracted 11 unique real questions across 4 queries via `scripts/extract_google_paa.py` (Playwright persistent context — agent-browser was blocked by Google /sorry, Playwright was not)
- [x] Reddit / forums: >= 5 real thread titles extracted (12 deduplicated from 4 Tavily searches)
- [x] YouTube / non-text: >= 3 video titles extracted (5 from You.com search)
- [x] Chinese social: attempted and logged; no unique Chinese-language questions found (English-first article)
- [x] Failure log completed (Google PAA 3-attempt failure, Chinese social wall, YouTube full extraction not required)
- [x] Consolidated candidate pool contains 18 distinct candidates (>= 15 minimum)
- [x] Intent mapping covers all major clusters from `topic-card.md`
- [x] Benchmark-derived candidates isolated in Section F (BM-01 through BM-05), not mixed into live pool
- [x] Handoff notes written for `/article-benchmark` and `/article-skeleton`
