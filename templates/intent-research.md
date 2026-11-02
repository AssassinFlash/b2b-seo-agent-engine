# Search Intent Research

**Article:** `<article-slug>`  
**Project:** `<project-slug>`  
**Stage:** `/article-intent-research`  
**Date:** `<YYYY-MM-DD>`  

---

## Search Intent Summary

| Field | Value |
|---|---|
| Primary keyword | `<from topic-card.md>` |
| Search intent (from topic-card) | `<informational / comparison / transactional / risk-avoidance>` |
| Reader promise | `<what the article must deliver>` |
| Key decision moments | `<list 2-4>` |
| Chinese-market relevance | `<yes / no / optional>` |
| Non-text relevance | `<yes / no / optional>` |

---

## Research Execution Log

Every live channel must be verifiable. Record the exact query URL, tool, method, and timestamp. Inferred candidates cannot be labeled as live-extracted.

| Channel | Minimum | Tool / URL used (Mandatory Apify-First) | Extraction method | Timestamp | Candidates extracted | Status |
|---|---|---|---|---|---|---|
| Google PAA | ≥ 4 | `python3 scripts/apify_research.py` (`apify/google-search-scraper`) + `extract_google_paa.py` / Playwright real Chrome | Apify SERP/PAA extraction + Browser DOM (`div[data-q]`) |  |  |  |
| Google Autocomplete | ≥ 8 | `https://suggestqueries.google.com/complete/search?client=firefox&q=...` (or Apify Autocomplete Actor) | HTTP API / Apify Actor |  |  |  |
| Reddit / English forums | ≥ 5 | `python3 scripts/apify_research.py` (`apify/google-search-scraper` `site:reddit.com <topic>`) + Crawl4AI/Tavily | Apify Search/Scraper + URL capture |  |  |  |
| Chinese social (Xiaohongshu / WeChat) | ≥ 3 if relevant | `python3 scripts/apify_research.py` / `agent-reach` / platform search | Apify / Platform scraper + URL capture |  |  |  |
| Non-text questions (YouTube / podcast titles) | ≥ 3 if relevant | `python3 scripts/apify_research.py` (`streamers/youtube-scraper` or Google `site:youtube.com`) | Apify Scraper / Search API + URL capture |  |  |  |
| topic-card.md outline sketch | all items | `content-workspace/<project>/articles/<slug>/topic-card.md` | Read file |  |  |  |

### Failure log
If any channel could not be extracted, record why here. Do not silently omit.

| Channel | Failure reason | Workaround used |
|---|---|---|
|  |  |  |

---

## Raw Candidate Inventory

For each extracted candidate, preserve the original wording and link it to evidence.

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |

**Required evidence format:**
- Google PAA: exact query URL + DOM selector used.
- Google Autocomplete: exact API URL used.
- Reddit: exact search query + thread URL(s).
- Chinese social: platform + search query + post URL(s).
- Non-text: platform + search query + media URL(s).

---

## Consolidated Candidate Pool

Deduplicate and synthesize the raw inventory into a working pool of ≥ 15 distinct candidate questions/angles.

| # | Consolidated candidate | Source | Extraction evidence | Intent cluster | Reader question type | Buyer intent | Priority for H2 | Proposed H2 # or discard |
|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |

> **Source** = the live channel name or upstream file path this candidate came from (must match a Raw Candidate Inventory row). **Extraction evidence** = URL + method + timestamp for live channels; file path + section for upstream files. These two columns preserve the traceability chain from the Raw Inventory into the consolidated pool — do not drop them.

---

## Golden Keyword / Phrase Map

3-10 phrases with unusual pulling power. These are not necessarily the highest-volume keywords; they are the phrases that carry attention, uniqueness, demand satisfaction, or timeliness. They feed `/article-title`, `/article-skeleton`, and `/article-draft` opener work.

| Phrase | Source | Why it matters (attention / uniqueness / demand / timeliness) | Search intent | Click / dwell mechanism | Use in title / H2 / opener / body / FAQ |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## User Language Bank

Raw reader wording and objection language. Use real user language when available. If the row comes from PAA/Autocomplete rather than a comment/forum, label it as `search-surface wording`, not `user comment`.

| Raw wording | Source URL / channel | Emotion | Underlying anxiety | Reusable wording |
|---|---|---|---|---|
|  |  |  |  |  |

## SERP Consensus Target (SERP 同行套话共识靶子 — Information Gain 反推)

Extract the 3–5 repetitive claims/platitudes shared across current SERP Top 5 pages so our article can directly dismantle, qualify, or deepen them.

| # | What SERP Top 5 Repeat in Unison (Consensus Platitude) | Why It Is Incomplete / Misleading for Real Buyers | Our Contrarian / Tier 1 Counter-Move | Target H2 |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |

## SERP Table-Stakes vs. Incremental Entities (必含基础实体防漏网)

Ensure differentiated framing does not omit foundational industry entities that buyers and search engines expect every authoritative guide on this query to cover.

| Entity / Concept | Layer (`table-stakes` \| `incremental`) | Source / SERP Evidence | Why it matters to buyer intent | Planned H2 / section |
|---|---|---|---|---|
|  |  |  |  |  |

## SERP Top 5 Visual & Structural Weaponry Audit (SERP 视觉与版式武器库对标矩阵)

Audit the structural and visual elements used by the current Top 5 ranking pages so `/article-skeleton` and `/article-enrich` can design richer, more alive HTML structural blocks that visually outclass the SERP:

| Rank & URL | Tables Count | Visual / Diagram Types Used | Interactive / HTML Blocks Present? | Structural Weakness / Monotony We Can Exploit |
|---|---|---|---|---|
| #1 | | | | |
| #2 | | | | |
| #3 | | | | |
| #4 | | | | |
| #5 | | | | |

## Peer Co-Research Calibration Notes (对等共研与校准点)

- **Suspect angles or potential blind spots for joint debate**:
- **Open questions where divergent operator/AI search can verify or challenge**:

## Intent → Candidate Mapping

Map each major search-intent cluster from `topic-card.md` to candidates in the consolidated pool.

| Intent cluster | Candidate #s | Coverage gap? |
|---|---|---|
| `<e.g., definition>` |  |  |
| `<e.g., comparison>` |  |  |
| `<e.g., cost/risk>` |  |  |
| `<e.g., process/how-to>` |  |  |

---

## Handoff Notes

### For `/article-benchmark`
- Top question types to cover in content-type library: `<list>`
- Gaps where benchmarks should provide structural patterns: `<list>`

### For `/article-skeleton`
- Candidates most likely to become final H2s: `<list #s>`
- Candidates requiring 7:3 rewrite: `<list #s>`
- Any red-line or buyer-persona constraints: `<list>`

---

## Completion Checklist

- [ ] `topic-card.md` Outline Sketch read and candidates extracted
- [ ] Google PAA: ≥ 4 real questions extracted with URL + method
- [ ] Google Autocomplete: ≥ 8 real suggestions extracted with API URL
- [ ] Reddit / forums: ≥ 5 real thread titles extracted with search query + URLs
- [ ] Chinese social / non-text channels attempted (if relevant) and logged
- [ ] Failure log completed (or explicitly empty)
- [ ] Consolidated candidate pool contains ≥ 15 distinct candidates
- [ ] Intent mapping covers all major clusters from `topic-card.md`
- [ ] Handoff notes written for `/article-benchmark` and `/article-skeleton`
