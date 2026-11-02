---
name: article-faq
description: "Use when: resources.md exists (resource cards and routing placed by /article-resources) and you need to generate the FAQ section that converts reader objections into action. Produces faq.md and merges friction-targeted objection modules (Scoped HTML5 details/summary accordions or decision cards) with conclusion-first answers and objection-to-CTA handling into enriched-draft.md. Runs after /article-resources, before /article-publish-pack."
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

# /article-faq

## Purpose

An FAQ / Objection-Resolution layer is not a knowledge-base appendix. It is a **conversion layer that clears the objections standing between the reader and the CTA**. Every question targets a real friction point the reader hits after reading the body, and every answer removes that friction while steering toward the recommended product or contact action.

> **Open-Ended Form Rule**: Grouped `[su_accordion]`/`[su_spoiler]` blocks are **one possible rendering format**, not a mandatory mechanical template. When an objection is better resolved by a ledger-style cost breakdown card, an interactive myth-vs-reality toggle, a side-by-side DIY-vs-Pro risk table, or a copyable installer-verification script, use the format that resolves the buyer's friction most effectively (while still exporting clean Q&A pairs for `FAQPage` JSON-LD schema).

This skill produces `faq.md` — a set of friction-targeted objection modules placed at cognitive friction points, with conclusion-first answers that give specific numbers (not "it depends") and resolve into a natural CTA.

This skill runs **after** `/article-resources` (curiosity cards and routing) and **before** `/article-publish-pack` (which packages everything and generates FAQPage schema from this file).

## Why a separate skill

FAQ generation has its own logic that does not belong inside `/article-enrich` or `/article-publish-pack`:
- Enrich is about visual + HTML expression blocks.
- Publish-pack is about SEO metadata, schema, and keyword records.
- FAQ is about **friction mapping, conclusion-first copywriting, and objection-to-CTA conversion** — a distinct copywriting discipline.

Mixing them dilutes the FAQ's conversion job. This separation lets the FAQ be audited and iterated against its own success metric: does it remove the objections that block the CTA?

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before FAQ work, verify:
- `project-profile.md` exists and `state.json` indicates `lockedProfile: true`.
- `enriched-draft.md` exists with visual markers and resource cards placed.
- `resources.md` exists (resource cards and routing already designed).
- `evidence-opinion-pack.md` exists (for specific numbers in answers).
- `project-profile.md` §5 (red lines) and §12 (CTA target) exist.

### Handoff Read (MANDATORY — complete before Phase 0)

| Upstream File | Extract | Used For |
|---|---|---|
| `enriched-draft.md` | Full article body + resource card positions | Locating cognitive friction points and avoiding overlap with resource cards |
| `resources.md` | Card positions and routing boxes | Ensuring FAQ groups land at different friction points than the resource cards |
| `skeleton.md` | Secondary Heading Library FAQ candidates + per-section link contracts | Seed questions and internal links to reference in answers |
| `evidence-opinion-pack.md` Part 2 | Tier 1 facts, costs, specs, tax-credit figures | Conclusion-first answers with extreme specificity (real numbers, not "it depends") |
| `project-profile.md` §5 | Red lines / brand stance | Answers must not bash installers or fabricate scarcity |
| `project-profile.md` §12 | CTA target / recommended products | Steering each objection resolution toward the CTA |
| `intent-research.md` | User Language Bank + PAA questions | Phrasing questions in the reader's real words |

---

## Core Principle 1: Friction-Targeted Questions

Do not ask soft awareness questions ("Is solar good?"). Ask the questions the reader is actually wrestling with **after reading the body, before acting**:

| Friction type (Peep Laja / Alex Hormozi B2B Risk-Reversal Taxonomy) | Example question |
|---|---|
| **Implementation & Site-Fit Friction** | "Can a 3.6m panel be anchored without drilling marble slabs?" / "How long does installation take?" |
| **Trust, QC & Crating-Damage Friction** | "What happens if a PVD panel arrives scratched or warped?" / "How do I verify 316 vs 304 on delivery?" |
| **Financial, TCO & CFO-Approval Friction** | "Why does vacuum PVD cost 20% more than powder coat, and what is the 5-year replacement math?" |
| **MOQ, Sample & Lead-Time Friction** | "Can I order a physical PVD sample swatch before locking a 50-panel custom run?" |
| **Compatibility & Spec-Boundary Friction** | "Can I add batteries later to this exact model?" / "What open-area ratio keeps HVAC return velocity under noise limits?" |

Source the questions from: the User Language Bank in `intent-research.md`, the PAA questions, and the reader-journey friction points implied by the body.

---

## Core Principle 2: Conclusion-First + Extreme Specificity

Every answer must:

1. **Lead with a bold conclusion in the first sentence** — a direct Yes/No, a specific number, or a specific duration. Never open with "It depends on many factors."
2. **Give extreme specificity** — real numbers, real dollar ranges, real durations, real percentages. If the evidence pack has the number, use it. If the number is a draft-born estimate, label it as a reference range and keep it truth-bounded.
3. **Use a "ledger-style" comparison** when the question is about cost or DIY — show the math that makes the recommended choice the obvious one.

Example (bad): "Installation time varies depending on your system and home."

Example (good): "**Typical residential install: 2–3 days for modular systems, 1–2 days for all-in-one.** Permitting adds 2–8 weeks depending on your city. Work from home? Most installation happens outside — only 1–2 hours indoors for electrical work."

Example (ledger-style, good): "DIY saves $3,000–$5,000 on labor but loses the 30% federal tax credit ($8,000–$12,000) because only licensed installers qualify. DIY also voids equipment warranties. Unless you are a licensed electrician, the math points to professional installation."

If the article lacks a specific number, **supplement with a truthful industry reference range** and label it as such. Never invent a precise figure the evidence cannot support.

---

## Core Principle 3: Objection-to-CTA Handling

Every answer's final move is to steer the reader toward the CTA — not with a hard sell, but by making the recommended path the obvious resolution of the objection.

- Implementation friction → resolves to "a professional installer handles this" → CTA: contact / product page.
- Trust friction → resolves to "the recommended hardware has a documented warranty" → CTA: product page for warranty details.
- Financial friction → resolves to "the tax credit + avoided retrofit cost makes the recommended path cheaper" → CTA: quote / contact.
- Compatibility friction → resolves to "the recommended model is specifically battery-ready" → CTA: product page.

The steering must feel earned by the answer's logic, not bolted on.

---

## Core Principle 4: Grouped Placement at Cognitive Friction Points

FAQ groups are not dumped at the article end. Each group is placed at the cognitive friction point where its questions become live:

| FAQ group | Placement |
|---|---|
| **Implementation & Getting Started** | After the section where the reader first imagines installing the system |
| **Long-Term Cost & Incentives** | After the section where the reader has done the ROI math and is weighing long-term risk |

Use host-native **Scoped HTML5 `<details class="b2b-mod-faq">` + `<summary>` accordions** (zero internal blank lines inside `<details>...</details>` for `wpautop` safety) so the page stays clean and the reader expands only the question that matches their current friction. (Use `[su_accordion]`/`[su_spoiler]` shortcodes only if `project-profile.md` explicitly requests Shortcodes Ultimate.)

Coordinate with `resources.md` so that a resource card and an FAQ group do not both land on the same sentence. Resource cards raise curiosity; FAQ groups resolve objections — they belong at different moments.

---

## Core Principle 5: Scoped HTML5 FAQ Accordion Format (`#md-blog-single` Dark-Gold Native)

```html
<div class="b2b-mod-faq-group" style="margin:28px 0;">
  <div style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--md-gold,#c9a962);margin-bottom:12px;">Quick Answers: [Friction Group Topic]</div>
  <details class="b2b-mod-faq" style="margin:10px 0;padding:14px 18px;border:1px solid var(--journal-line,rgba(255,255,255,0.14));border-radius:8px;background:var(--journal-panel,#1a1a1a);">
    <summary style="cursor:pointer;font-weight:700;color:var(--md-gold,#c9a962);">[Friction-targeted question in buyer's real words]?</summary>
    <p style="margin:10px 0 0;color:var(--journal-ink,rgba(255,255,255,0.92));"><strong>[Conclusion-first answer sentence with the specific number / Yes-No verdict.]</strong> [Ledger-style elaboration or risk-reversal proof, ending with an earned internal link such as <a href="/inquiry/">requesting a shop-drawing review</a>.]</p>
  </details>
</div>
```

- Keep zero blank lines (`\n\n`) inside `<div class="b2b-mod-faq-group">...</div>` so CommonMark Type-6 / `arch-dark-gold` / `wpautop` never splits the HTML block.
- Bold the first sentence only (the BLUF conclusion).
- Keep answers to 2–4 sentences. Longer answers belong in the body, not the FAQ.
- Each answer links to either the relevant H2 (in-page anchor) or a canonical internal page (`/patterns/`, `/manufacturing-process/`, `/inquiry/`, or `href="#open-quote"`) — never a bare `#`.

---

## Phase 0 — Plan Preview

Before generating `faq.md`, present:

1. **Upstream Consumption Report** — what was read from each handoff file.
2. **Friction Map** — the 4–6 friction points identified, grouped into 2 FAQ groups, each with its cognitive placement point and the resource-card positions to avoid overlapping.
3. **Question + Answer Sketch** — for each FAQ: the question (in reader words), the conclusion-first first sentence (with the specific number), and the CTA it steers toward.
4. **Truth-Bounded Check** — for each specific number in the answers, the source (evidence pack, draft-born estimate labeled as reference, or industry range labeled as such).

Output the plan, then use the unified stop language and wait for explicit approval.

---

## Phase 1 — Generate faq.md and Merge into enriched-draft.md

Produce `articles/<article-slug>/faq.md` containing:

- **Friction Map** (reference)
- **FAQ Group 1** — heading + Scoped HTML5 `<details class="b2b-mod-faq">` Q&A blocks, with the insertion position noted
- **FAQ Group 2** — heading + Scoped HTML5 `<details class="b2b-mod-faq">` Q&A blocks, with the insertion position noted
- **Objection-to-CTA Trace** — for each FAQ, which CTA it resolves toward
- **Truth-Bounded Ledger** — every specific number and its source
- **Publish-Pack Handoff Notes** — FAQPage schema JSON-LD will be generated by `/article-publish-pack` from these Q&A pairs; flag any answer whose specific number is a draft-born estimate so Truth QA can verify or soften

Then **merge the approved FAQ blocks into `articles/<article-slug>/enriched-draft.md`** at their designated cognitive friction points so `enriched-draft.md` is complete and ready for `/article-publish-pack` (`validate_publish.py` enforces `merge:resources-or-faq`).

---

## Output

Create `articles/<article-slug>/faq.md` and update `articles/<article-slug>/enriched-draft.md` with the merged FAQ modules.

Update `state.json`: `currentStage: article-faq`, `nextCommand: /article-publish-pack`. Record `faq: articles/<article-slug>/faq.md` in the article entry.

---

## Hard Rules

- **Friction-targeted.** No soft awareness questions. Every question must target a real objection that blocks the CTA.
- **Conclusion-first.** First sentence is bold and gives a specific Yes/No, number, or duration. Never "it depends."
- **Extreme specificity.** Real numbers from the evidence pack, or labeled reference ranges. No vague ranges ("thousands") when a real one exists.
- **Truth-bounded.** Every specific number traces to a source. Draft-born estimates are labeled as reference ranges and flagged for Truth QA.
- **Objection-to-CTA.** Every answer resolves toward the recommended product or contact action, earned by the answer's logic.
- **Grouped at friction points.** FAQ groups land at cognitive friction points, not dumped at the end. Coordinate with `resources.md` to avoid overlap.
- **No bare `#` links.** Every link in an answer is a real internal URL or a real in-page anchor to an H2.
- **Host-Adaptive Accordion Syntax (`arch-dark-gold` / WordPress / External Tool Compatible).** Check `project-profile.md`: by default, output clean **Scoped HTML5 `<details class="b2b-mod-faq" style="...">` + `<summary style="...">` accordions** so the article renders natively in WordPress (`arch-dark-gold` / LiveCanvas / Gutenberg), Astro, and external citation tools without displaying raw bracket codes; use `[su_accordion]`/`[su_spoiler]` shortcodes only when `project-profile.md` explicitly requests Shortcodes Ultimate.
- **Red lines.** No installer-bashing, no fabricated scarcity, no fake statistics.
- **Do not edit enriched-draft.md.** This skill produces `faq.md` only. Merge happens downstream.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，生成 faq.md
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit peer co-research consensus before generating `faq.md`.
