---
name: article-html-visuals
description: "Use when: an article needs embedded HTML expression blocks, visual explainers, decision cards, comparison modules, checklist cards, or static-render fallbacks that support reader understanding beyond ordinary images or Markdown tables."
user-invocable: false
---

# Article HTML Visuals

## Purpose

Provide the **HTML synthesis** branch of the visual pipeline. `/article-visual` has already decided that a given visual should be HTML-synthesized rather than searched or image-to-image-generated. This skill gives the implementation patterns and engineering constraints for that HTML block:

- how to structure the HTML,
- how to keep it article-readable rather than slide-like,
- how to capture it as a static WebP or animated GIF when needed,
- and how to keep the data and labels truth-bounded.

This skill is reference logic. `/article-visual` is the controlling skill that writes the spec and decides when HTML synthesis is the right path.

## What This Skill Owns

| Owns | Does Not Own |
|---|---|
| HTML expression strategy for article moments | Sourcing external photos |
| Component type choice: card, matrix, explainer, flow, checklist | Deciding whether a marketplace image is trustworthy |
| Fixed-canvas or responsive embed specification | Rewriting article prose |
| Static fallback needs: screenshot, PNG/WebP, alt, caption | Publishing live WordPress changes |
| Render QA notes for readability and rhythm | Fabricating data or project proof |

Use `visual-material-hunt` for external image/media candidates, `article-visual-fit` for candidate usefulness, and `image-strategy` for overall visual placement.

## Inputs

- `draft.md` or `enriched-draft.md`: exact paragraph, section function, and reader moment.
- `skeleton.md`: section contracts and visual opportunity hints.
- `evidence-opinion-pack.md`: facts, buyer risks, project proof, and numbers allowed in visuals.
- `benchmark-success-formula.md`: rhythm, visual density, and answerability style to preserve.
- `image-plan.md`: existing visual opportunities and fallback decisions.
- `project-profile.md`: brand/positioning constraints and source-library reality.

## Outputs

Create these only when HTML visuals are actually selected:

- `html-visual-plan.md`: planning artifact for each HTML expression block.
- `html-visuals/<visual-id>.html`: self-contained embeddable HTML block or fixed-canvas visual.
- `visual-render-check.md`: render/readability review, including screenshot or static fallback notes when available.

HTML visual files are optional publish assets, not required for every article.

## Trigger Gate

Create an HTML visual only when at least one is true:

1. The reader must compare options that prose alone makes slow.
2. A decision rule, process, checklist, risk map, or specification card would reduce uncertainty.
3. AIO capture would benefit from a compact answer block that is still human-readable.
4. A real photo would be decorative or misleading, but a visual explanation would be useful.
5. The article's benchmark uses visual or modular rhythm that the current draft lacks.

Skip HTML visuals when the paragraph's force depends on uninterrupted prose, when a simple table is clearer, or when the component repeats a module already used in the article.

## Instructions

1. Read the exact article moment, not just the section heading.
2. Name the reader job: decide, compare, trust, act, or understand faster.
3. If prose, a simple table, or a real photo is better, do not create an HTML visual.
4. Choose one component family and output mode.
5. Record the decision in `html-visual-plan.md`, including evidence IDs and fallback needs.
6. If producing HTML or a static fallback, create/update `visual-render-check.md`.
7. Keep implementation details in `references/` or `html-visuals/`; keep the article body light.

## Component Families (Open-Ended Repertoire — Not a Closed Menu)

The families below are starting archetypes, **not a fixed checklist**. Do not default to the same static card + table + accordion trio across articles. Design or invent the specific interactive/visual component that best resolves the buyer's exact cognitive friction at that paragraph:

| Family | Best Use | Article Example |
|---|---|---|
| Interactive Calculator / Estimator | Buyer needs to plug in their own numbers (size, load, budget, ROI) | Sizing/wattage calculator, retrofit cost penalty estimator |
| Diagnostic Quiz / Path Router | Buyer needs 2-4 questions to route into Path A / B / C | 3-step inverter or material grade selector |
| Quote Red-Flag Annotator | Expose hidden traps inside a real-looking vendor quote or spec sheet | Annotated installer quote showing where battery-ready lock-in hides |
| Forensic Pass/Fail QC Comparator | Show what good vs. defective manufacturing looks like up close | Weld seam / PVD coating / PCB potting pass vs. fail callout |
| Copyable RFQ / Interrogation Card | Give the buyer exact questions or spec clauses to copy-paste to suppliers | 5-line RFQ clause block with `user-select:all` selectable styling |
| Decision Card | One recommendation with why/when/not | Choose stainless steel over glass when glare and cleaning cycles matter |
| Comparison Matrix | 2-5 options across concrete criteria | Grade 304 vs Grade 316 stainless steel across exposure zones |
| Risk Map | What can go wrong and how to avoid it | Pattern density vs daylight vs privacy |
| Process Strip | Sequential workflow with proof gates | Sample approval -> production -> QC -> packing |
| Spec Card | Dense specification made scannable | Gauge, open area, finish, mounting method |
| Annotated Explainer | Object anatomy or callout diagram | Floor track, ceiling bracket, panel, anchor |
| AIO Answer Block | Direct answer plus qualifiers | Best divider material for high-traffic commercial interiors |
| Custom Article-Specific Module | Any novel interactive/visual widget invented for this article's unique tension | Document the custom reader job and interaction logic in `html-visual-plan.md` |

See `references/html-expression-patterns.md` for implementation patterns.

## Design Policy

Borrow the useful parts of `frontend-slides`, adapted for articles:

- **Show first**: when style is subjective, produce 2-3 compact visual directions in `html-visual-plan.md` instead of describing style abstractly.
- **Controlled canvas**: use a fixed design canvas only when a static screenshot/fallback is needed. For article embeds, prefer responsive max-width blocks.
- **Self-contained & Zero-JS for Mode A**: inline scoped CSS (`.b2b-mod-*`); never reference external CDN libraries, Google Fonts, or `<script>` in Mode A inline article embeds (blocked by host CSP `script-src 'self'`, `font-src 'self'`). Chart libraries may only be used in Mode B offline Playwright screenshot synthesis.
- **One reader job**: each component must make one decision, comparison, or concept easier.
- **Article rhythm wins**: a beautiful block that interrupts benchmark pacing should be rejected or moved.
- **Data discipline**: every number must trace to Tier 1/Tier 2 evidence or be labeled as a qualitative judgment.

## Canvas And Output Modes (Two Strict Engineering Contracts)

Every HTML visual MUST follow one of two strict engineering contracts depending on how it enters the article:

| Mode | When to Use | Mandatory Engineering Contract | Verification Command |
|---|---|---|---|
| **Mode A: Scoped Inline HTML5 Snippet (Default — Direct Article Embed)** | Interactive Scenario Tabs, Bento Spec Grids, Spec-vs-Reality Split Cards, Preset Calculators, Quote Red-Flag Annotators, CFO Ledgers, Copyable RFQ Cards | **NO `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, external `cdn.tailwindcss.com`, `fonts.googleapis.com`, `<script>`, or `onclick/oninput` attributes!** Host CSP (`script-src 'self'`, `font-src 'self'`) blocks all inline JS and external fonts. Use **Pure CSS State Machines** (`<input type="radio"> + :checked` or `<details><summary>`) inside `<div class="b2b-mod-<id>">` with 100% `.b2b-mod-<id>`-prefixed CSS selectors and max 2 columns (`minmax(220px,1fr)`). | `python3 scripts/render_html_visual.py html-visuals/<id>.html --validate-snippet` |
| **Mode B: Canvas Screenshot / GIF HTML** | Complex multi-node flow schematics or Chart.js canvases intended to be exported as a static `.webp` (`<100KB`) or `.gif` (`<500KB`) image | Wrap the visual inside `<div class="b2b-canvas-card" style="max-width: 960px; ...">`. Export via DOM-selector cropping (never full browser viewport). | `python3 scripts/render_html_visual.py html-visuals/<id>.html --render visual/<id>.webp --selector .b2b-canvas-card` |

Do not write full-page `<html>...<body class="bg-dark">...` files and pretend they are inline article embeds — full-page HTML breaks WordPress/CMS themes and forces everything back into static screenshots.

## Plan Format

```markdown
# HTML Visual Plan - <article slug>

## Selected HTML Expression Blocks

| ID | Placement | Reader job | Component family | Evidence source | Output mode | Render check |
|---|---|---|---|---|---|---|
| hv-01 | after material comparison paragraph | compare options fast | Comparison Matrix | T1-01, T1-03 | responsive embed + screenshot fallback | required |

## Rejected Opportunities

| Placement | Why skipped |
|---|---|
| opening paragraph | prose already creates the scene; visual would slow entry |
```

## Render Check

For each selected block, record:

- Desktop width: readable, no overlap, no clipped labels.
- Mobile width: either responsive or intentionally static with clear fallback.
- Static fallback: screenshot path or reason none is needed.
- Article rhythm: where it appears and why it does not break the argument.
- Accessibility: alt/aria label or nearby text equivalent.
- Evidence: numbers and claims traced to source IDs.

## Render Engineering (critical for GIF / WebP export)

When an HTML visual needs to become a GIF or a static WebP, the export path is part of the spec — not an afterthought.

### DOM-selector cropping, not viewport capture

Do **not** record the browser viewport. Viewport capture creates black bars, inconsistent margins, and cropped labels. Instead, lock onto the outermost visual card/container (for example the `.max-w-5xl` card wrapper) and measure its actual DOM size. Export only that container.

### Animation denoise rules

GIFs have severe frame-rate constraints. Therefore:
- Keep only the animation that teaches the point (typically direction arrows or a slider-driven state change).
- **Remove dashed-line flow animations.** `stroke-dasharray` / `stroke-dashoffset` patterns flicker at 15fps and make small labels unreadable.
- Prefer solid lines + a moving arrowhead or a subtle opacity pulse.
- If the visual contains small text (model names, voltage labels, spec annotations), prefer **static WebP** over GIF.

### Recommended export settings

| Output | Settings |
|---|---|
| GIF | 15fps, 3-4s loop, target <500KB, DOM-selector crop |
| Static WebP | DOM-selector screenshot, quality ~90%, target 30-100KB |
| Interactive HTML | Responsive embed, no external JS/CDN unless truly needed |

### Why these rules matter

A multimodal AI can create a beautiful HTML mockup that becomes unreadable when exported badly. This section exists so the exported asset preserves the learning value the HTML had on-screen.

## Common Mistakes

- Turning every table into a designed component.
- Building a slide inside an article.
- Using animation because the tool can, not because the reader learns faster.
- Letting the component restate the paragraph instead of adding comprehension.
- Using fake numeric precision or unverified percentages.
- Treating HTML visuals as mandatory. They are powerful, but optional.
