# Publish Package

## WordPress QA

- Word count:
- H1/H2/H3 structure:
- Mobile preview:
- Table readability:
- CTA placement:
- Meta Description:
- Preview blockers:

## SEO Metadata

- SEO title:
- Meta Description:
- Slug:
- Primary category:
- Tags:

## Images and Alt

| Placement | Image file | Alt | Caption | Source |
|---|---|---|---|---|

## HTML Visuals

| Visual ID | Placement | Component | HTML source / fallback | Render check | Accessibility |
|---|---|---|---|---|---|

## Internal Links (Outbound: New → Existing)

| Anchor | URL | Placement | Reason |
|---|---|---|---|

## Inbound Retro-Link Checklist (旧文回链清单: Existing → New)

Generated via `python3 scripts/update_link_graph.py` (`knowledge/site-link-graph.json`) so this new article never becomes an orphan page.

| Existing Article / Page | Target Section / Paragraph | Suggested Anchor Text | Target URL (This Article) |
|---|---|---|---|

## External Links & Citation Handoff Slots (外部工具站二次加工槽位)

| Anchor / Claim | URL (or `[TO FILL IN EXTERNAL TOOL]`) | Placement | Rel / target | Reason / Verification Note |
|---|---|---|---|---|

## Schema

- `schema.json`:
- Article Schema:
- FAQPage Schema candidates:
- HowTo Schema candidates:
- ImageObject Schema:
- Schema exclusions and reason:

## Keyword Record

| Field | Value |
|---|---|
| Final title | |
| Outline summary | |
| Primary keyword | |
| Search intent | |
| Monthly search volume | |
| Product internal-link anchor | |
| Product URL | |
| Case internal-link anchor | |
| Case URL | |
| Contact anchor | |
| Contact URL | |

## Publish Checks

- Truth QA status:
- Information Gain QA status:
- Benchmark Drift QA status:
- Reader QA status:
- Internal links verified:
- External links verified:
- WordPress preview checked:
- Keyword record completed:

---

## Full Assembled Article Body (Copy-Paste Ready for External Citation Tool / CMS)

> Generated and verified by `python3 scripts/assemble_publish_draft.py content-workspace/<project-slug> <article-slug>` (also saved standalone at `publish-ready-body.md`). Contains the complete article prose + inlined Scoped HTML5 Snippets + merged FAQ & Resource modules + `{{CITE: ...}}` slots, with `Draft Control Metadata` cleanly stripped.

