# Visual Design System

The design system ensures visual consistency across all visuals in an article and across all articles in a project. It is sourced from `project-profile.md` §12, not invented per-article.

## Why a design system

Without a shared design system, each article's visuals look different — different colors, fonts, backgrounds, and styles. This breaks brand trust and makes the site look unprofessional. The design system is the single source of truth for visual style.

## Default Design System

These are the defaults. They may be overridden by `project-profile.md` §12. Always check the profile first.

### Colors & Host-Theme CSS Variable Tokens (`#md-blog-single` Native Alignment)

Always prefer **Host-Theme CSS Variables with Dark-Gold Fallbacks** so inline HTML components blend seamlessly into `#md-blog-single` (`archmetal-screens.example.com` WindPress `tokens.css` & `blog.css`) while remaining self-contained in standalone previews:

| Element | CSS Variable Token (with Fallback) | Usage |
|---|---|---|
| Deep Surface | `var(--md-bg-deep, #141414)` | Outer card or recessed backgrounds |
| Panel Surface | `var(--md-bg, #1a1a1a)` | Primary card / module surface |
| Primary Accent (Gold) | `var(--md-gold, #c9a962)` | Highlights, key metrics, primary links on dark surface (7.6:1 contrast) |
| Border / Accent Dark | `var(--md-gold-dark, #a88a4a)` | Left accent borders (`3px solid`), active tab outlines |
| Gold Wash Tint | `var(--journal-wash, rgba(201, 169, 98, 0.12))` | Subtle callout / check-box background wash |
| Subtle Divider Line | `var(--journal-line, rgba(255, 255, 255, 0.14))` | Card borders, table cell borders, section dividers |
| Text Primary | `var(--journal-ink, rgba(255, 255, 255, 0.92))` | Headings, specs, body text on dark |
| Text Secondary | `var(--journal-muted, rgba(255, 255, 255, 0.58))` | Captions, secondary labels (keep readable body text ≥0.75 opacity) |
| Dark Ink on Gold Fill | `var(--md-bg-darkest, #0a0a0a)` | Text inside solid `--md-gold` badges/buttons (never put white text on gold fill!) |
| Success / Pass | `#2dd4bf` (teal) | Recommended engineering path, pass state, compliant tolerance |
| Warning / Disqualified | `#ef4444` (red) | Disqualified or high-risk path, failure mode, spec trap |

### Native `#md-blog-single` Host Classes & `68ch` Measure Rules

When the target site uses the `#md-blog-single` WindPress journal sheet (`max-width: 68ch` middle column flanked by sticky left TOC and right Related rails):
1. **Never exceed 2 columns inside `68ch` (`~620px`)**: Use `grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))` (at most 2 cards per row). Hardcoding 3 or 4 columns (`repeat(3, 1fr)`) crushes cards in the 3-column desktop layout and will be rejected by `assemble_publish_draft.py`.
2. **Reuse native `blog.css` structural classes when appropriate**:
   - `.linker-article-comparison` (`display: grid; gap: 24px`)
   - `.linker-article-topic` (`padding-bottom: 24px; border-bottom: 1px solid var(--journal-line)`)
   - `.linker-article-check` (`margin-top: 32px; padding: 24px; border-left: 3px solid var(--md-gold-dark); background: var(--journal-wash)`)
   - `.linker-article-next` (`font-size: 14px`)
3. **Explicit inner spacing & CommonMark Type-6 zero-blank-line rule**: Because `#md-blog-single :is(h1,h2,h3,p,ul,figure) { margin: 0; }` resets margins, any custom `<div class="b2b-mod-...">` container must explicitly set `margin` or `gap` on its inner flex/grid children. Keep zero blank lines (`\n\n`) inside `<div class="b2b-mod-...">...</div>` so `arch-dark-gold` / `wpautop` never splits the HTML block or injects `<p>` tags.
4. **Sticky Header Anchor Clearance & Lightning CSS `-webkit-` Rule**:
   - Any jump target (`id="..."`) inside an article must carry `scroll-margin-top: calc(var(--md-header-h, 73px) + 24px)` so `#md-blog-single`'s sticky header (`60px` desktop / `73px` mobile) never covers the heading after an anchor click.
   - When writing vendor-prefixed CSS (e.g., `-webkit-backdrop-filter` + `backdrop-filter`), always write the `-webkit-` property **before** the standard property so WindPress / Lightning CSS does not drop the standard rule.

### Typography (CSP `font-src 'self'` Compliant — No External Google Fonts)

| Element | Font | Usage |
|---|---|---|
| Labels and specs | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` | Model names, tolerances, open-area percentages, technical labels |
| Body text in visuals | `var(--md-font-sans, "Inter", system-ui, sans-serif)` | Descriptions, captions (self-hosted on `#md-blog-single`) |
| Headings in visuals | `var(--md-font-display, "Playfair Display", Georgia, serif)` or `var(--md-font-sans)` Bold | Card titles, section labels (self-hosted on `#md-blog-single`) |

### Visual style

| Property | Value |
|---|---|
| Corner radius | `8px` (cards, containers) |
| Border | `1px solid #3d3d5c` (subtle, on dark background) |
| Shadow | `0 0 20px rgba(255, 183, 3, 0.15)` (neon glow on accent elements) |
| Spacing | `20px` padding inside cards; `16px` between elements |
| Icon style | Flat, single-color, matching accent |

### Animation

| Property | Value |
|---|---|
| Direction arrow | Solid line with `stroke-dashoffset` slide animation (not dashed) |
| Pulse | `opacity: 0.6 → 1.0` transition, 2s loop |
| Hover (interactive) | Scale `1.0 → 1.05`, 200ms ease |
| No-go | Dashed-line `stroke-dasharray` animation (flickers at GIF frame rate) |

### Chart.js defaults (Mode B Offline Playwright Canvas Screenshot Only — Never Inline in Article Body)

```javascript
{
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { labels: { color: '#f8f9fa', font: { family: 'ui-monospace, SFMono-Regular, Menlo, monospace' } } }
  },
  scales: {
    x: { ticks: { color: '#adb5bd', font: { family: 'ui-monospace, SFMono-Regular, Menlo, monospace' } }, grid: { color: '#3d3d5c' } },
    y: { ticks: { color: '#adb5bd', font: { family: 'ui-monospace, SFMono-Regular, Menlo, monospace' } }, grid: { color: '#3d3d5c' } }
  }
}
```

## Consistency rules

1. **All visuals in one article must use the same design system.** No mixing dark and light backgrounds.
2. **All articles in one project must use the same design system.** The system is defined once in `project-profile.md` §12 and referenced by every article's visual spec.
3. **If the profile does not define a design system**, use the defaults above and flag in `visual-spec.md` that the profile needs a design system section.
4. **AI-generated visuals must match the design system.** The prompt must specify the background, accent colors, and font style to match HTML-synthesized visuals.
5. **Real photos do not need to match the design system** (they are real-world), but their framing/cropping should be consistent (same aspect ratio, same border treatment if any).
