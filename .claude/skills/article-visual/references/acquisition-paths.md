# Acquisition Paths

Three paths to acquire visual assets, with a strict fallback chain. Each path has specific tools, constraints, and decision criteria.

## Fallback Chain

```
Priority 1: Search (real product photos, install shots, official diagrams, social media)
  ↓ if not found or needs scene-ization/composition/enhancement
Priority 2: Image-to-image AI generation (real base image + prompt)
  ↓ if needs precise technical data visualization or animated flow
Priority 3: HTML synthesis (HTML+CSS+JS → Playwright screenshot/recording)
  ↓ if none work
Priority 4: Markdown table or prose (no visual)
```

The chain is not always linear. Some visuals should go directly to HTML synthesis (data charts) or AI generation (concept composites). The decision is per-visual, based on what the visual needs to show.

---

## Path 1 — Search (Mandatory Apify-First)

### Entry Rule
Always start external visual asset discovery with **Apify** (`python3 scripts/apify_research.py` or `mcp__apify__*` specialized Actors for Google Images, Alibaba, 1688, YouTube, Pinterest, Instagram), combined with Scrapling stealth, Crawl4AI, Firecrawl, and Playwright real Chrome. If an Actor or route is blocked, repair the Actor/parameters/browser-mode and pivot across keywords, pages, and Actors rather than giving up.

### When to use
- Real product photos (SAJ R6, H2, HS3; 304/316L panels, PVD swatches)
- Forensic workshop & QC proof (caliper measurements, weld heat-affected zones, salt-spray samples, crate packing)
- Real installation shots (wall mount, patio, garage, hotel lobby)
- Official technical diagrams (grid on/off flow, wiring, mounting cross-sections)
- Social media installation documentation (YouTube, TikTok, B站, Xiaohongshu)

### Multi-channel matrix

| Platform | What to find | Volume cap | Notes |
|---|---|---|---|
| Official site (from `project-profile.md` §1 Domain) | Product overview images, spec sheet screenshots, CAD drawings | 10 | Highest trust; check wp-content/uploads/ or asset CDN |
| Alibaba / Made-in-China | B2B product photos with spec labels | 30 | High resolution; check for white-background product shots |
| Amazon | Product photos with lifestyle/install context | 20 | May have user-uploaded installation photos |
| YouTube | Installation videos, wiring tutorials, LCD screen demos | 50 | Extract specific frames, not just thumbnails |
| TikTok | Short installation clips, real-world operation | 50 | Vertical format; may need landscape crop |
| LinkedIn / Facebook | Professional installer posts, project case photos | 28 each | Often has real-world installation context |

### Denoise (Dynamic per `project-profile.md`)

Short brand, material grade, or model strings always carry cross-industry homonym pollution (for example, `304`/`316` matching HTTP status codes or highway numbers, or `SAJ`/`H2` matching unrelated consumer terms).

- **Denoise word bag (inclusion)**: Derive 10–15 domain-specific nouns and technical qualifiers from `project-profile.md` §2 (e.g., for architectural metal fabrication: `stainless steel, 316L, PVD coating, laser cut, partition screen, hairline finish, TIG weld, architectural metalwork`; for solar electronics: `solar, inverter, battery, PV, grid-tied, hybrid, LiFePO4, ESS`).
- **Denoise exclusion (rejection)**: List homonym noise categories discovered during initial Apify probing (e.g., `HTTP 304, route 304, toy, anime, game, pet, chemistry formula`).

Implement denoise via regex keyword filtering in a processing script. Items matching exclusion terms are dropped; items not matching any inclusion term are dropped.

### Video frame extraction

Video sources need specific frame capture, not just thumbnails:

| Title semantic | Recommended capture | What to look for |
|---|---|---|
| "wiring" / "connection" / "installation" | 01:25 (unboxing/bracket), 03:45 (AC wiring area) | Physical wiring, terminal blocks, port layout |
| "without battery" / "no battery" / "grid-tied" | 02:10 (LCD indicators), 04:30 (app monitoring) | LCD screen showing no-battery mode, app status |
| "battery" / "storage" / "ESS" | 00:45 (battery stack), 02:55 (connection sequence) | Battery module stacking, connection blind-plug |
| "hybrid" / "inverter" | 01:00 (product overview), 03:15 (working mode display) | Product exterior, working mode indicators |

Extract 2-3 frames per video at the recommended timestamps. Use ffmpeg or Playwright screenshot at the timestamp.

---

## Path 2 — Image-to-image AI Generation

### When to use
- A real product photo exists but needs to be placed in an installation scene (scene-ize)
- Two real product photos need to be composed into a comparison image (compose)
- A real installation photo is low quality / wrong angle / needs annotation (enhance)

### Hard rule: base image is mandatory

No pure text-to-image generation. Every AI-generated visual must start from a real product/asset photo as its base input. The AI modifies the base — it does not invent the product.

### Three modes

| Mode | Input | Output | Example |
|---|---|---|---|
| **Scene-ize** | Real product photo (white background / official) | Product placed in a realistic installation scene | SAJ H2 white-bg → mounted on garage wall |
| **Compose** | Two or more real product photos | Combined comparison or layered image | R6 photo + H2 photo → side-by-side path comparison |
| **Enhance** | Real photo (low quality / phone shot / wrong angle) | Higher quality, better angle, annotated | Blurry install photo → sharp + labeled callouts |

### Prompt constraints

The prompt is written by the skill (which has full article context), not by the executing AI. It must:
- Reference the real base image explicitly ("using this SAJ H2 product photo as the base...")
- Specify what to change (scene, background, angle, composition)
- Specify what must NOT change (product model, interface count, appearance ratio)
- Forbid fabrication ("do not add interfaces not present in the base, do not change the model name, do not generate spec labels")

### Tools

| Tool | Mode | Notes |
|---|---|---|
| nanobanana (img2img) | Scene-ize, compose, enhance | Preferred if available; check nanobanana-mcp config |
| DALL-E edit | Scene-ize, enhance | Good for scene replacement; less control over composition |
| Midjourney (image prompt) | Scene-ize | Style-heavy; may override technical accuracy |
| Stable Diffusion (img2img) | All modes | Maximum control; requires local setup |

### What AI generation must NOT do
- Invent product interfaces, ports, or connections not in the base photo
- Generate model names, spec labels, or voltage numbers (use HTML synthesis for labeled diagrams)
- Change the product's physical proportions or appearance
- Generate "realistic installation photos" that are actually fabricated scenes with no real product base
- Produce text that could be mistaken for a real spec sheet

---

## Path 3 — HTML Synthesis

### When to use
- Data visualizations (Chart.js line/bar charts, calculators, sliders)
- Technical schematic diagrams (wiring topology, energy flow, system architecture)
- Animated flow diagrams (DC vs AC coupling, energy direction)
- Comparison matrices with precise spec data that must be 100% accurate

### Why not AI generation for these
AI cannot reliably produce:
- Correct circuit topology (it invents connections)
- Accurate spec labels (it garbles small text)
- Precise data values in charts (it approximates)
- Sharp small text at mobile resolution

HTML synthesis guarantees accuracy because the data comes from the evidence pack, rendered through code.

### HTML source storage

Store HTML source in `html-visuals/v-XX.html`. This is the editable source — keep it for future updates.

### Playwright recording (for GIFs)

| Parameter | Value | Rationale |
|---|---|---|
| Capture target | DOM selector (`.max-w-5xl` or outermost card container) | Viewport capture produces black bars and crops content |
| Frame rate | 15fps | Higher causes file bloat; lower causes flicker |
| Duration | 3-4 seconds, looped | Long enough to show the flow; short enough to stay small |
| Animation constraint | Direction arrows only; NO dashed-line flow | Dashed lines flicker at GIF frame rate, causing visual vertigo |

### Static WebP capture (for diagrams with small text)

| Parameter | Value | Rationale |
|---|---|---|
| Capture target | Same DOM selector as GIF | Consistency |
| Format | WebP | Better compression than PNG for the same quality |
| Quality | 90% | Sharp text on mobile without file bloat |
| Target size | <100KB (aim for 30-50KB) | Mobile page load |
| Why static not GIF | Small text (model names, specs) must be razor-sharp on mobile. GIF frame compression blurs small text. |

### Design system for HTML visuals

See `references/design-system.md` for the full design spec. Key points:
- Dark background matching the site
- Warm orange accent for highlights and energy flow
- Monospace font for specs and labels
- Chart.js for interactive data charts
- CSS animation for flow direction (not SVG dashed-line animation)
