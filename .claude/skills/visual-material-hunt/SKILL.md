---
name: visual-material-hunt
description: "Use when: /article-visual has already defined the visual's exact role, format, and acquisition path, and you need to execute the *search* portion of the plan: multi-channel discovery, noise cleaning, capacity control, video frame extraction, and candidate capture. This skill finds source-backed candidates; /article-visual writes the spec and judges what gets promoted."
user-invocable: false
---

# Visual Material Hunt

## Purpose

Execute the **search** branch of the visual pipeline. `/article-visual` already decided what the visual needs to show, what format it should be, and whether the primary path is search. `visual-material-hunt` carries out that search across multiple channels, cleans the noise, caps the candidate pool, and extracts precise video frame timestamps so the operator or a multimodal AI can work efficiently.

This skill does not decide:
- where the visual belongs in the article,
- whether the format should be a GIF/WebP/HTML diagram,
- whether AI generation or HTML synthesis would be better,
- or which candidate ultimately wins.

Those are `/article-visual`'s decisions. This skill finds candidates, records source evidence, and refuses to pretend a weak or fake source is good enough.

## Inputs

- Visual spec block from `visual-spec.md` (visual id, cognitive job, format, primary path, fallback chain)
- Search brief: concrete keywords, target platforms, denoise word bag, exclusion terms, capacity caps, video title semantics, unacceptable assets
- Existing article/project visual library (to avoid duplicate searching)

## Outputs

Write candidate records into the article workspace:

- `visual-asset-candidates.md` for operator review
- `visual-asset-candidates.json` for structured downstream selection
- `visual-material-library.html` when the candidate pool is large enough that interactive filtering saves time (recommended for >20 candidates)

Do not promote assets, edit the article, or generate visuals here. This skill only finds and records candidates.

Each candidate must include:

| Field | Meaning |
|---|---|
| `candidate_id` | Stable local id, e.g. `proof-a-01` |
| `source_url` | Page, post, listing, article, or video URL |
| `asset_url` | Direct image/video URL when available |
| `platform` | Official site, Alibaba, Made-in-China, Amazon, YouTube, TikTok, LinkedIn, Facebook, etc. |
| `image_type_fit` | Which visual role it can serve |
| `fit_reason` | Why this candidate helps the reader |
| `risk_flags` | Watermark, logo, UI chrome, poor crop, low resolution, irrelevant scene, license uncertainty |
| `recommended_route` | primary search route / backup route / reserve route / reject |
| `source_evidence` | Title, snippet, supplier/post name, or page text proving context |
| `video_timestamps` | For video sources: recommended capture frames (e.g. `01:25`, `03:45`) and why |

## Source Routing

Read `references/source-routing.md` for route-specific tricks. The high-level matrix:

| Channel | Best for | Capacity cap |
|---|---|---|
| Official site / wp-content | Product overviews, official diagrams, spec-sheet screenshots | 10 |
| Alibaba / Made-in-China | High-res product photos, B2B listing images | 30 each |
| Amazon | Product + lifestyle mix | 20 |
| YouTube | Installation videos, LCD demos, wiring walk-throughs | 50 |
| TikTok | Short real-world install clips | 50 |
| LinkedIn / Facebook | Professional installer case photos | 28 each |

### Denoising (Dynamic per `project-profile.md`)

Short brand, grade, or model strings (e.g., `304`, `316L`, `H2`, `R6`) create heavy homonym noise. Build the inclusion and exclusion word bags dynamically from `project-profile.md` §2 (Product Scope) and `visual-spec.md`:
- **Inclusion word bag**: core product nouns, material grades, fabrication processes, and application terms from `project-profile.md` (e.g., for architectural metalwork: `stainless steel, laser cut, PVD, partition, screen, fabrication, weld, caliper`; for solar storage: `solar, inverter, battery, PV, hybrid, LiFePO4, ESS`).
- **Exclusion terms**: consumer toys, unrelated chemistry/gaming homonyms, and off-category consumer goods.

Drop any candidate that does not match at least one inclusion term or that matches an exclusion term.

### Video Frame Extraction

For video sources, record 2-3 recommended capture timestamps based on title semantics:
- `wiring` / `connection` → bracket + terminal block frames
- `without battery` / `no battery` → LCD status + app monitoring frames
- `battery` / `storage` / `ESS` → battery stack and connection sequence frames
- `hybrid` / `inverter` → product overview + working mode frames

## Candidate Selection Rules

- Prefer real product/application scenes for opening, context, and proof visuals when the visual spec says trust-building is the job.
- Prefer real factory, QC, packing, material, or sample photos for Proof and Detail visuals.
- Prefer HTML synthesis for technical diagrams, data charts, and animated flow schematics — if the visual spec's primary path is HTML, stop searching and hand off to `article-html-visuals`.
- Do not count search result pages, category pages, profile pages, or captcha pages as candidates.
- Do not mark a platform unavailable until at least two different routes fail, except when authentication is explicitly missing.
- Use qualitative fit only: `strong`, `usable`, `weak`, `reject`.

## Handoff To /article-visual

When candidates are found, `/article-visual` judges:
- `promote` — embed in the article and register in the visual library
- `reserve` — keep in the library for future use
- `reject` — discard
- `needs-human` — ambiguous, operator review required

If no credible real asset exists, say so directly. Do not force a weak candidate just because the visual spec wanted a real image. The fallback chain may move to image-to-image AI generation (with a real base) or HTML synthesis.