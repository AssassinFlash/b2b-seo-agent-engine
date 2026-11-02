# HTML Visual Plan - metal-room-divider-design-guide

## Article

- **Article slug**: `metal-room-divider-design-guide`
- **Article title**: Metal Room Divider Design Guide
- **Visual mix control**: real images/media 35%, HTML expression blocks 40%, table/no visual 25%
- **HTML role in this article**: explain material and specification decisions that marketplace photos cannot prove.

## Selected HTML Expression Blocks

| ID | Placement | Reader job | Component family | Evidence source | Output mode | Static fallback | Render check |
|---|---|---|---|---|---|---|---|
| hv-01 | after `Material choice shapes everything` paragraph | compare material choices without slowing the prose | Decision Card / Comparison Matrix | T1-01, T1-03 | responsive embed | `html-visuals/hv-01-material-choice-card.png` | complete |

## Component Briefs

### `hv-01` - Material Choice Decision Card

- **Supported paragraph**: the material section that compares Grade 304 and Grade 316 stainless steel.
- **Reader job**: understand why the article recommends 3.0 mm Grade 304 for dry commercial interiors and Grade 316 for coastal/wet hospitality zones.
- **Component family**: decision card with a compact 2-column comparison matrix.
- **Core content**: "Grade 304 (Dry Interiors) vs Grade 316 (Coastal & Wet Zones)"; rows for exposure boundary, PVD finish durability, and thickness.
- **Evidence IDs**: T1-01, T1-03.
- **Design direction**: clean B2B card, no slide controls, no deck-like chrome, enough whitespace for scanning.
- **Output mode**: responsive article embed, max-width 68ch; source file `html-visuals/hv-01-material-choice-card.html`.
- **Accessibility text**: Decision card comparing Grade 304 and Grade 316 stainless steel for commercial metal room dividers.
- **Fallback path**: `html-visuals/hv-01-material-choice-card.png` if the CMS cannot preserve inline HTML; mobile check screenshot `html-visuals/hv-01-material-choice-card-mobile.png`.

## Rejected HTML Opportunities

| Placement | Why skipped |
|---|---|
| opening paragraph | prose already creates the Austin lobby scene; a forced opening image would slow entry |
| case section | no verified Toronto project image exists; do not create a synthetic proof visual |
| specification checklist | current bullet list is clear; upgrade only if publish context needs a downloadable spec card |
