---
name: voice-and-humanization
description: "Use when: (1) facts need to become opinions in /article-evidence-opinions, (2) a section needs a voice lens in /article-skeleton, (3) writing or reviewing prose in /article-draft, (4) removing AI-writing patterns before publish, or (5) deciding whether an AIO-ready answer belongs naturally in prose."
user-invocable: false
---

# Voice and Humanization

## Purpose

Prevent B2B content from reading like a supplier catalog or an AI-generated summary. This skill provides one unified policy for:

1. Turning facts into earned judgments.
2. Selecting the right voice lens for each scene.
3. Using bold and AIO-ready answers only where they serve the reader and benchmark rhythm.
4. Removing AI-writing patterns during drafting and QA.

## Argument Contract

This skill is loaded by agents and other skills; it is not invoked directly. Use the Skill tool with name `voice-and-humanization` when an agent or skill frontmatter lists it.

---

## Part 1: Four Thinking Lenses

Select by scene function. If a benchmark anchor article already provides the right voice for a scene, calibrate against the anchor instead of forcing a lens.

| Scene | Lens | Why |
|---|---|---|
| Reader feels confused or overwhelmed | Ann Handley | Story and humanity build trust before complexity |
| Reader is anxious about cost/risk/wrong decision | Josh Braun | Problem recognition creates the bridge to understanding |
| Reader needs specification confidence | Sujan Patel | Data-led argument lets numbers do the persuading |
| Reader carries a misconception | Joe Sugarman | Curiosity and conviction rewire assumptions |

### Lens Calibration Against Benchmark Anchor

When a benchmark article is selected as the draft's primary anchor, the anchor's actual sentence-level execution is the first authority; lenses are optional seasoning. Cross-reference the full benchmark read with lens suggestions and ask: "How would the anchor article's author handle this section?"

---

## Part 2: How Opinions Emerge from Facts

Wrong pattern: fact → "therefore we recommend X" (mechanical, sales-like).
Right pattern: scene → fact → consequence → judgment (natural, expert-like).

### Four Methods

**Method 1 — Conditional Judgment**
Don't say "X is better." Say "If A, choose X. If B, choose Y."

**Method 2 — Trade-off Framing**
Show what the reader gains AND gives up. Real expertise knows what things are NOT good for.

**Method 3 — Counterexample**
Show the wrong choice causing real damage. Let the counterexample make the opinion.

**Method 4 — Field Language**
Sound like someone who has seen projects go wrong. Use specific, physical scenarios.

### Opinion Intensity Scale

| Numeric Intensity | When | Guidance |
|---|---|---|
| 1-3 | Routine context, background | Low-risk explanation; avoid turning every fact into a stance |
| 4-6 | Key judgment, section pivot | Use where the reader needs a decision nudge |
| 7-8 | Stance climax, decision moments | **Normal default for spec-heavy B2B and risk-heavy buyer guides** — sections with quantified judgments, named risks, "the installer / supplier will not flag X" insights, retrofit-trap quantification. Not "sparingly"; the article *should* land here at decision sections so the reader has memorable takeaways. |
| 9-10 | Extreme conviction | Sparingly. Reserve for verified proprietary breakthroughs, named conflicts in source material, or the single sticky thesis the whole article hinges on. Most articles never need 9-10. |

> **Calibration note:** This scale is aligned with Part 3's Numeric Control Vector (Opinion intensity normal range 3-9). Use 7-8 as the **stance climax default for B2B buyer-guide articles**, not as an exception. Reader QA does NOT penalize articles for landing in 7-8 — it penalizes articles that go 9-10 without proprietary proof, or articles that stay below 4 when buyer risk is high.

### Stance vs Hype Boundary

The Opinion Intensity Scale rewards **quantified, named, verifiable stance**. It does NOT reward hype. The two look similar from outside and differ on one test: **a stance survives fact-check; hype does not.**

| ✅ Stance (encouraged at 7-8) | ❌ Hype (rejected at any intensity) |
|---|---|
| "Quietly selling you a $3,000-to-$9,000 future surprise" | "Game-changing solar revolution" |
| "The cheapest inverter on the quote quietly closes the battery door" | "Unleash the ultimate solar power" |
| "The installer who tells you to add a battery later is doing you a favor only if your inverter is battery-ready" | "Skyrocket your energy independence" |
| "What most buyers miss: the inverter decides reversibility, not the battery" | "Revolutionary breakthrough in solar tech" |

**Stance test:** the sentence makes a *falsifiable* claim about a specific buyer, condition, cost, or actor — and the article (or Fact Inventory) can support it. **Hype test:** the sentence makes an *unfalsifiable* claim using a category-level superlative, movement metaphor, or vague intensifier.

Banned hype words are off-limits at **any** intensity (also enforced by `scripts/validate_discovery_profile_workflow.py` BANNED_PHRASES — see Part 4). Quantified stance phrases are **encouraged** especially at intensity 7-8.

When in doubt, ask: **"Could a competitor's sales manager write this verbatim?"** If yes, it is either too generic or hype-adjacent. Rewrite with a named risk, a named number, or a named condition.

### Quality Gates

- Never write "We believe..." / "We recommend..." / "Our opinion is..." → rewrite as conditional judgment.
- Every opinion must pass the competitor test (would a competitor's sales manager say this verbatim?).
- If a fact has no obvious "so what?", ask for more context before processing it into an opinion.

---

## Part 3: Bold and Dynamic AI Overview (AIO) Capture

Bold serves two purposes: help skimming readers find key B2B judgments, and make natural answer moments easier to extract for Google AI Overviews. AIO is a strategic target, but the article must still read like the benchmark anchor, not like a snippet farm.

### Core Principle

Capture as many AIO opportunities as the article naturally supports. Do not use a fixed quota per article or per H2. Do not force every question-like section into the same bold-answer pattern.

### Numeric Control Vector

Before drafting or auditing, choose the article's AIO/bold controls:

| Control | Normal Range | Push Higher When | Push Lower When |
|---|---|---|---|
| AIO capture target | 2-12 extractable moments | article is question-led, comparison-heavy, or targeting AI Overview coverage directly | benchmark is essay-like and narrative flow matters more than snippets |
| Bold judgment target | 2-14 bold judgments | dense decision sections contain multiple extractable rules or warnings | bold starts feeling like formatting for its own sake |
| Opinion intensity | 3-9 / 10 | buyer risk is high or benchmark is strongly opinionated | topic is simple, evidence is thin, or benchmark is restrained |

The selected numbers give direction, not a quota. If the prose starts to look like a snippet farm, reduce AIO/bold targets. If real buyer questions remain unanswered, raise the AIO target.

### What to Bold

**Two bold types, two different goals.** Distinguish them when writing — and when running Reader QA:

- **Full-sentence bold (≥8 words)** — the **AI Citation anchor**. A standalone, falsifiable judgment / decision rule / definition / risk warning that AI Overview, Bing Copilot, or a snippet panel can extract verbatim as the article's takeaway. **Plan at least 1 full-sentence bold per H2** for spec-heavy B2B articles. This is the dominant type for AI-citability.
- **Short bold (< 8 words)** — **navigation only**. Path labels (`**Path A — Grid-tied string inverter**`), rule numbers (`**Rule 1: ...**`), table column emphasis, list-item leads (`**The real version:**`). Helps human skimmers locate structure; does **NOT** count as an AI citation anchor. Useful, but do not inflate bold count by stacking shorts when there is no full-sentence anchor in the section.

Within those two types, bold these:

- Conditional judgments
- Decision rules
- Risk warnings
- Direct answers to question H2s
- Definitions that are the answer to a definition H2

### What NOT to Bold

- Keywords (e.g. ~~**metal room divider**~~)
- Generic marketing (e.g. ~~**high quality**~~)
- Every claim in a section
- A "full-sentence bold" that is actually multiple sentences glued — split it first, then bold the load-bearing one

### Dynamic Capture Rules

- Use bold when the sentence is a real judgment, decision rule, risk warning, or direct answer that a reader would value even if Google never extracted it.

### Part 3.5: Self-Contained RAG Citation Chunks (GEO / Perplexity / SearchGPT / Google AIO 独立语义块工程)

Modern AI answer engines (Google AI Overviews, Perplexity, SearchGPT, Claude Search) retrieve web pages by splitting them into **200–400 token passage chunks** and ranking those chunks via vector + lexical retrieval. If an H2 opening paragraph relies on pronouns (`"It"`, `"This configuration"`, `"They"`) that point back to the H2 heading, the chunk loses its entity context when sliced and fails citation retrieval.

**The 4-Element Self-Contained Chunk Formula (40–60 words at the start of decision-critical Question H2s)**:
1. **Explicit Subject Entity** (name the exact product class, material grade, or architecture — never open with `"It"` or `"Yes, it can"`).
2. **Operating Condition / Boundary** (under what load, climate, code, or budget this applies).
3. **Direct Verdict** (the conclusion-first answer, with the core rule bolded as the full-sentence AI Citation anchor).
4. **Quantified Metric / Consequence** (the concrete dollar, tolerance, efficiency, or failure figure).

| ❌ Dangling-Pronoun Opening (Fails RAG Chunking) | ✅ Self-Contained RAG Citation Chunk (Wins GEO + AIO) |
|---|---|
| *"Yes, you can do this, and for most people it is the smartest move. However, if you pick the wrong one on your quote, it will lock you out later and cost thousands."* (Missing subject entity, missing hardware names, vague cost) | *"A grid-tied solar array can run without a battery using either a standard string inverter or a battery-ready hybrid inverter like the SAJ H2. **Choosing a non-hybrid string inverter saves $800–$1,500 upfront, but adding storage later triggers a $3,500–$7,500 AC-coupled retrofit or full inverter replacement penalty.**"* |

### Part 3.6: Named Engineer Persona & Buying Committee Dual-Register

B2B articles are read by a **Buying Committee**, not a single consumer:
- **Speak to the Technical Specifier (Engineer / Architect / Installer)** with workshop and job-site specificity (named test standards, real failure modes, installation clearances), anchored in the **Named Technical Author / Reviewer persona** from `project-profile.md`.
- **Equip the Specifier to Convince the Approver (Procurement / CFO / Owner)** by translating every technical failure mode into **Total Cost of Ownership (TCO), rework downtime, warranty exposure, or schedule risk** that a financial decision-maker immediately understands.
- Question H2s should have an early, clear answer when the section genuinely targets a real search question. If a benchmark-native opening needs tension before the answer, preserve the rhythm and make the answer extractable at the first natural point.
- Multiple bold answers are allowed when the section genuinely contains multiple extractable decision points. Remove bolding when it starts to look like formatting for its own sake.
- **Do not bold ordinary nouns, product names, or definitions unless they are the answer to a question H2.**
- If a bold sentence is the answer to a definition H2, make it a complete standalone sentence.

### AI Overview (AIO) Answer Quality

For AIO candidate sentences, prefer:

1. **Clear entity and condition**: state what the answer applies to, with the condition that makes it true.
   * *Bad*: *It is widely believed that using 304 stainless steel is the best decision for general partitions.*
   * *Good*: ***Grade 304 stainless steel is the industry standard for interior room dividers because it balances cost with rust resistance in humidity.***
2. **Self-contained context**: the sentence should make sense when extracted, but it can still sound like the benchmark author.
3. **Objective wording when appropriate**: if a sentence is intended as a direct extractable answer, avoid making the answer depend on "we" or "our." Brand experience can appear in the surrounding proof.
   * *Bad*: ***We fabricate custom room dividers in our Foshan workshop with hand-chamfered edges to ensure installer safety.***
   * *Good*: ***Custom room dividers manufactured with hand-chamfered edges eliminate cut hazards for installation crews during onsite assembly.***
4. **Natural length**: concise enough to be extractable, long enough to carry the condition. Do not force a fixed word window if the benchmark rhythm needs a shorter punch or a longer conditional sentence.

### Snippet Quality Test

Read each bold sentence in isolation:
1. Does it make sense without surrounding context? (Must be a complete standalone sentence).
2. Does it answer the H2 (if the H2 is a question)?
3. Does it avoid unnecessary first-person dependency when meant as a direct extractable answer?
4. Is it concise without becoming clipped or robotic?
5. Would a competitor say this? If yes, rewrite.

---

## Part 4: Anti-AI Patterns & Translation Dictionary

During drafting and QA, scan for the patterns in `references/patterns.md`. Use the translation mappings below to swap generic "AI-speak" into expert, scene-driven "B2B field talk".

### AI-Speak to Expert-Speak Translation Mappings

| AI-Speak Pattern | Expert-Speak Translation | Why |
|---|---|---|
| *Furthermore, it is essential to consider [feature]...* | *But here is the catch: if [action goes wrong], [consequence happens].* | Shifts from academic list-making to real-world risk management. |
| *In conclusion, selecting a room divider requires careful planning...* | *The math is simple: saving $50 on a low-nickel panel now means spending $500 next year to replace it.* | Replaces summary wrap-ups with concrete ROI logic. |
| *As a leading provider, we offer high-quality metal dividers...* | *We fabricate custom dividers in our Foshan workshop—our engineers chamfer every laser-cut edge by hand to prevent installer injuries.* | Trades empty corporate self-praise for physical craftsmanship proof. |
| *Moreover, it represents an excellent combination of beauty and durability...* | *If you pick the wrong finish, fingerprints will look like oil smudges under lobby lights within 24 hours.* | Replaces poetic fluff with hands-on architectural frustration. |
| *It is crucial to note that certifications are important...* | *If the supplier cannot show you a third-party ASTM salt spray test, the panel will start pitting in three months.* | Moves from generic advice to strict specification standards. |

### Vocabulary Palette & High-Fidelity Emulation Guidelines

When writing, you are not a generic AI assistant; you are **the author of the primary benchmark article** who is writing a custom guide for our brand.
1. **Emulate the Reasoning Trajectory**: Clone the benchmark's logic progression. If the benchmark writer starts with a story about a failed install, you must start with a story about a failed install (substituting our metal screen facts).
2. **Apply the Alternative Transitions**: Actively draw transitions from the **Vocabulary Palette** (the extracted Linguistic DNA Card).
3. **No Rigid Restraints**: Do not artificially enforce sentence limits or standard deviations. Focus purely on natural phrasing, conversational speed, and precise, unvarnished industry facts.

For the full 24-pattern catalog and rewrite examples, see `references/patterns.md` in this skill directory.

---

## Part 5: Markdown in Prose

Inline formatting is a prose tool, not an SEO checklist. Apply it as the benchmark anchor applies it.

- **Bold `**`**: Judgments worth extracting. Use dynamically; benchmark rhythm and reader value decide density.
- **Italic `*`**: Quotes, asides, the word the reader needs to hear differently.
- **Bold-italic `***`**: The ONE sentence you want a skimming reader to remember. Use once per article.
- **Inline code `` ` ``**: Technical values only — tolerances, certifications, material grades, specs.
- **Strikethrough `~~`**: Common wrong assumptions. Use 1–2 times per article maximum.
- **Horizontal rule `---`**: Visual breathing room between major cognitive shifts, not between every section.
- **Lists and tables**: Use when content demands comparison or sequence.

---

## Guardrails

### Anti-Patterns
- Treating lens suggestions as mandatory orders — lenses are a menu; the benchmark anchor is the default.
- Using all four opinion methods in one paragraph.
- Bolding every claim in a section.
- Treating AIO capture as a quota instead of a dynamic opportunity.
- Writing "we recommend" instead of conditional judgment.
- Every paragraph ending with a summary sentence.
- Leaving AI filler phrases, generic conclusions, or mechanical three-part lists.

### When NOT to Use
- Pure specification data sheets (no opinion needed).
- Legal/compliance content (must be neutral).
- Sections whose only job is listing facts.

## Instructions

Execute the steps described in the canonical sequence.

## Examples

### Example 1: Applying Voice Lens
输入: `/voice-and-humanization content-workspace/steel-screen screen-article`
输出: `Adjusted tone of section H2-02 to use "Engineer Perspective" lens with active, B2B-compliant prose.`
