---
description: "Use when: all four QA gates pass and you need to place visual markers and HTML expression blocks at cognitive decision points. Produces enriched-draft.md and image-plan.md. Resource cards, routing boxes, and FAQ are handled by /article-resources and /article-faq (run after this skill)."
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
  - mcp__douyin__*
  - mcp__linkedin__*
  - mcp__mcp-server-chart__*
name: article-enrich
---

# /article-enrich

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before enrichment, verify: `project-profile.md`, `state.json` indicates `lockedProfile: true`, `draft.md`, and all 4 QA gates PASS (truth-qa.md, information-gain-qa.md, benchmark-drift-audit.md, reader-qa.md).

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `draft.md` | Full article body plus QA metadata (read in entirety, do not rely on memory) | Identifying cognitive decision points where an image, HTML expression block, table, or no visual would help the reader. Read `Draft Control Metadata` for context, but do not treat it as publishable prose or a place for images |
| `skeleton.md` | Per-section format type, section function, and **visual opportunity hints** | Matching article image roles and HTML expression families to section function, not forcing a visual slot into every H2 |
| `evidence-opinion-pack.md` Part 2 | Per-stage Tier 1 fact inventory with project references | Mapping project photos to the sections where those projects are cited |
| `evidence-opinion-pack.md` Part 2b (External Verification) | Photography references from Dezeen/ArchDaily research (if any were preserved) | Creative reference for image types and placement patterns — not for copying, for understanding what works |
| `project-profile.md` §10 | Source library inventory (project photos available) | Knowing what real photos exist vs. what needs placeholder/fallback |
| `project-profile.md` §12 | Internal linking architecture diagram | Reference only — accordion/resource card placement is now `/article-resources`'s job, not enrich's |

## Pre-Flight Source-Library Check (mandatory before Phase 0)

Before deciding what images the article can have, audit the actual assets available in `project-profile.md` §10.

### Procedure

1. List every real photo / visual asset mentioned in §10 with:
   - File name or case reference
   - Scene or subject (hotel, office, factory QC, finish swatch, etc.)
   - Whether permission is confirmed
2. Cross-reference the list against the visual opportunity hints from `skeleton.md` and the actual cognitive decision points in `draft.md`.
3. Produce a short **Asset Reality Report**:

```
Real project photos available: N
Factory/process photos available: N
Finish/detail photos available: N
No real asset available for: [list of planned visual opportunities]
```

### Decision Rules

- If a real photo exists for a planned visual opportunity -> the primary real-image route may be a real project photo.
- If **no** real photo exists for a planned opportunity -> **do NOT invent a source file path for the primary real-image route**. Mark the real-image route as `[NOT AVAILABLE - source missing]` or omit it entirely. Prioritize:
  - **HTML expression blocks** for decision, process, comparison, checklist, spec-card, or AIO answer moments.
  - **Text-only, table, or no visual** for sections where a visual would slow the reader.
  - **Detail diagram or external concept image** only when it improves the exact paragraph.
  - **Backup concept routes** only when a credible generic image supports the point without pretending to be a real project.
- If the entire source library is empty or §10 is missing → default to **HTML expression / table / no-visual decisions**, not fake project imagery, and flag in `state.json` that this article is "image-asset-constrained".

This check prevents enrich from producing an `image-plan.md` full of unfulfillable real-photo placeholders.

## Purpose

The draft body is pure prose — voice, structure, opinions. `Draft Control Metadata` is QA/control metadata and must not be copied into `enriched-draft.md` as article body. Enrichment adds the visual, interactive, and navigational persuasion layer WITHOUT touching the prose.

**Open-Ended HTML Structural Liveness Principle (打破“老三样”固化，让文章排版活跃不死板)**:
Static HTML infographics, curiosity callout cards (`[su_box]`), and FAQ accordions (`[su_accordion]`) are **only baseline examples, never the ceiling or a fixed 3-item checklist**. The primary goal of enrichment is to make the article **visually and structurally alive (`显得活跃、有呼吸感、不死板`)** by weaving diverse HTML-built structural blocks that break up monotonous Markdown prose. In Phase 0, propose varied HTML structural blocks tailored to THIS article's exact rhythm and content — and debate them with the operator during the Peer Co-Research pause. Examples from the open HTML repertoire include (and you should invent new HTML structures when the article calls for them):
- **Interactive Scenario Switchers & Bento Grids**: Zero-JS Pure CSS environment/application pill tabs (`<input type="radio"> + :checked`), 2×2 (max 2-column for `68ch`) Bento-Grid spec callout cards with oversized monospace metrics, pure CSS parameter toggles.
- **Contrast & Visual Tension Blocks**: Spec-Sheet Promise vs. Shop-Floor Reality split cards, Pass/Fail QC side-by-side loupe comparators, visual Safe-Zone / Failure-Zone gauge bars, layered cost-anatomy stacked bars.
- **Interactive Preset Comparators & Diagnostic Routers**: Above-the-fold 3-path self-router strips, Pure CSS radio-state payback/sizing/tolerance comparators, 3-step hardware path quizzes.
- **Forensic & Actionable HTML Cards**: Quote Red-Flag Annotators (line-by-line visual teardown of a supplier quote), Anti-Sell Disqualification boundary cards, Internal Champion 30-second CFO ledgers, `user-select:all` copyable RFQ / spec checklist blocks.

Five core jobs in this stage:

1. **Visual placement decisions** at cognitive decision points (`image-strategy` skill)
2. **Open-ended HTML interactive & visual expression modules** when a designed tool, calculator, diagnostic card, or visual explainer helps more than prose, photo, or table (`article-html-visuals` skill)
3. **Internal link blocks** — accordions, resource cards, reader-stage routing (`internal-linking` skill)
4. **Visual material candidates** when real external photos, product images, project scenes, or platform media are needed (`visual-material-hunt` skill)
5. **Image / HTML visual plans** so publish-pack can make final selections based on actual asset and render availability

Do NOT rewrite paragraphs. Do NOT change voice or structure. Only add visual, HTML expression, and navigational elements around the existing prose.

---

## Phase 0 — Plan Preview

1. **Upstream Consumption Report** (MANDATORY first item): confirm exactly what was read from upstream:
   - From draft.md: full article body read; `Draft Control Metadata` reviewed then excluded from enrichment copy. Cognitive decision points identified = [list specific paragraph locations, not section names]
   - From skeleton.md: per-section format types → maps to image roles (Opening Anchor→opening orientation, Detail→material, Proof→case study sections)
   - From evidence-opinion-pack Part 2: project photo inventory available per stage → what real photos exist vs. what needs placeholder
   - From project-profile §12: internal linking architecture → guides accordion/resource block placement
2. **Asset Reality Report** from Pre-Flight Source-Library Check: which real photos exist, which visual opportunities have no real asset, and how that changes the route plan
3. Visual mix control: exact working percentages for real images, HTML expression blocks, tables/no visual, and why those numbers fit this article
4. Visual opportunity map: which sections need images, HTML expression blocks, tables, or no visual, at what cognitive decision point
5. Planned image roles and HTML expression families per selected section
6. Accordion/resource block placement
7. Sample section selection for cold-start review

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for approval.

---

## Instructions

**[Differentiate]** This skill operates on layer 3 of the Imitate → Inject → Differentiate stack.

**Main context**: read the draft and skeleton, identify visual opportunity points and link placement points.

**Subagent for sitemap processing** (optional): if the sitemap needs fresh scraping, spawn a subagent and let it use the `search-toolbox` skill to choose the appropriate map/scrape tool.

**Subagent for visual material hunting** (optional but recommended when real-image/media routes depend on external assets): use `visual-material-hunt` to collect source-backed candidates before finalizing `image-plan.md`. Do not let failed headless marketplace pages block the search; follow the You/Apify/Scrapling routes in `search-toolbox`.

**Visual fit review**: when `visual-material-hunt` produces more than one credible candidate, use `article-visual-fit` before promoting candidates into `image-plan.md`. The review decides whether each candidate should be promoted, reserved, rejected, or sent to the operator as `needs-human`. Do not judge it as website imagery; judge whether it helps this article explain, prove, compare, orient, or pace the reader.

**HTML visual planning**: use `article-html-visuals` whenever the best expression is a decision card, comparison matrix, risk map, process strip, spec card, annotated explainer, AIO answer block, or static-render fallback. Do not bury HTML expression work inside `image-strategy` as a generic generated-image fallback.

**Skills to load**: `image-strategy` (article visual need, dynamic visual mix, image roles, and option logic), `article-html-visuals` (HTML expression blocks and render checks), `visual-material-hunt` (source-backed external image/media candidates when needed), `article-visual-fit` (lightweight fit review before candidates enter `image-plan.md`), `internal-linking` (link roles, inline/block/accordion, reader-stage routing, density controls), `search-toolbox` (tool selection and fallback logic for sitemap refresh and visual material sourcing).

---

### Cold-Start Sample Section (adapted from Codex_1118 S8.7)

Before enriching the full article, submit ONE section for review. Pick a section that:
- Contains a key image opportunity (opening anchor, comparison, or proof image)
- Or contains a key HTML expression opportunity (decision card, comparison matrix, process strip, spec card, AIO answer block)
- Benefits from an accordion or resource block
- Demonstrates the enrichment approach for the rest of the article

The sample MUST show:
1. One selected visual route: image placeholder, HTML expression marker, table/no-visual decision, or a mix if the section truly needs it.
2. The supporting option/selection note in `image-plan.md` or `html-visual-plan.md`, not a bloated block inside the prose.
3. One internal link block (inline, resource, or accordion) when it improves routing.
4. How the enriched section reads alongside the surrounding prose.

Use the unified stop language. Wait for approval. Do NOT proceed to full enrichment until the sample section is approved.

### Example Cold-Start Output

```markdown
### Stainless steel grade choice shapes everything

Grade 304 and Grade 316 stainless steel each serve a distinct exposure boundary. Grade 304 covers dry commercial interiors cleanly, while Grade 316 adds 2–3% molybdenum to resist chloride pitting in coastal lobbies and pool corridors.

<!-- html-visual: hv-01 material-choice-decision-card -->

For high-traffic hospitality spaces within 5 km of salt air, 3.0 mm Grade 316 with vacuum PVD titanium-nitride coating is the safer long-term specification.

**Related:** [Custom stainless steel screens for hospitality](/stainless-steel-screens/) · [Manufacturing and QC process](/manufacturing-process/)
```

Planning notes:
- `html-visual-plan.md`: `hv-01` is a material choice decision card using approved evidence IDs.
- `image-plan.md`: no forced photo for this section; detail photos remain reserve candidates only if they clarify finish or pattern density.
- `visual-render-check.md`: required only if the HTML block is generated or exported as a static fallback.

---

### Job 1 — Visual And HTML Expression Layer

Scan the draft and skeleton. For each cognitive decision point, choose the lightest helpful enrichment route:

- real image / verified asset
- external candidate image/media
- HTML expression block
- simple table or checklist
- no visual

Use the `image-strategy` 5-question gate before adding anything. Use `article-html-visuals` when the selected route is an HTML component.

**Asset-Aware Route Defaults**:
- If a real asset exists in `project-profile.md` §10 for this visual opportunity -> primary real-image route = real photo with actual source file path.
- If no real asset exists -> the real-image route must be marked `[NOT AVAILABLE - source missing]` or omitted. Default to:
  - **HTML expression blocks** for diagrams, processes, comparisons, decision trees, spec references, and AIO answer moments that need visual expression.
  - **Text/table/no visual** when the paragraph is already clear or rhythm would suffer.
  - **Detail diagram or external concept image** only when it clarifies the exact reader job.
- Never invent a real project photo file path or claim a stock/AI image is a real project photo.

**Density**: no default count. Choose an exact visual mix control and the number of opportunities based on article length, benchmark rhythm, asset reality, and reader need. Never one per H2.

**Placement rules**:
- Opening Anchor: near the opening only when it helps orientation; do not force it after H1
- Context images: in application sections, only if each shows a different design decision
- Detail images: near material/finish/process descriptions
- Comparison visuals: near comparison content
- Diagrams: near complex concepts (open area, mounting methods)
- Proof images: in QC/case study sections
- Never: inside strong opinion paragraphs in flow (let the argument land)

### Job 2 — Internal Link Blocks (MOVED to /article-resources)

Resource cards, reader-stage routing boxes, and inline link coverage verification are now `/article-resources`'s job, not enrich's. Enrich only places visual markers and HTML expression blocks. Do not generate `**Related:**` blocks, routing boxes, or the inline link coverage map here — that happens in the next stage.

If the draft already contains inline links (placed by `/article-draft` per skeleton contracts), leave them in place. `/article-resources` will verify coverage and fill gaps.

### Job 3 — Image And HTML Visual Plans

For every visual opportunity added to the enriched draft, create the appropriate planning entry:

| Visual Opportunity | Reader Job | Route | Candidate / Component | Fallback | Recommended |
|---|---|---|---|---|---|
| Opening Anchor: hotel lobby divider | orient reader | real image | Real Riyadh project photo or source-backed candidate | text-only opening | TBD at publish-pack |
| Detail: PVD color swatches | compare finish choices | HTML expression | comparison matrix or spec card | table-only | TBD at publish-pack |
| Process: QC workflow | explain proof gates | HTML expression | process strip with source IDs | bulleted list | TBD at publish-pack |
| ... | ... | ... | ... | ... | ... |

Use `image-plan.md` for image/photo/media routes. Use `html-visual-plan.md` for HTML expression blocks and render requirements. The `Recommended` column may remain "TBD at publish-pack" when final asset quality still needs review.

---

## Output

Create:
- `articles/<article-slug>/enriched-draft.md`
- `articles/<article-slug>/image-plan.md`
- `articles/<article-slug>/html-visual-plan.md` when HTML expression blocks are selected
- `articles/<article-slug>/visual-render-check.md` when static fallback or render verification is needed

Use `templates/image-plan.md`, `templates/html-visual-plan.md`, and `templates/visual-render-check.md` as the structures for those artifacts.

`enriched-draft.md` must exclude `Draft Control Metadata` from the publishable article body. If metadata is needed for audit continuity, summarize it in a non-publish note inside `image-plan.md`, not in the article copy.

Update `state.json`: `currentStage: article-enrich`, `nextCommand: /article-visual`.

---

## Examples

### Example 1: Enriching Draft with HTML Expression Blocks
输入: `/article-enrich content-workspace/steel-screen screen-article`
输出: `enriched-draft.md, image-plan.md, and optional html-visual-plan.md updated with selected visual routes.`

## Guardrails

- **HTML Formatting**: Ensure generated HTML/SVG visuals are article-compatible, readable, and covered by `visual-render-check.md` when rendering matters.
- **Mock Fallback**: If real factory assets are unavailable, outline precise technical schematics as backup Options B & C.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Present the enriched draft. Ask: are images, HTML expression blocks, tables, and links at the right decision points? Do the planned fallbacks feel useful rather than decorative? Any accordion block that feels like link-stuffing? Do NOT proceed to publish-pack until user confirms.
