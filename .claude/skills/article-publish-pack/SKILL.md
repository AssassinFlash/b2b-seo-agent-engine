---
description: "Use when: all four QA gates pass and you need to create the publish-ready SEO, WordPress, schema, link, image, and keyword-record package."
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
name: article-publish-pack
---

# /article-publish-pack

## Instructions

**Main context**: read all 4 QA outputs (must all PASS), coordinate the publishing pipeline.

**Subagent-appropriate work**: 
- Package creation → spawn **publish-readiness-agent** to generate the 5 publish artifacts
- Final verification → spawn **publish-package-qa** to validate everything before WordPress deployment

**Skills to load**: `publish-package`.

**Available MCP tools**: None required — all inputs are local artifacts.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`. If either value is missing, stop and ask for the missing path or article slug.

Before packaging, verify:

- `project-profile.md` exists
- `project-profile.json` exists
- `state.json` exists
- `state.json` indicates `lockedProfile: true`
- `enriched-draft.md` exists
- `html-visual-plan.md` exists if the article uses embedded HTML expression blocks
- All 4 QA gate files exist and are not blocked:
  - `truth-qa.md`
  - `information-gain-qa.md`
  - `benchmark-drift-audit.md`
  - `reader-qa.md`

If the locked profile is missing, only allow profile skills.

## Purpose

Turn the final draft into a publishable package:
- **H1 + SEO title** — run `/article-title` first to generate, score, and select the title (produces `title-options.md`). Do not write the title as an afterthought; it drives CTR and AIO citation. Then derive Meta Description and slug from the selected title + primary keyword.
- Publishable article body only. Exclude any `Draft Control Metadata`, QA notes, control vectors, repair notes, or verifier tables from the final copy.
- WordPress preview checklist
- Image/media final selection: choose final image/media routes from `visual-spec.md` and the project `visual-library/`; do not regenerate visual strategy from scratch.
- HTML visual finalization: if the selected route is HTML synthesis, verify each embedded component, static fallback need, alt/aria text, and article rhythm. Create or update `visual-render-check.md` when a render/static fallback decision matters.
- Internal links (Outbound + Inbound Retro-Link Checklist via `scripts/update_link_graph.py`)
- External links & External Tool Citation Handoff Slots
- Schema snippets / `schema.json` — include **Named Technical Author (`author`) and Technical Reviewer (`reviewedBy`)** credentials from `project-profile.md` (with jobTitle, worksFor, knowsAbout) alongside `Article` and `FAQPage` JSON-LD to maximize E-E-A-T entity graph signals.
- Long-term keyword asset record
- **FAQ merge**: merge `faq.md` (produced by `/article-faq`) into `enriched-draft.md` at the cognitive friction points specified in `faq.md`. Generate FAQPage schema JSON-LD from the faq.md Q&A pairs.
- **Resources merge**: merge `resources.md` (produced by `/article-resources`) callout cards and routing boxes into `enriched-draft.md` at the positions specified in `resources.md`.
- **Link coverage verification**: verify that every internal link URL assigned in `skeleton.md` contracts appears at least once in the final `enriched-draft.md` (inline, card, or routing). Block if gaps remain.
- **FAQ verification**: verify `faq.md` exists with ≥ 5 Q&A pairs and that the FAQ groups are placed at cognitive friction points (not dumped at the end). Route back to `/article-faq` if missing.
- **Asset upload checklist verification**: verify `asset-upload-checklist.md` exists, and every local/generated asset in it has either (a) an uploaded WordPress media URL filled in, or (b) a documented reason why it remains local for non-publish use. Final publishable files must contain **no local `visual/...` paths** once upload is complete.
- **Publish Gate Preflight**: Run `python3 scripts/validate_publish.py content-workspace/<project-slug> <article-slug>` before creating any publish artifacts, and abort on a non-zero exit. A `PreToolUse` hook (`scripts/hooks/publish_gate.py`) enforces the same step-and-verdict check on `Write` and `Edit` for `publish-package.md`, `wordpress-preview-check.md`, `schema.json`, and `keyword-record.csv`.
- **Experience Recirculation (经验回流机制)**: You MUST run the following bash command to automatically extract all verified claims from `truth-qa.md` and sync them to `knowledge/fact-library.json` (with `used_in_articles` and `usage_count` anti-footprint tracking):
  ```bash
  python3 scripts/sync_draft_born_claims.py content-workspace/<project-slug> <article-slug>
  ```
  This prevents system amnesia and allows future articles to select least-used facts first.
- **Bi-Directional Site Link Graph (全站双向内链图谱与旧文回链清单)**: Run:
  ```bash
  python3 scripts/update_link_graph.py content-workspace/<project-slug> <article-slug>
  ```
  to update `knowledge/site-link-graph.json` and include the resulting **Inbound Retro-Link Checklist (《旧文回链清单》)** in `publish-package.md` (which existing articles should add an internal link pointing to this new article).
- **Full Copy-Paste Draft Assembly & Scoped HTML Verification (单文件完整正文组装与沙盒校验)**: Run:
  ```bash
  python3 scripts/assemble_publish_draft.py content-workspace/<project-slug> <article-slug>
  ```
  This automatically:
  1. Strips internal `## Draft Control Metadata` so internal QA vectors never leak into the publishable copy,
  2. Verifies and inlines Scoped HTML5 Snippets (`html-visuals/<id>.html`) while blocking any full-page `<html>`/`<body>`/`cdn.tailwindcss.com` pollution,
  3. Extracts all `{{CITE: claim | query}}` slots into the top-level **External Tool Citation & Reference Handoff Slots** table, and
  4. Writes the 100% merged, copy-paste-ready article body to both `publish-ready-body.md` and the `## Full Assembled Article Body (Copy-Paste Ready)` section inside `publish-package.md`.
- **External Tool Handoff Draft (非终态直发包)**: `publish-package.md` is an advanced handoff draft for the operator to copy into external citation/reference tool sites — never auto-deploy it to a live CMS.

## Output

Create:
- `publish-package.md`
- `wordpress-preview-check.md`
- `visual-spec.md` final selection (use routes from `/article-visual`; this is now the visual source of truth)
- `visual-render-check.md` when HTML visuals or static fallbacks need verification
- `schema.json`
- `keyword-record.csv`

Use `templates/visual-render-check.md` as the structure for the render-check artifact.

Update `state.json` with:

```json
{
  "currentStage": "article-publish-pack",
  "nextCommand": "/article-next",
  "lockedProfile": true
}
```

## Examples

### Example 1: Packing Deliverables
输入: `/article-publish-pack content-workspace/steel-screen screen-article`
输出: `publish-package.md, schema.json, keyword-record.csv, and assets/ generated.`

## Guardrails

- **Schema Isolation**: The schema JSON-LD must reside exclusively in schema.json; never embed it in the copy body.
- **Keyword Accuracy**: Ensure keyword placements mapped in keyword-record.csv match the actual copy text with 100% precision.

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

Stop after package review. Do not deploy or publish automatically.
