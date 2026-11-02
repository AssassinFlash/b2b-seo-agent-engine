# B2B SEO Title Style

B2B SEO titles optimize for **search-intent match, SERP click-through, and AIO citation** — the opposite of emotional clickbait. The rules below are the B2B English counterpart to the data-backed title methodology (adapted from qiaomu-xinzhiyuan-title, which extracted rules from a 2688-article Chinese AI-media corpus). The methodology is reused; the signals are re-derived for B2B SEO.

## Guiding Principles

1. **Keyword-first, intent-matched.** The primary keyword appears in every title, front-loaded when natural. The title's verb matches the searcher's intent (a "how" question gets a how-answer; a "which" question gets a comparison).
2. **CTR is the gate, trust is the floor.** A title that nobody clicks is dead, no matter how rigorous. So every title must carry a real CTR hook. But the hook must be honest — B2B buyers (procurement, engineers, installers, founders) click clarity and a promised answer, then bounce on hype. The floor is: fact-bound, no invented claims, passes voice-and-humanization. Above the floor, maximize clickability with a genuine hook.
3. **One strong hook, not a stack.** A single CTR hook (number, loss, reframe, information-gap, list, comparison, timeliness) plus the keyword is the sweet spot. Stacking two or more hooks reads as hype and erodes the trust floor.
4. **Fact-bound.** Any number, spec, price, ranking, "first", or "best" in the title must be sourced from the draft or locked profile. The hook is built from real facts, not invented ones. No presupposed claims.
5. **SERP-fit length.** H1: 40–60 characters (tight band 24–42 for question forms). SEO `<title>`: 50–60 characters to avoid SERP truncation.

## Length Signals (B2B SEO)

- H1 question form: 24–42 characters is the tight, punchy, AIO-friendly band. Up to ~60 is acceptable for guide/comparison titles that carry multiple true hooks.
- SEO `<title>`: 50–60 characters. Beyond ~60, Google truncates with `...` in SERP. Under ~50 wastes SERP real estate.
- These targets are display-driven, not stylistic — they match how Google renders titles.

## Lexical Signals (what to use / avoid)

**Use (front-load the keyword):**
- The primary keyword, ideally in the first 3–5 words.
- Intent-matching verbs: *Can, How, Which, What, Should, Do, Is* (question intent); *vs, Compared, Best, Choose* (comparison intent); *Cost, Price, Much* (cost intent — only with a real number or range).
- One micro-tension word from the approved 7:3 vocabulary: *Actually, Really, Mistake, Costly, Number One, Lock You Out*.
- True specs/numbers when sourced: `98.2% availability`, `3 kW`, `2026`, `NEM 3.0`.
- Authority markers grounded in the profile: brand name, certification, case-study count.

**Avoid (voice-and-humanization + B2B trust):**
- Hype verbs and clichés: *unleash, revolutionize, game changer, skyrocket, super-charge, disrupt, transform, demystify* (overused), *ultimate, killer, insane*.
- Stacked superlatives: *The Best, Fastest, Cheapest* in one title.
- Vague emotion: *Shocking Truth About…*, *You Won't Believe…*.
- invented urgency: *Just Released*, *Breaking*, *Now* — unless the draft genuinely covers a fresh event.
- Clickbait question loops: *Is X the New Y?* when the article doesn't answer it.

> The hype words above are listed as an avoid-set for the agent. The project's banned-phrase validator scans files literally, so the agent should apply this list at generation time without pasting these words into titles.

## Title Shapes

### 1. Standard question (default)
```text
Can You [Primary Keyword]?
[Primary Keyword]: [direct answer fragment]
```
The cleanest intent match. Aligns with the 7:3 SEO base. Default recommendation for most articles.

### 2. Number-anchored
```text
[Primary Keyword]: [N] [units] [consequence]
[N] [units] of [Primary Keyword]: [what it means]
```
Use only when the draft has a true spec, count, or range. The number must be in the Fact Inventory.

### 3. Decision / comparison
```text
[Option A] vs [Option B]: Which [Primary Keyword] Is Right for You?
How to Choose [Primary Keyword]: [buyer's real decision]
```
For buyer's guides and X-vs-Y articles. Surfaces the decision the buyer is making.

### 4. Risk / mistake hook
```text
The Costly Mistake With [Primary Keyword] (And How to Avoid It)
[Primary Keyword]: What Actually Matters (and What Doesn't)
```
Uses one micro-tension word. For mistakes / risk-avoidance articles. One hook, not a pile.

### 5. Question-with-reframe
```text
[Common assumption] About [Primary Keyword]? Here's What Actually Happens
[Primary Keyword]: The [reframe] Most Buyers Miss
```
The reframe must be a real conclusion from the draft. Do not out-promise the H2s.

### 6. Restrained / E-E-A-T
```text
[Brand] [Primary Keyword]: What Works and What Doesn't
[Primary Keyword]: A [buyer role] Guide to [real scope]
```
Low-tension, authority-led. Often the best choice for spec-heavy B2B where the buyer distrusts hype (installers, engineers, procurement).

### 7. AIO-citable (declarative answer fragment)
```text
[Primary Keyword]: [direct declarative answer in ~40-55 chars]
Yes, You Can [Primary Keyword] — [one grounded qualifier]
```
For definitional intent where AIO / featured-snippet capture is the priority. Declarative, not interrogative.

## Model-Driven Candidate Evaluation Criteria (No Mechanical Regex Scoring)

Evaluate every candidate qualitatively using model judgment (never a rigid character-count script), checking how well it balances these signals for the specific query and B2B buying committee:

- [ ] **Primary keyword & intent spine**: primary keyword present and naturally front-loaded; verb matches search intent (how/which/what/can/should/vs)
- [ ] **SERP display fit**: typically 40–60 chars for H1 (or 24–42 tight question band) and 50–60 chars for `<title>`, adjusted naturally when a high-value spec or entity requires it
- [ ] **Single unmistakable CTR mechanism**: carries one genuine hook (number / loss / reframe / info-gap / list / comparison / timeliness) without stacking multiple hooks into clickbait
- [ ] **Buying Committee dual appeal**: commands respect from both the technical specifier (engineer/architect/installer) and the commercial approver (procurement/CFO/owner)
- [ ] **Strict Fact Boundary**: every number, spec, or comparative claim traces directly to the Fact Inventory in `draft.md` / `project-profile.md`
- [ ] **Trust register**: zero banned hype words; scope matches the actual H2s

## CTR Hook Library (English B2B)

These are the hooks that actually lift CTR in English B2B/SEO SERPs — they create curiosity, specificity, or loss aversion **without** emotional clickbait. Every Level 2+ title carries exactly one. The hook must be built from real facts in the Fact Inventory.

| Hook | Pattern | Example | Why it works |
|---|---|---|---|
| **Number (specific)** | `[Keyword]: The N [things] That Actually Work` | `Solar Without a Battery: The 3 Configurations That Actually Work` | Specificity = a promised, countable answer |
| **Number (counter-intuitive)** | `[N] [units] [surprising claim]` | `98% Uptime Without a Battery: How SunRiver Did It` | A surprising number creates curiosity |
| **Loss / risk** | `The Costly Mistake With [Keyword] (And How to Avoid It)` | `The Costly Mistake With Battery-Free Solar` | Loss aversion is the strongest CTR driver |
| **Reframe / contrarian** | `Why "[common belief]" Is Wrong (For Most Buyers)` | `Why "Solar Needs a Battery" Is Wrong for Most Buyers` | Counter-common-sense = curiosity gap |
| **Information gap** | `What [authority] Won't Tell You About [Keyword]` | `What Solar Installers Won't Tell You About Battery-Free Systems` | Information asymmetry drives clicks |
| **List / promise** | `[N] Things to Check Before [Keyword]` | `5 Things to Check Before Going Battery-Free` | List promise = known, bounded effort |
| **Comparison / decision** | `[A] vs [B]: The Real [Cost/Performance] Difference` | `Battery vs. No-Battery Solar: The Real Cost Difference` | Decision anxiety drives clicks |
| **Timeliness** | `[Keyword] in [Year]: What Changed` | `Solar Without a Battery in 2026: What Changed` | Freshness signal (only if the draft covers change) |

**Hook discipline:**
- One hook per title. A number hook already counts as the tension element — do not also add "Actually" or "Mistake".
- The hook must be true. `5 Things to Check` requires the article to actually have 5 things. `What Installers Won't Tell You` requires the article to deliver insider info.
- If the Fact Inventory is thin, use a question or reframing hook rather than inventing a number.

## Title Shapes

## Avoid

- two or more unsupported superlatives in one title
- hype words from the avoid list
- numbers, prices, rankings, or "first/best" not in the Fact Inventory
- emotional clickbait that would fail Reader QA
- title scope wider or narrower than the actual article
- `Just Released` / `Breaking` on evergreen content

## Intensity Levels (B2B-adapted, CTR-calibrated)

**Level 1 — restrained (E-E-A-T heavy, technical buyers):**
```text
[Keyword]: What Works and What Doesn't
[Brand] [Keyword]: A [buyer role] Guide
```
Use when the buyer distrusts any hook (e.g., an engineer reading a spec sheet). Low CTR ceiling but high trust. Not the default.

**Level 2 — CTR-optimized (DEFAULT):**
```text
[Keyword]: [one CTR hook built from a real fact]
Why "[common belief]" Is Wrong for Most [buyers]
[Keyword]: The N [things] That Actually Work
```
The default. One genuine CTR hook + keyword + fact. Maximizes clicks without breaking trust. Most articles should land here.

**Level 3 — high-tension (risk/mistake articles only):**
```text
The Costly Mistake With [Keyword] (And How to Avoid It)
[N] [units] [surprising loss claim]
```
Use only for mistakes/risk-avoidance articles where loss aversion is the article's actual thesis. One loss/risk hook, built from a real fact. Do not use Level 3 for evergreen definitional content.

**Default to Level 2.** Drop to Level 1 only for trust-sensitive technical buyers. Rise to Level 3 only for risk/mistake articles. Never stack hooks across levels.

## Why not emotional intensity (the B2B vs. media distinction)

The qiaomu skill's power words (`爆、杀疯、狂飙、封神、破防、血洗`) optimize WeChat朋友圈 point-through rate via emotional shock. B2B SEO titles optimize Google SERP CTR + AIO citation via **intent match + trust + clarity**. These goal functions diverge: emotional shock titles underperform in B2B SERPs because the searcher wants an answer, not a thrill, and because hype undermines the E-E-A-T trust signals B2B buyers rely on. This is why this skill reuses the methodology (data rules + variants + scoring + fact boundary) but rewrites every signal for B2B SEO.
