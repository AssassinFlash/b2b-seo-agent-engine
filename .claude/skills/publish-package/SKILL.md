---
name: publish-package
description: "Use when: (1) all QA gates have passed in /article-publish-pack, (2) enriched draft is approved, (3) preparing final publishing assets. Creates the publish-ready package after all 4 QA gates pass. Generates WordPress preview checks, image/media plan, HTML visual checks when present, internal/external links, schema JSON-LD, metadata, and keyword records."
user-invocable: false

---

# Publish Package

## Purpose

Convert an approved, QA-passed article into a complete, high-craft **handoff publishing package** (`publish-package.md` + companion files). Note: `publish-package.md` is an advanced handoff draft that the operator takes to external citation/reference tool sites for final enrichment before CMS publishing — never auto-deploy directly to a live CMS.

## When to Use

- `/article-publish-pack`: all 4 QA gates passed, `enriched-draft.md` approved (enforced at the tool boundary by `scripts/hooks/publish_gate.py` and `scripts/validate_publish.py`)

## Instructions

### Required Outputs

1. **WordPress Preview Check** — verify formatting, headings, tables, images, and open-ended HTML interactive/visual modules render cleanly
2. **SEO Title + Meta Description** — selected from `title-options.md` (100% model-evaluated, no mechanical regex scoring)
3. **Slug** — URL path, primary keyword in slug
4. **Image/Media Plan** — per image or media asset: source file, alt text, placement, caption, forensic source attribution
5. **HTML Visual Plan / Render Check** — when `html-visual-plan.md` exists, verify open-ended component placement, evidence IDs, static fallback, accessibility, and article rhythm
6. **Outbound Internal Links** — exact placement and anchor text per linking plan
7. **Inbound Retro-Link Checklist (《旧文回链清单》)** — generated via `python3 scripts/update_link_graph.py` (`knowledge/site-link-graph.json`), listing which existing articles should link back to this new article to prevent orphan pages
8. **External Links & Citation Handoff Slots (《外部工具站二次加工槽位》)** — verified authoritative external links plus explicit `[TO FILL IN EXTERNAL TOOL]` slots for the operator's external citation tool workflow
9. **Schema JSON-LD (`schema.json`)** — `Article`/`TechArticle` with **Named Technical Author (`author`) and Technical Reviewer (`reviewedBy`)** credentials from `project-profile.md`, `FAQPage`, `HowTo`, and `ImageObject` as applicable (never embedded in body text)
10. **Keyword Record (`keyword-record.csv`)** — primary/secondary/supporting keywords with target vs actual placement
11. **Dynamic Fact Library Sync** — run `python3 scripts/sync_draft_born_claims.py` so verified claims and cases are logged in `knowledge/fact-library.json` with `used_in_articles` and `usage_count` tracking

### Schema & SEOPress Pro Metabox Rule

1. **SEOPress Pro Native Metabox Fields**: When the target host uses SEOPress Pro (such as `archmetal-screens.example.com`), record the exact `_seopress_titles_title` and `_seopress_titles_desc` values in `publish-package.md`. Note that `Seo\SchemaFilters` and SEOPress Pro automatically emit the `Article`, `Organization`, and `BreadcrumbList` JSON-LD in `wp_head`, so never paste a duplicate `Article` `<script type="application/ld+json">` inside the post body!
2. **`schema.json` Isolation**: Keep `schema.json` as a separate machine-facing file (and use its `FAQPage` JSON-LD block only for the post's custom schema field when the host does not auto-generate FAQPage on blog posts).
3. **CSP Same-Origin Media (`img-src 'self' data:`)**: Every `<img>` or Markdown image in the assembled body must use a same-origin uploaded path (`/wp-content/uploads/...`) or inline SVG/`data:` URI — external image hotlinks are blocked by the host CSP.

### Supporting Template

- `templates/publish-package.md`

---

## Examples

### Input (defining meta title):
```
Article: Metal Room Divider Design Guide
Primary keyword: metal room divider (480 vol, KD 3)
```

### Output:
```
Title (55 chars): Metal Room Divider Design Guide — Applications & Custom Specs
Meta (155 chars): Custom stainless steel room divider design guide for architects. 
See hotel, restaurant, and office partition applications with Grade 304/316 
specs, PVD finishes, and tolerances.
Slug: metal-room-divider-design-guide
```

### Input (generating FAQ schema):
```
Article FAQ section has 6 questions about lead times, MOQ, color matching, 
installation, documentation, and project scale.
```

### Output:
```
schema.json contains FAQPage schema with the 6 actual Q&A pairs.
Body text remains unchanged — schema is separate.
Do NOT generate FAQPage schema if the article has no FAQ section.
```

---

## Guardrails

### Anti-Patterns
- Generating schema for content that doesn't exist in the article
- Stuffing keywords into alt text
- Adding FAQ schema when the article has no FAQ section
- Forcing machine-facing content into human-readable body text
- Publishing HTML expression blocks without render/accessibility checks when `html-visual-plan.md` exists

### Prerequisites
All 4 QA gates must PASS before this step. A single BLOCK stops progression.
