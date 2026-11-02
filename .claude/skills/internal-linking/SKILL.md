---
name: internal-linking
description: "Use when: (1) building the article skeleton to assign link targets per section, (2) writing the draft to place inline links and accordion blocks, (3) creating the publish-pack linking plan. Governs how internal links are selected from sitemap, assigned link roles, placed in article body, and structured into accordion blocks. Internal links answer the reader's \"what should I read next?\" at each cognitive node — not \"what URLs do we have?\""
user-invocable: false

---

# Internal Linking

## Purpose

Internal links are not SEO signals to stuff. They are the reader's next step at each cognitive node. Link badly and you create noise. Link well and you create a natural reading path from awareness → specification → trust → action.

## When to Use

- `/article-skeleton`: map each section's reader question to a link target
- `/article-draft`: place natural inline body links only (`[anchor](URL)`) — no accordion blocks, no resource cards
- `/article-enrich` (post-QA): add accordion blocks, resource cards, and reader-stage routing
- `/article-publish-pack`: create the final linking plan and run `python3 scripts/update_link_graph.py content-workspace/<project-slug> <article-slug>` to update `knowledge/site-link-graph.json` and generate the **Inbound Retro-Link Checklist (《旧文回链清单》)** so older published articles link back to the new article (preventing orphan pages).

---

## Instructions

### Phase 1: Build the Link Inventory from Sitemap

### Step 1: Filter the sitemap

Remove: `/cart`, `/account`, `/login`, `/privacy`, `/terms`, `/search`, `/tag`, `/collections/all`.

Keep: product pages, application pages, material pages, process pages, case study pages, FAQ pages, contact/quote pages, certification/quality pages, about pages.

### Step 2: Classify each URL by Link Role

| Role | Purpose | Example Canonical URLs (Root Paths — Never Legacy `/pages/...`) |
|---|---|---|
| **Concept / Hub Link** | Explain what the system/material is | `/stainless-steel-screens/`, `/patterns/` |
| **Deep-Dive Link** | Expand technical / manufacturing detail | `/manufacturing-process/`, `/laser-cut-panels/`, `/perforated-panels/` |
| **Application / Family Link** | Show specific architectural family | `/outdoor-privacy-landscape-screens/`, `/laser-cut-geometric-metal-screens/`, `/glass-hybrid-screens/`, `/chinese-style-artistic-screens/` |
| **Pattern / Series Link** | Route to specific pattern or series | `/pattern/<slug>/`, `/collections/pattern-geometric/` |
| **Proof Link** | Provide project case evidence | `/project-gallery/` |
| **Trust Link** | Establish company & factory credibility | `/about-us/`, `/faqs/` |
| **Conversion Link** | Drive direct inquiry action | `/inquiry/`, `#open-quote` |

### Step 3: Match links to article sections

Map each article H2 to the reader's current question, then to the link that answers "what should I read next?"

| Section | Reader Question | Link Role | Target |
|---|---|---|---|
| What Is a Custom Metal Room Divider? | How does this relate to SS screens? | Concept | `/stainless-steel-screens/` |
| Hotel Application | Can I see more hotel projects? | Proof | `/project-gallery/` |
| Outdoor / Villa | What about outdoor-rated options? | Application | `/outdoor-privacy-landscape-screens/` |
| Manufacturing Methods | How do you produce these? | Deep-Dive | `/manufacturing-process/` |
| QC & Certifications | How do you control quality? | Trust | `/manufacturing-process/` |
| FAQ | More questions? | Concept | `/faqs/` |
| Ready to Quote | I'm ready to enquire | Conversion | `/inquiry/` |

---

### Phase 2: Write Links in Markdown

### Inline Link (primary — in body text)

Format: `[specific anchor text](url "title attribute")`

```
For outdoor or poolside applications, review our 
[outdoor-rated stainless steel privacy screen patterns](/outdoor-privacy-landscape-screens/ "Outdoor stainless steel privacy screen patterns") 
before choosing 304 or 316 stainless steel.
```

Every inline link MUST include a title attribute: `[anchor](url "title")`. The title provides SEO value and hover context.

Anchor text rules (Cyrus Shepard / Zyppy Internal Linking Laws):
- **Good**: `[outdoor-rated 316 stainless steel privacy screen patterns]` — specific 4–7 word phrase that tells both reader and search engine the exact topic and grade scope of the target page
- **Bad**: `[click here]`, `[learn more]`, `[our products]` — zero semantic value (and `products` violates the `pattern` glossary rule)
- **First-Link Priority Law**: When an article links to the same destination URL more than once (e.g., an inline link in H2-02 and a routing card in H2-07), Google weights the **first anchor text in the DOM** most heavily. Ensure the **first link** to any URL uses a rich, descriptive entity-attribute anchor, never a generic label.
- **Cross-Article Anchor Variation**: Across different articles in the same Hub-and-Spoke cluster, vary the natural phrasing pointing to the same Hub URL (e.g., `/stainless-steel-screens/`) rather than repeating 100% identical exact-match anchor text on every page.

### Resource Block (section exit — bold arrow link + supporting bullets)

Format:
```
**[→ View Anchor Text](url "title")**: One-line description.

*   **Point 1:** Description with detail. **Bold takeaway if applicable.**
*   **Point 2:** Description with detail.
*   **Point 3:** Description with detail. **Bold key number or claim.**
```

Example:
```
**[→ View H2 Product Line](https://sunriver-energy.example.com/hybrid-inverter/ "SAJ H2 Hybrid Inverter series")**: Single-phase (3-6kW) and three-phase (5-30kW) models available.

*   **Future-Proofing:** You can install it with just panels today. When you're ready for batteries in two years, it's plug-and-play.
*   **10ms Switchover:** If the grid fails, the H2 switches to battery power in under 10 milliseconds. **Your Wi-Fi won't even disconnect.**
*   **High-Voltage Efficiency:** Older systems use 48V architecture. The H2 uses 180-600V. Less current means thinner cables, less heat, and **hundreds of extra kWh saved per year.**
```

Place after key sections where the reader has just absorbed evidence and is ready for a deeper dive. One resource block per major section boundary. Max 2-3 per article. The bold arrow link `**[→ ...](url "title")**` is the entry point. The supporting bullets sell the reader on why clicking is worth their time.

### FAQ Accordion Block (natural reading break — Scoped HTML5 `<details>` default)

Format:
```html
<div class="b2b-mod-faq-group" style="margin:24px 0;">
  <div style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--md-gold,#c9a962);margin-bottom:10px;">Quick Answers: [topic]</div>
  <details class="b2b-mod-faq" style="margin:10px 0;padding:14px 18px;border:1px solid var(--journal-line,rgba(255,255,255,0.14));border-radius:8px;background:var(--journal-panel,#1a1a1a);">
    <summary style="cursor:pointer;font-weight:700;color:var(--md-gold,#c9a962);">Q: [real reader question]?</summary>
    <p style="margin:10px 0 0;color:var(--journal-ink,rgba(255,255,255,0.92));"><strong>[Conclusion-first answer with key emphasis.]</strong> [Optional second sentence with a linked resource.]</p>
  </details>
</div>
```

Placement rules:
- Place at natural reading breaks where the reader has absorbed heavy evidence and now has specific follow-up questions
- Ideal placement: after a block of space-type sections, before the decision framework
- Each Q should be something a real reader would ask at that exact point
- Each A should be 2-4 sentences wrapped in `<p>` tags
- Use `<strong>` for key numbers, specs, and takeaways within answers
- Default to Scoped HTML5 `<details class="b2b-mod-faq">` containers (use Shortcodes Ultimate attributes `open="no" style="fancy" icon="plus" anchor="" anchor_in_url="no" class=""` only when `project-profile.md` explicitly requests Shortcodes Ultimate)

---

### Phase 3: Link Placement Map (per article structure)

At article level, the three link types form a natural escalating path:

```
Section body → Inline links (technical terms, evidence anchors)
Section exit  → Resource block (single blockquote, directional arrow, one deep-dive)
Article break → FAQ Accordion (after evidence, before decision — real Q&A with linked answers)
Article end   → Reader-stage routing box (before CTA)
```

**Inline links** go in body text at the moment a technical term or evidence anchor appears. **Resource blocks** go at section boundaries when the reader has absorbed evidence and wants a next step. **FAQ accordions** go at natural reading breaks — after heavy evidence blocks, before the decision framework.

Never place an accordion block immediately after an H2. The reader needs prose to arrive at the question naturally.

---

### Link Density

| Article Length | Inline Links | Resource Blocks | Accordion Blocks |
|---|---|---|---|
| 2,500-3,500 words | 5-8 | 2-3 | 1-2 |

Key links go inline. Supplementary links go in accordion blocks. Never hide critical links inside collapsed content.

---

## Examples

### Input (inline link missing — technical term without link):
```
For outdoor applications, 316 stainless steel with PVD coating is the safer choice.
```

### Output (inline link added):
```
For outdoor applications, [316 stainless steel with PVD coating](/outdoor-privacy-landscape-screens/ "Outdoor stainless steel privacy screens") is the safer choice.
```

### Input (resource block — bare inline text):
```
**Related:** [Custom screens](/custom-metal-divider-screens/) · [Outdoor screens](/outdoor-privacy-landscape-screens/)
```

### Output (resource block — bold arrow + supporting bullets):
```
**[→ View H2 Product Line](/hybrid-inverter/ "SAJ H2 Hybrid Inverter series")**: Single-phase (3-6kW) and three-phase (5-30kW) models available.

*   **Future-Proofing:** You can install it with just panels today. When you're ready for batteries in two years, it's plug-and-play.
*   **10ms Switchover:** If the grid fails, the H2 switches to battery power in under 10 milliseconds. **Your Wi-Fi won't even disconnect.**
*   **High-Voltage Efficiency:** Older systems use 48V architecture. The H2 uses 180-600V. Less current means thinner cables, less heat, and **hundreds of extra kWh saved per year.**
```

### Input (accordion as link dump):
```html
<details><summary>Related links</summary>
- link 1, link 2, link 3, link 4, link 5, link 6, link 7, link 8
</details>
```

### Output (FAQ accordion — Scoped HTML5 `<details>` default):
```html
<div class="b2b-mod-faq-group" style="margin:24px 0;">
  <div style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--md-gold,#c9a962);margin-bottom:10px;">Quick Answers: Material &amp; Installation</div>
  <details class="b2b-mod-faq" style="margin:10px 0;padding:14px 18px;border:1px solid var(--journal-line,rgba(255,255,255,0.14));border-radius:8px;background:var(--journal-panel,#1a1a1a);">
    <summary style="cursor:pointer;font-weight:700;color:var(--md-gold,#c9a962);">Q: Can 304 stainless steel work outdoors?</summary>
    <p style="margin:10px 0 0;color:var(--journal-ink,rgba(255,255,255,0.92));"><strong>304 works only for dry, sheltered interiors — for any exterior, coastal (&lt;5 km), or poolside zone, Grade 316 stainless steel with PVD coating is required.</strong> The 25–35% alloy delta disappears the first time you avoid tea-staining replacement in year two. See <a href="/outdoor-privacy-landscape-screens/">outdoor privacy screen specifications</a>.</p>
  </details>
  <details class="b2b-mod-faq" style="margin:10px 0;padding:14px 18px;border:1px solid var(--journal-line,rgba(255,255,255,0.14));border-radius:8px;background:var(--journal-panel,#1a1a1a);">
    <summary style="cursor:pointer;font-weight:700;color:var(--md-gold,#c9a962);">Q: How long does a custom screen project take from inquiry to delivery?</summary>
    <p style="margin:10px 0 0;color:var(--journal-ink,rgba(255,255,255,0.92));"><strong>Standard fabrication runs 15–25 working days after CAD shop-drawing sign-off; custom multi-panel hospitality runs take 25–35 working days.</strong> Our <a href="/manufacturing-process/">5-gate QC process</a> verifies laser kerf, TIG weld flatness, and PVD color before crating.</p>
  </details>
</div>
```

---

## Guardrails

### Anti-Patterns
- Stuffing every sitemap URL into the article
- Using `click here` or `learn more` as anchor text
- Inline links without title attribute: `[anchor](url)` → use `[anchor](url "title")` (CommonMark space-separated title, never a comma after `url`)
- Placing accordion blocks immediately after H2s — let the reader arrive at the question naturally
- Hiding the contact/quote link inside a collapsed accordion
- Using the same anchor text for every link to the same page
- Resource blocks without the arrow `→` or supporting bullets — bare `**[→ X](url)**` with no bullets is too thin
- Accordion blocks that are just link lists — each Q must have a real answer, not just URLs
- **Host-Adaptive Accordion & Card Containers**: Default to clean Scoped HTML5 `<details class="b2b-mod-faq">` and `.b2b-mod-*` / `.linker-article-check` containers so articles render natively in `#md-blog-single` (`arch-dark-gold` / LiveCanvas) and external citation tools; use `[su_accordion]` / `[su_spoiler]` only when `project-profile.md` explicitly requests Shortcodes Ultimate.

### When NOT to Use Accordion
- When there is only one link (use a resource block instead)
- For the primary CTA (must be visible, not collapsed)
- At the very top of the article (interrupts the reading promise)
- In articles under 1,500 words (feels disproportionate)
