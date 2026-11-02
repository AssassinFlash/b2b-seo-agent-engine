# Visual Spec — `<article-slug>`

**Stage:** `/article-visual`  
**Date:** `<YYYY-MM-DD>`  
**Article:** `<article-slug>`  
**Design system source:** `project-profile.md` §12

---

## Visual Opportunity Audit

| # | Marker | Section | Cognitive job | Original enrich intent correct? | Corrected intent |
|---|---|---|---|---|---|
| v-01 | `<!-- visual: v-01 -->` | H2-XX | `<what the reader needs to see>` | yes/no | `<if no, what it should be>` |
| v-02 | `<!-- visual: v-02 -->` | H2-XX | | | |
| ... | | | | | |

---

## v-01: `<Visual name>`

### Position
- Section: H2-XX
- After paragraph: `<exact sentence the visual follows>`
- Cognitive job: `<what the reader needs to see at this point>`

### Visual content
`<Detailed description — layout, elements, labels, data, flow direction. A paragraph or structured list that a multimodal AI can act on. Not a one-liner.>`

### Format
- Output: `<Scoped Inline HTML5 Snippet (.b2b-mod-*) / Static WebP / Animated GIF / Markdown table / Real photo>`
- Dimensions: `<width x height or "responsive 68ch prose / 74rem breakout">`
- File size target: `<<100KB / <500KB / Zero-JS inline HTML>`
- Path: `visual/<filename>` (or `html-visuals/<id>.html` for Scoped Inline HTML5 Snippets)

### Acquisition strategy

#### Priority 1 — Search (if applicable)
- Keywords: `<specific search terms>`
- Platforms: `<Apify channels>`
- Denoise word bag: `<inclusion terms>`
- Denoise exclusion: `<irrelevant terms>`
- Volume cap: `<per-platform limit>`
- Video frame extraction: `<title semantic → timestamps>`

#### Priority 2 — Image-to-image AI generation (if applicable)
- Base image: `<path/URL to real product photo>`
- Base image source: `<official site / Alibaba / YouTube / local>`
- Generation mode: `<scene-ize / compose / enhance>`
- Prompt: `<generation instruction based on real base>`
- Must preserve: `<product model, interface count, appearance ratio>`
- May change: `<scene, background, angle, lighting, composition>`
- Forbidden: `<inventing interfaces, inventing model names, changing proportions>`
- Tool: `<nanobanana img2img / DALL-E edit / other>`

#### Priority 3 — HTML synthesis (if applicable)
- HTML source: `html-visuals/v-XX.html`
- Data source: `<evidence pack T1.X / draft / calculated>`
- Animation: `<none / direction arrows only / slider interaction>`
- Recording: `<Playwright DOM-selector cropping; 15fps; 3-4s loop>`
- Animation constraint: `<no dashed-line flow; only direction arrows>`

#### Fallback
- `<Markdown table / prose description>`

### Design (Match `project-profile.md` §12 Tokens)
- Background: `<var(--journal-panel, #1a1a1a) for archmetal-screens.example.com / dark #1a1a2e for sunriver / light / transparent>`
- Accent: `<var(--md-gold, #c9a962) for archmetal-screens.example.com / warm orange #ffb703→#fb8500 / brand color>`
- Font: `<var(--font-sans) + var(--font-mono) / ui-monospace, SFMono-Regular, Menlo, monospace>`
- Style: `<Scoped Zero-JS HTML5 dark-gold card / flat technical / realistic forensic photo>`

### Truth-bounded & Forensic Specificity check
- `<Every spec number, model name, tolerance caliper reading, and interface count traces to T1.X / draft / profile. Prefer forensic Pass/Fail QC proof and workshop reality over glossy renders. If not verified, flag for Truth QA.>`

### Status
- [ ] Spec produced
- [ ] Handed to multimodal AI
- [ ] Candidates received
- [ ] Judgment complete (promote/reserve/reject/needs-human)
- [ ] Embedded in enriched-draft.md

---

## v-02: `<Visual name>`

`<repeat the same structure>`

---

## Summary

| # | Format | Acquisition path | Status |
|---|---|---|---|
| v-01 | | | |
| v-02 | | | |
| ... | | | |

---

## Visual Library Updates

New assets generated for this article that should be registered in the project visual library:

| Asset | Type | Source | Tags | Reusable? |
|---|---|---|---|---|
| | | | | |
