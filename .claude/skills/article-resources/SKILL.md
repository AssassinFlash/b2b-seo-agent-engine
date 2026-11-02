---
name: article-resources
description: "Use when: visual-spec.md and enriched-draft.md exist and you need to design and place curiosity-driven resource cards, reader-stage routing boxes, and verify inline internal link coverage. Produces resources.md and merges approved resource/routing modules into enriched-draft.md. Runs after /article-visual, before /article-faq."
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
---

# /article-resources

## Purpose

Resource cards and internal link blocks are not navigation furniture. They are **emotional turning-point and buyer-routing devices** that raise dwell time, internal-link CTR, and conversion.

> **Open-Ended Form Rule**: Shortcode boxes (`[su_box]`) and the two turning-point callout cards below are **baseline examples, not a rigid template**. Depending on the article's buyer journey, you may design interactive path-routing matrices, side-by-side "Which spec fits my site?" selector cards, downloadable/copyable spec sheets, or diagnostic callouts. Choose the form that best serves the reader's decision at that exact spot, and debate the choice with the operator at the Peer Co-Research pause.

This skill produces two layers:

1. **Curiosity-driven callout cards** — placed at the two golden emotional turning points (anxiety/trap reveal, and perfect-solution-after-readiness). Each card uses a suspense-heavy micro-copy formula that implies the reader will lose something by not clicking.
2. **Reader-stage routing layer** — inline links (placed during `/article-draft` per skeleton contracts) are inherited; reader-stage routing boxes (`[su_box]`) route the reader to the right next page based on where they are in their decision. Plus an inline link coverage map that verifies every skeleton-assigned internal link URL appears in the draft.

This skill runs **after** `/article-enrich` (which places visual markers and HTML expression blocks) and **before** `/article-faq` (which places FAQ accordions using `[su_accordion]`/`[su_spoiler]` shortcodes at cognitive friction points).

## Why a separate skill

Resource card generation has its own logic that does not belong inside `/article-enrich`:
- Enrich is about visual + HTML expression blocks at cognitive decision points.
- Resources is about **emotional turning-point callouts** + reader-stage routing + inline link contract compliance.

Mixing them dilutes both. This separation lets each layer be audited and iterated independently.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before resources work, verify:
- `project-profile.md` exists and `state.json` indicates `lockedProfile: true`.
- `enriched-draft.md` exists (visual markers already placed by `/article-enrich`).
- `skeleton.md` exists with per-section `Internal/external link requirements` contracts.
- `project-profile.md` §12 has the internal linking architecture / sitemap.

### Handoff Read (MANDATORY — complete before Phase 0)

| Upstream File | Extract | Used For |
|---|---|---|
| `enriched-draft.md` | Full article body with visual markers | Locating emotional turning points and reader-stage boundaries |
| `skeleton.md` | Per-section `Internal/external link requirements` | Building the inline link coverage map (which assigned URLs are already inline vs. need a card) |
| `project-profile.md` §12 | Internal linking architecture / sitemap | Selecting which existing site pages to link to |
| `project-profile.md` §5 | Red lines / brand stance | Card copy must not violate red lines (no installer-bashing, no fake scarcity) |
| `evidence-opinion-pack.md` Part 2 | Tier 1 facts and numbers | Suspense copy must be truth-bounded — real cost numbers, real failure modes |
| `benchmark-success-formula.md` | Borrowed callout patterns | Emulating how benchmarks place "related" hooks without copying their house style |

---

## Core Principle: Two Golden Turning Points

Resource cards are not scattered at every section boundary. They are placed at the two moments where the reader's emotion pivots:

### Turning Point 1 — Anxiety / Trap Reveal
**When:** immediately after the body exposes a hidden cost, industry trap, or risk the reader did not know about.
**Reader state:** "Wait, am I about to get hurt by this?"
**Card job:** channel the anxiety into a specific protective next-read.

Example trigger: the body just explained the $4,500 retrofit trap. The card appears right after, titled "Before You Wire It: Can Hybrid Inverters Run Without Batteries?" — channeling the reader's fear into a single protective read.

### Turning Point 2 — Perfect-Solution / Readiness
**When:** immediately after the body presents an attractive, complete solution and the reader is leaning toward committing.
**Reader state:** "This sounds great, should I just buy it?"
**Card job:** introduce the long-term / comparison question that a confident buyer should still ask.

Example trigger: the body just praised the All-in-One system. The card appears right after, titled "All-in-One vs. Modular: What Changes After Year 3?" — introducing a sober comparison before the impulse buy.

If the article does not have both turning points, place cards only where they genuinely exist. Do not manufacture fake anxiety.

---

## Core Principle: Suspense Micro-Copy (Three Formulas)

A resource card's link description is not a summary. It is a **suspense loop** that implies the reader loses something by not clicking. Use one of three formulas per card:

| Formula | Pattern | When to use |
|---|---|---|
| **A — Single lever / only fix** | "...here's the one setting you need to flip to avoid the $4,500 trap." | The linked page reveals a single actionable lever that prevents the loss just exposed. |
| **B — Crisis / failure warning** | "This chart shows which combinations fail (and void your warranty)." | The linked page exposes specific failure cases with consequences. |
| **C — Crowd-proof / majority mistake** | "Question #4 ('Can you add batteries later?') trips up 60% of buyers." | The linked page quantifies how many readers get this wrong. |

**Truth-bounded rule:** the suspense claim must be supportable. If the linked page does not actually contain the lever / failure chart / crowd statistic, soften the copy to a truthful teaser. Do not invent a "60% of buyers" figure the linked page cannot back. A real, weaker teaser beats a fake strong one — the bounce from a clicked-but-empty link is worse than a lower CTR.

---

## Core Principle: Visual Callout Format

Cards are not plain inline links. They are visual callout blocks:

```markdown
> ### ⚠️ [Card title]
>
> [One-line suspense intro that implies loss if not read]
>
> - **[Linked article title](/url)** — [suspense micro-copy, formula A/B/C]
> - **[Linked article title](/url)** — [suspense micro-copy]
```

- Use `>` blockquote to create visual separation.
- Use an Emoji sentinel (`⚠️` for risk/trap cards, `💡` for comparison/opportunity cards, `→` for routing cards) to signal card type at a glance.
- Bold the linked article title so it reads as a clickable entry point.
- One-line suspense intro above the bullets sets the stakes.

Keep to 2–3 cards per article. More than 3 dilutes the emotional impact of each.

---

## Core Principle: Reader-Stage Routing Boxes

Distinct from curiosity callout cards, routing boxes answer "I am at stage X — what do I read next?" Place at most 1–2 routing boxes, at section boundaries where the reader has just completed a decision and needs pattern/collection/process-page routing.

```html
<div class="b2b-mod-routing linker-article-check" style="margin:24px 0;padding:18px 22px;border-left:3px solid var(--md-gold-dark,#a88a4a);background:var(--journal-wash,rgba(201,169,98,0.12));border-radius:0 8px 8px 0;">
  <div style="font-weight:700;color:var(--md-gold,#c9a962);margin-bottom:8px;">Which Specification Path Fits Your Project?</div>
  <ul style="margin:0;padding-left:18px;color:var(--journal-ink,rgba(255,255,255,0.92));">
    <li><strong>Path A (Dry Commercial Interior):</strong> <a href="/laser-cut-panels/" title="Laser-Cut Stainless Steel Panels">Grade 304 Laser-Cut Panels (2.0–3.0 mm)</a></li>
    <li><strong>Path B (Coastal / Poolside / Wet Zone):</strong> <a href="/outdoor-privacy-landscape-screens/" title="Outdoor 316 Stainless Steel Privacy Screens">Grade 316 PVD Outdoor &amp; Landscape Screens</a></li>
    <li><strong>Path C (Custom Project Elevation):</strong> <a href="/inquiry/" title="Request a Custom Stainless Steel Screen Inquiry">Send CAD / Elevation for Shop-Drawing Review</a></li>
  </ul>
</div>
```

Routing boxes use neutral, navigational copy — not suspense. They are the "calm" companion to the curiosity cards' "heat." Routing boxes are visible by default (not collapsed), so they work better than accordions for final CTA routing. (Use `[su_box]` shortcodes only when `project-profile.md` explicitly requests Shortcodes Ultimate.)

---

## Core Principle: Inline Link Coverage Map

`/article-draft` was supposed to place inline links per the skeleton contracts. This skill verifies that coverage and fills gaps:

1. Read every `Internal/external link requirements` field from `skeleton.md`.
2. For each assigned internal URL, check whether it already appears as an inline link in `enriched-draft.md`.
3. Record a coverage map in `resources.md`:

| Skeleton-assigned URL | Inline in draft? | Covered by card? | Status |
|---|---|---|---|
| /product/h2-... | yes (H2-05) | — | covered |
| /can-hybrid-... | no | yes (card 1) | covered via card |
| /faq/ | no | no | gap — add inline or card |

4. For any gap, either add an inline link at the natural moment or fold the URL into a card. Every skeleton-assigned internal URL must appear somewhere in the enriched draft by the time this skill finishes.

---

## Phase 0 — Plan Preview

Before generating cards, present:

1. **Upstream Consumption Report** — what was read from each handoff file.
2. **Turning Point Map** — the 2 (or fewer) golden emotional turning points located in the body, with the trigger sentence for each.
3. **Card Plan** — for each turning point: card type (⚠️/💡), title, 1–2 linked articles, suspense formula (A/B/C), and the truth-bounded check for each suspense claim.
4. **Routing Box Plan** — where routing boxes go and what paths they route.
5. **Inline Link Coverage Map** — which skeleton-assigned URLs are already inline, which need cards, which are gaps.

Output the plan, then use the unified stop language and wait for explicit approval.

---

## Phase 1 — Generate resources.md and Merge into enriched-draft.md

Produce `articles/<article-slug>/resources.md` containing:

- **Turning Point Map** (reference)
- **Curiosity Callout Cards** — the 2–3 card blocks in ready-to-paste Markdown/Scoped HTML5, each with its trigger sentence and insertion position
- **Reader-Stage Routing Boxes** — the 1–2 routing blocks in ready-to-paste Scoped HTML5 (`<div class="b2b-mod-routing">`)
- **Inline Link Coverage Map** — the verification table
- **Publish-Pack Handoff Notes** — which cards were placed where in `enriched-draft.md`, and confirmation that all skeleton-assigned internal URLs are covered

Then **merge the approved resource cards, routing boxes, and any missing inline links into `articles/<article-slug>/enriched-draft.md`** so `enriched-draft.md` is complete entering `/article-faq` and `/article-publish-pack` (`validate_publish.py` enforces `merge:resources-or-faq`).

---

## Output

Create `articles/<article-slug>/resources.md` and update `articles/<article-slug>/enriched-draft.md` with the merged resource/routing modules.

Update `state.json`: `currentStage: article-resources`, `nextCommand: /article-faq`. Record `resources: articles/<article-slug>/resources.md` in the article entry.

---

## Hard Rules

- **Truth-bounded suspense.** Every suspense claim (the lever, the failure, the crowd statistic) must be supportable by the linked page or the evidence pack. If not supportable, soften to a truthful teaser. Never invent a percentage, a failure mode, or a "single fix" the linked page does not deliver.
- **No more than 3 curiosity cards, and NEVER repeat the same container format in consecutive H2s (Anti-Pattern-Fatigue Rule).** Do not paste identical `> ### → Related:` blockquotes at the end of every H2 section. Alternate between inline contextual anchors, Scoped HTML5 Bento/Split cards (`<div class="b2b-mod-...">`), compact horizontal link pills, and at most 1–2 blockquote callouts across the entire article.
- **No more than 2 routing boxes.** Routing is calm; too many break the prose rhythm.
- **Every skeleton-assigned internal URL covered.** By inline link, card, or routing box. Gaps must be closed before this skill finishes.
- **Host-Adaptive Container Syntax (`arch-dark-gold` / WordPress / External Tool Compatible).** Check `project-profile.md`: by default, output clean **Scoped Inline HTML5 cards (`<div class="b2b-mod-routing" style="...">`)** that render natively in WordPress (`arch-dark-gold` / LiveCanvas / Gutenberg), Astro, and external citation tools without plugin lock-in; use `[su_box]` shortcodes only when the project profile explicitly specifies Shortcodes Ultimate.
- **Red lines.** Card copy must not bash installers, fabricate scarcity, or violate `project-profile.md` §5.
- **Keep `enriched-draft.md` synchronized.** After writing `resources.md`, weave the approved cards and routing boxes into `enriched-draft.md` at their designated turning points so downstream stages inspect the complete enriched text.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，生成 resources.md
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit peer co-research consensus before generating `resources.md`.
