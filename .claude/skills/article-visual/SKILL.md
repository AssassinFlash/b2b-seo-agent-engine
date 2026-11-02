---
name: article-visual
description: "Use when: enriched-draft.md has visual markers placed by /article-enrich and you need to produce an executable visual spec for a multimodal AI (Gemini, etc.) to search and synthesize assets. Produces visual-spec.md with per-visual acquisition strategy (search / image-to-image AI generation / HTML synthesis), format judgment, design system, and truth-bounded constraints. You write the spec; the multimodal AI executes the search; candidates come back to you for judgment and embedding. Runs after /article-enrich, before /article-resources."
argument-hint: '[content-workspace/project-slug] [article-slug]'
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Agent
  - mcp__apify__*
  - mcp__crawl4ai__*
  - mcp__firecrawl__*
  - mcp__plugin_playwright_playwright__*
---

# /article-visual

## Purpose

You have full article context. You know exactly what visual each section needs, what data it should show, and why. This skill turns that knowledge into an **executable visual specification** that a multimodal AI can act on without guessing.

The workflow is a **Dual-Mode Local Execution + Multimodal Engine**:
1. **You** produce `visual-spec.md` — detailed, per-visual, execution-level specs.
2. **For Path 3 (HTML Synthesis — Scoped Inline Snippets & Canvas Visuals)**: You build the HTML files directly in `html-visuals/`, validate inline snippets with `python3 scripts/render_html_visual.py <file.html> --validate-snippet`, and render static `.webp`/`.png` fallbacks via Playwright DOM-selector cropping (`python3 scripts/render_html_visual.py <file.html> --render visual/<id>.webp --selector .b2b-canvas-card`).
3. **For Path 1 (Search)**: You execute `visual-material-hunt` + `python3 scripts/apify_research.py` locally to gather real candidate assets into `visual-asset-candidates.md` / `visual-material-library.html` (or hand `visual-spec.md` to an external multimodal agent when requested).
4. **For Path 2 (Image-to-Image AI generation)**: You prepare the real base image + forensic img2img prompt so the operator or multimodal AI can synthesize the composite, then judge (`promote / reserve / reject / needs-human`) and embed.
5. **For local/generated assets that will be uploaded to WordPress**, you create `asset-upload-checklist.md` so the operator can upload them and then hand you the final media URLs for replacement.

## Why a separate skill

Visual spec production is a distinct discipline from enrich (which places markers), resources (which places curiosity cards), or faq (which places objection-resolution). It requires deep article context to determine what each visual should show, what format, where to find it, and how to synthesize it if not found.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before visual spec work, verify:
- `enriched-draft.md` exists with visual markers placed by `/article-enrich`
- `skeleton.md` exists with per-section visual opportunity hints
- `evidence-opinion-pack.md` exists for truth-bounded spec numbers
- `project-profile.md` exists for design system and AI tool config

### Handoff Read (MANDATORY)

| Upstream File | Extract | Used For |
|---|---|---|
| `enriched-draft.md` | Full article body + visual marker positions + surrounding prose | Determining what each visual needs to show based on the exact paragraph it serves |
| `skeleton.md` | Per-section visual opportunity hints + link requirements | Initial visual opportunity map + link targets to include in visuals |
| `evidence-opinion-pack.md` Part 2 | Tier 1 specs, costs, model numbers | Truth-bounded visual content — real specs, not invented |
| `benchmark-success-formula.md` | Hook Distribution Map + Copyable Execution Rules | How benchmarks use visuals |
| `project-profile.md` | Design system + AI tool config + search platform matrix | Visual design consistency + acquisition constraints |
| `intent-research.md` | Golden Keyword Map + User Language Bank | Visual labels and annotations in reader-native language |

---

## Three Acquisition Paths

Every visual spec must declare one primary acquisition path plus fallbacks.

| Path | When | Key constraint |
|---|---|---|
| **Search** | Real product photos, install shots, official diagrams, social media | Must use Apify-first (`scripts/apify_research.py` / Actors) + denoise + cap volume + extract video frame timestamps |
| **Image-to-image AI generation** | Need to scene-ize a real product photo, compose two real photos, or enhance a low-quality real photo | **Base image is mandatory.** No pure text-to-image. The base must be a real product photo. AI only scene-izes, composes, or enhances. Prefer **Forensic Specificity** (annotated tolerances, workshop environment, pass/fail QC callouts) over glossy plastic renders. |
| **HTML synthesis** | Open-ended interactive calculators, diagnostic quizzes, quote red-flag annotators, data visualizations, technical schematics, animated flow diagrams | HTML source stored in `html-visuals/`; Playwright recording uses DOM-selector cropping, not viewport |

**Fallback chain:** Search then image-to-image AI (requires real base) then HTML synthesis then markdown table/text.

**Hard rule:** Pure text-to-image AI generation is **forbidden** in B2B articles. Every AI-generated visual must have a real product photo as its base input.

Read `references/acquisition-paths.md` for the full decision logic, multi-channel matrix, denoise word bags, video frame extraction, AI prompt constraints, and Playwright recording parameters.

---

## Format Judgment

Every visual spec must declare its output format.

| Format | Use when | Key constraint |
|---|---|---|
| **Static WebP** | Contains small text that must be sharp on mobile | Under 100KB; capture from clean HTML via Playwright DOM-selector screenshot |
| **Animated GIF** | Needs to show energy flow or dynamic interaction | Under 500KB; 15fps; only direction arrows, no dashed-line flow |
| **Interactive HTML** | Needs user interaction (sliders, toggles) | Must degrade gracefully; WordPress-compatible |
| **Markdown table** | Data already structured, needs no visual enhancement | Already in draft; no additional asset needed |
| **Real photo** | Actual product/installation photo | Must attribute source; alt text required |

Read `references/format-judgment.md` for the full decision matrix and common mistakes.

---

## Design System

Visual style must be consistent across all visuals in the article and across all articles in the project.

Key defaults (override only if profile says otherwise):
- Dark background (`var(--md-bg-deep, #141414)` / `var(--md-bg, #1a1a1a)`)
- Warm gold/accent highlight (`var(--md-gold, #c9a962)` / `var(--md-gold-dark, #a88a4a)`)
- System monospace font stack for labels and specs (`ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` — never external Google Fonts due to CSP `font-src 'self'`)
- Neon glow effect for interactive elements
- Flat technical diagram style, not 3D render

Read `references/design-system.md` for the full spec including colors, typography, animation rules, and Chart.js defaults.

---

## Phase 0 — Plan Preview

Before producing `visual-spec.md`, present:

1. **Upstream Consumption Report** — what was read from each handoff file
2. **Visual Opportunity Audit** — for each visual marker in `enriched-draft.md`:
   - The surrounding paragraph and its cognitive job
   - What the visual needs to show (detailed content brief, not a one-liner)
   - Whether the original enrich marker intent was correct or needs correction
3. **Acquisition Path Plan** — for each visual: primary path plus fallback chain plus rationale
4. **Format Plan** — for each visual: output format plus technical parameters
5. **Design System Confirmation** — verify against `project-profile.md`

Output the plan, then use the unified stop language and wait for explicit approval.

---

## Phase 1 — Produce visual-spec.md

For each visual opportunity, produce a spec block using `templates/visual-spec.md` as the structure. Register all new assets in the project visual library using `templates/visual-library-index.md` as the index format. Each spec must include:

- **Position**: section, exact paragraph it follows, cognitive job
- **Visual content**: detailed description of layout, elements, labels, data, flow direction. A paragraph or structured list that a multimodal AI can act on.
- **Format**: output type, dimensions, file size target, file path
- **Acquisition strategy**: Priority 1 (search with keywords, platforms, denoise, volume cap, video frames) then Priority 2 (image-to-image with base image, prompt, constraints) then Priority 3 (HTML synthesis with data source, animation, recording) then fallback
- **Design**: background, accent, font, style
- **Truth-bounded check**: every spec number, model name, interface count traces to evidence

---

## Phase 2 — Candidate Judgment (after multimodal AI returns assets)

When candidates come back from the multimodal AI:

1. For each candidate, judge:
   - **Promote**: meets spec, embed in `enriched-draft.md` replacing the marker
   - **Reserve**: meets spec but better exists; keep in visual library
   - **Reject**: does not meet spec; discard
   - **Needs-human**: ambiguous without human eyes

2. For promoted candidates:
   - Copy the asset to `articles/<article-slug>/visual/`
   - Replace the visual marker in `enriched-draft.md` with actual embed syntax
   - Update `visual-spec.md` with final asset path and status

3. For all candidates (promoted or reserved):
   - Register in `visual-library/library-index.md` with tags, source, and usage record

---

## Project-Level Visual Library

The visual library is project-level, not per-article. Reusable, incremental, dynamic.

```
content-workspace/<project-slug>/
├── visual-library/
│   ├── product-shots/
│   ├── install-photos/
│   ├── diagrams/
│   ├── animations/
│   ├── ai-generated/
│   └── library-index.md
└── articles/<article-slug>/
    └── visual/
```

When a new article generates a new asset, it goes into the library for future reuse. When a new article needs an asset, check the library first before searching.

---

## Output

Create:
- `articles/<article-slug>/visual-spec.md` — the executable spec document
- `articles/<article-slug>/asset-upload-checklist.md` — upload manifest for any local/generated assets that must be moved into WordPress media before publish

Update (after Phase 2):
- `articles/<article-slug>/enriched-draft.md` — replace markers with actual asset embeds
- `content-workspace/<project-slug>/visual-library/library-index.md` — register new assets

Update `state.json`: `currentStage: article-visual`, `nextCommand: /article-resources`. Record `visualSpec` path in the article entry.

---

## Hard Rules

- **No pure text-to-image.** Every AI-generated visual must have a real product photo as its base input.
- **Truth-bounded visuals.** Every spec number, model name, interface count must trace to the evidence pack.
- **Specs are executable.** A multimodal AI reading `visual-spec.md` must know exactly what to search, what to synthesize, what format, and what constraints without guessing.
- **Design system from profile.** Visual style comes from `project-profile.md`, not invented per-article.
- **Library is project-level.** Assets are reusable across articles. Check library before searching.
- **Do not search yourself.** This skill produces the spec. The operator hands it to a multimodal AI. Candidates come back for your judgment.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，进入下一阶段
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit peer co-research consensus before generating or finalizing `visual-spec.md`.
