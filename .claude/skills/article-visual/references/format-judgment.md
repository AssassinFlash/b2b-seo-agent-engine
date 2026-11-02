# Format Judgment

Decision matrix for choosing the output format of each visual. The format determines file size, mobile readability, animation capability, and production method.

## Decision Matrix

| Visual need | Format | Why |
|---|---|---|
| Product overview photo (what does it look like?) | Real photo (WebP/JPEG) | Trust — readers need to see the actual product |
| Installation scene (how does it look mounted?) | Real photo or AI scene-ized | Trust — real install context builds credibility |
| Comparison of 2-3 products side by side | Static WebP (from HTML) or composed photo | Small text (model names) must be sharp on mobile |
| Technical schematic (wiring, topology, energy flow) | Static WebP (from HTML) or Animated GIF | Static if labels are critical; GIF if flow direction is the point |
| Data chart (cost comparison, savings calculator, rate curves) | Interactive HTML or Animated GIF | Interactive if the reader should explore; GIF if the flow is the message |
| Decision flowchart (3 questions → 3 paths) | Static WebP (from HTML) or markdown | Static if the flow is simple; markdown if it is already structured |
| Checklist / red-flag table | Markdown table | No visual needed — structure IS the visual |
| Callout / single question highlight | Markdown blockquote or GitHub-style callout | No visual needed — typography IS the visual |
| Animated energy flow (DC vs AC coupling, current direction) | Animated GIF (from HTML) | Motion is the point; static cannot show direction |
| Interactive calculator / 3-step diagnostic quiz / path router | Interactive HTML (embedded) + Static WebP fallback | Lets specifiers test their own project numbers while preserving a sharp fallback |
| Quote Red-Flag Annotator / Internal Champion CFO Ledger / Pass-Fail QC Loupe | Responsive HTML block or Static WebP (from HTML) | Razor-sharp callout badges and financial/tolerance numbers on mobile |
| Copyable RFQ / Installer Interrogation Script | Embedded HTML card (`user-select: all`, Zero-JS) or styled Markdown block | Gives the buyer an immediate procurement tool they can select and copy-paste into emails |

## Format Constraints

### Static WebP
- **Use when:** The visual contains small text (model names, specs, labels) that must be razor-sharp on mobile
- **File size:** <100KB (aim for 30-50KB)
- **Production:** HTML → Playwright DOM-selector screenshot → WebP export
- **Why not GIF:** GIF frame compression blurs small text at mobile resolution
- **Why not PNG:** WebP has better compression for the same quality

### Animated GIF
- **Use when:** The visual needs to show energy flow, dynamic interaction, or before/after state, AND motion is essential to understanding
- **File size:** <500KB
- **Frame rate:** 15fps
- **Duration:** 3-4 seconds, looped
- **Animation constraint:** Direction arrows only. NO dashed-line flow animations — at 15fps, dashed lines flicker and cause visual vertigo. Use solid arrows with a subtle pulse or slide animation instead.
- **Production:** HTML+CSS animation → Playwright recording (DOM-selector cropping) → GIF export
- **Why not interactive HTML:** WordPress may not support embedded JS; GIF is universally renderable

### Interactive HTML (embedded — Mode A Zero-JS Pure CSS)
- **Use when:** The visual needs user interaction (preset switching, scenario tabs, expandable drawers) inside the article body
- **Constraint:** Strictly Zero-JS (`script-src 'self'` blocks `<script>` and `onclick=`/`oninput=`); max 2 columns inside `68ch`; use Pure CSS State Machines (`<details>` or `<input type="radio"> + :checked`)
- **Production:** Scoped HTML5 + Pure CSS (`.b2b-mod-*`) → embed directly in article (not a file link)
- **Why not GIF:** Interaction is the point — the reader clicks tabs/drawers directly in the browser

### Markdown table
- **Use when:** Data is already structured in rows/columns and needs no visual enhancement
- **Constraint:** Already in the draft body; no additional asset needed
- **Why not WebP:** A table is more accessible, more SEO-friendly, and more editable than an image of a table

### Real photo (WebP/JPEG)
- **Use when:** The visual is an actual product, installation, or documentation photo
- **Constraint:** Must attribute source; alt text must describe what the photo shows for accessibility and AIO
- **Production:** Sourced from search (Path 1) or AI scene-ized (Path 2)

## Common Mistakes

1. **Using GIF when static would work** — if the reader does not need to see motion, static is always better (smaller, sharper, faster)
2. **Using AI generation for technical schematics** — AI invents connections and garbles labels. Use HTML synthesis for anything with precise data.
3. **Using interactive HTML when GIF captures the essence** — if the interaction is "move a slider and see a curve change," a GIF showing that change is more portable and universally renderable
4. **Forgetting mobile** — small text in GIFs is unreadable on phones. If the visual has labels, use static WebP.
5. **Over-animating** — too many animated elements in a single GIF cause visual vertigo. One animation per GIF, max.
