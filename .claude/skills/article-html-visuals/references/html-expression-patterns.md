# HTML Expression Patterns For B2B Articles

This reference expands HTML visuals beyond chart/diagram fallback. Use it when an article moment needs a designed HTML block that helps the reader decide, compare, trust, or act.

## Selection Matrix (Open-Ended Repertoire)

| Reader / Buying Committee Need | Best Pattern | Avoid |
|---|---|---|
| "First 3 seconds on page — am I in the right place?" | **Above-the-Fold 3-Path Self-Router Strip** | Full-screen decorative stock hero image |
| "Let me plug in my own load / size / budget numbers" | **Interactive TCO / Sizing / Payback Calculator** | Wall of prose formulas |
| "Which hardware / material grade fits my site?" | **3-Step Diagnostic Path Quiz** or **Comparison Matrix** | Decorative icon grid |
| "Where is the supplier / installer hiding extra costs?" | **Quote Red-Flag Forensic Annotator** (annotated vendor quote) | Generic warning bullet list |
| "How do I convince my CFO / Procurement / Owner?" | **Internal Champion 30-Second Executive TCO & Risk Ledger** | Expecting the CFO to read 3,000 words |
| "When is your high-spec option overkill for me?" | **Anti-Sell Disqualification Boundary Card** | Pretending one product fits 100% of buyers |
| "What does real factory quality vs. failure look like?" | **Forensic Pass/Fail QC Loupe Comparator** | Glossy 3D render or stock handshake photo |
| "What exact clauses should I send suppliers?" | **Copyable RFQ / Installer Interrogation Script Card** | Generic "Contact us" button alone |
| "What is the direct answer for AI/skimmers?" | **Self-Contained RAG Citation Block** + caveats | Forced bold sentence in every H2 |

## Core & Advanced B2B Patterns (Open-Ended — Invent New Forms When Needed)

### 0A. Above-the-Fold 3-Path Self-Router Strip (Navboost Anti-Pogo)

Place immediately after the opening 120–180 word contrarian answer so the reader locks into their exact scenario within 3 seconds:
- 3 compact horizontal cards (`Path A: Budget / Standard`, `Path B: Future-Ready Hybrid`, `Path C: Full Commercial/Off-Grid`).
- Each card shows: **1-line profile ("If your site has X") → Upfront vs. 5-Year TCO → Jump anchor (`#path-a`)**.

### 0B. Interactive TCO / Sizing / Payback Preset Comparator (CSP Zero-JS Pure CSS)

Use when a B2B buyer is weighing upfront capex against retrofit penalty, energy yield, panel count, or material waste:
- Because host CSP (`script-src 'self'`) blocks inline `<script>` and `oninput="..."`, implement interactive calculators in Mode A using **Pure CSS Radio-State Presets** (`<input type="radio" name="b2b-calc" id="calc-1">` + `:checked ~ .b2b-calc-result-1` for 3–4 realistic project profiles, e.g., *Small 12m² Partition* / *Hotel Lobby 45m²* / *Coastal Exterior 80m²*).
- Outputs pre-computed engineering & TCO breakdowns per selected profile with zero JS execution needed and 100% CSP compliance.

### 0C. Quote Red-Flag Forensic Annotator

A visual mock of a real supplier/installer quotation or spec sheet with numbered forensic callout badges (`[1]`, `[2]`, `[3]`):
- Shows the exact innocent-looking line item (e.g., `"Battery-Ready Solar Package — Inverter Included"` or `"304 Stainless Brushed Screen — Outdoor Grade"`).
- Callout badge reveals the hidden trap (`"Trap: No model suffix specified — standard string inverter locks out DC battery coupling"`) and the exact replacement clause to demand.

### 0D. Internal Champion 30-Second Executive TCO & Risk Ledger (For CFO / Procurement)

Designed specifically for the technical searcher (Engineer / Architect / Installer) to screenshot or forward to their budget approver:
- Structured as a compact 4-row boardroom ledger: **Option | Year-0 Capex | Year-1–5 Failure / Rework Exposure | Warranty / Compliance Risk | CFO Verdict**.
- Includes a 1-sentence **"Forward this to Procurement"** summary note.

### 0E. Anti-Sell Disqualification Boundary Card

Builds immediate engineering credibility by telling the buyer when **NOT** to buy the high-spec option:
- Split into two columns: **✅ When You Need [High-Spec Option]** vs. **🛑 Save Your Budget (Buy [Simpler Option] Instead) When...**
- Every threshold is quantified (distance from coast in km, outage frequency per year, span height in meters).

### 0F. Copyable RFQ / Installer Interrogation Script Card

Placed before the final CTA so the buyer leaves with an actionable procurement weapon:
- Styled as a clean terminal/clipboard block containing 3–5 exact technical verification questions or RFQ contract clauses, plus a **What a trustworthy answer sounds like vs. What an evasive sales answer sounds like** key.

### 0G. Interactive Scenario / Environment Switcher Tabs (CSP-Safe Pure CSS Radio Tabs)

Use when advice changes across 3–4 operating environments or project scales, avoiding repetitive paragraphs:
- **Zero-JS Pure CSS State Machine**: Use hidden `<input type="radio" name="env-tab" id="env-1" checked>` + `<label for="env-1">` pill buttons + `#env-1:checked ~ .b2b-panels .panel-1 { display: grid; }` (never `<script>` or `onclick`, which are blocked by `script-src 'self'`).
- Clicking a tab flips the active panel showing **Recommended Grade | Coating Thickness | Fixing Hardware | Failure Risk if Under-Spec'd**.

### 0H. Bento-Grid Spec & Tolerance Callout Matrix

Use to replace monotonous bullet lists when presenting 4–6 critical engineering parameters:
- 2-column Bento Grid (`grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px`) safe for `68ch` reading columns.
- Each tile features a **large system-monospace metric (`±0.15 mm`, `14 ms`, `>2,000 hrs` using `ui-monospace, SFMono-Regular, Menlo, monospace`)**, a micro-badge (` Shop-Floor Verified `), and a 2-line practical implication.

### 0I. Spec-Sheet Promise vs. Shop-Floor Reality Split Card

Use to create visual tension when debunking industry marketing claims:
- Two contrasting side-by-side cards: **Left (Muted/Dashed Border): "What the Brochure Claims"** vs. **Right (Accent/High-Contrast Border): "What Happens on Site After 18 Months"**.
- Connected by a center delta pill showing the exact hidden cost or tolerance drift.

### 0J. Visual Safe-Zone / Failure-Zone Threshold Gauge Bar

Use when explaining a continuous engineering variable (e.g., span height, voltage window, gauge thickness, wind load):
- A horizontal segmented bar divided into **Green (Safe Operating Zone)**, **Amber (Reinforcement Required)**, and **Red (Structural / Thermal Failure Risk)** with pinned callout markers above and below the bar.

---

## Scoped Inline HTML5 Snippet Contract (防污染宿主环境标准模板)

When producing an inline HTML module (`Mode A`), **never** output `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, or `<script src="https://cdn.tailwindcss.com">`. Every snippet must be 100% scoped inside `.b2b-mod-<id>` so it pastes cleanly into WordPress (`arch-dark-gold` / LiveCanvas / Gutenberg Custom HTML) and external citation tool sites:

```html
<div class="b2b-mod-env-tabs" style="margin:24px 0;padding:20px;border:1px solid var(--journal-line,rgba(255,255,255,0.14));border-radius:12px;background:var(--md-bg-deep,#141414);color:var(--journal-ink,rgba(255,255,255,0.92));font-family:var(--md-font-sans,system-ui,sans-serif);">
  <style>
    .b2b-mod-env-tabs .b2b-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin-top:14px; }
    .b2b-mod-env-tabs .b2b-card { background:var(--md-bg,#1a1a1a); border:1px solid var(--journal-line,rgba(255,255,255,0.14)); border-radius:8px; padding:16px; }
    .b2b-mod-env-tabs .b2b-metric { font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace; font-size:20px; font-weight:700; color:var(--md-gold,#c9a962); margin-top:4px; }
  </style>
  <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--md-gold,#c9a962);font-weight:600;">Shop-Floor Specification Matrix (68ch 2-Col Safe)</div>
  <div class="b2b-grid">
    <div class="b2b-card">
      <div style="font-size:12px;color:rgba(255,255,255,0.78);">Indoor Dry Commercial</div>
      <div class="b2b-metric">304 · 2.0 mm</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.75);margin-top:6px;">Hairline + anti-fingerprint seal; ±0.15 mm laser HAZ tolerance.</div>
    </div>
    <div class="b2b-card" style="border-color:var(--md-gold-dark,#a88a4a);background:var(--journal-wash,rgba(201,169,98,0.12));">
      <div style="font-size:12px;color:var(--md-gold,#c9a962);font-weight:600;">Coastal &lt;15 km / Poolside</div>
      <div class="b2b-metric">316 · 2.5–3.0 mm</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.82);margin-top:6px;">Vacuum PVD ≥0.3 μm required; 304 tea-stains within 14 months.</div>
    </div>
  </div>
</div>
```

> **68ch Column, Contrast & Native `#open-quote` CTA Rules**:
> 1. Never hardcode `repeat(3, ...)` or `repeat(4, ...)` — the `#md-blog-single .reader-body` column is `68ch` (`~620px`), so 2 columns (`minmax(220px, 1fr)`) is the maximum side-by-side density.
> 2. Never put white text on a `--md-gold` (`#c9a962`) fill (2.25:1 contrast failure); always use `color: var(--md-bg-darkest, #0a0a0a)` on gold badges/buttons.
> 3. You can also use the host blog's built-in classes `.linker-article-check`, `.linker-article-comparison`, `.linker-article-topic`, and `.linker-article-next`.
> 4. On `archmetal-screens.example.com`, linking any inline CTA button to `href="#open-quote"` (with `data-quote-source="article-module"`) natively opens the site's footer quote dialog (`partials/md-inquiry-cta.html`) with zero custom JS required; or link directly to `/inquiry/` or `https://wa.me/85264731687`.

Run `python3 scripts/render_html_visual.py html-visuals/<id>.html --validate-snippet` after creating every inline snippet.

### 1. Decision Card

Use for one strong recommendation plus qualifiers.

Structure:
- Claim line.
- "Best when" / "Avoid when" / "Ask supplier for" rows.
- One evidence note.

Good for AIO capture because it gives a direct answer without turning the article into snippet spam.

### 2. Comparison Matrix

Use for 2-5 choices across 3-6 criteria.

Rules:
- Keep criteria concrete: durability, maintenance, lead time, glare, cost pressure.
- Highlight the practical winner only when evidence supports it.
- Do not use more than one comparison matrix per short article unless each compares a different decision.

### 3. Risk Map

Use when the reader needs to avoid hidden mistakes.

Structure:
- Left side: risk or wrong assumption.
- Middle: why it happens.
- Right side: prevention or spec question.

This often beats a photo for B2B procurement articles because it makes expert judgment visible.

### 4. Process Strip

Use for manufacturing, QC, sample approval, or publish workflow sequences.

Rules:
- 3-6 stages.
- Each stage gets one verb-led title.
- Proof gates should cite real evidence or be framed as a recommended process, not a verified claim.

### 5. Spec Card

Use for dense values the reader may need to copy into a brief.

Structure:
- 3-6 specs.
- Each spec has label, value, and "why it matters" note.
- Works well as a static fallback image.

### 6. Annotated Explainer

Use when physical relationships matter: mounting, layers, airflow, panel anatomy, packing stack.

Rules:
- Keep labels close to the object.
- Prefer 4-7 callouts.
- Use arrows or lines only when they clarify the spatial relation.

### 7. AIO Answer Block

Use when the article has a natural AI Overview opportunity.

Structure:
- Direct answer.
- Conditions/caveats.
- Proof or practical next step.

Do not force a fixed count. Capture as many answer moments as the article earns.

### 8. Procurement Checklist

Use near quote/specification sections.

Rules:
- Group by buyer action, not supplier department.
- Each item should be something the reader can actually provide or ask.
- Avoid turning the final CTA into a bloated form.

## Rendering Guidance

- Author responsive embeds for article use first.
- Create fixed-size screenshot fallbacks only when the CMS or distribution channel needs them.
- Prefer `max-width: 760px` to `900px` for body embeds unless the article layout supports wider blocks.
- Keep text sizes explicit and mobile-readable.
- Do not rely on system dark/light mode. Set background and text colors.
- Avoid slide-like page chrome, navigation controls, and deck pagination.

## Fit Review Questions

Before promoting an HTML visual, answer:

1. What does this block help the reader do that prose or a simple table does not?
2. Which exact paragraph does it support?
3. Does it preserve benchmark rhythm?
4. Are all numbers and claims traceable?
5. Can the final channel render it, or do we need a static fallback?
