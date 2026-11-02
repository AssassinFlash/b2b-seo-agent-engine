---
name: benchmark-led-answerability
description: "Use when: (1) building answerability structures in /article-skeleton, (2) drafting sections that use tables, FAQs, definitions, or direct answers, (3) verifying answerability blocks in Benchmark Drift QA, (4) any time a comparison table, FAQ, or AIO capture point is proposed."
user-invocable: false

---

# Benchmark-Led Answerability

## Purpose

Prevent answerability structures from creating mechanical SEO templates. Tables, FAQs, definitions, and AIO-ready answer sentences must serve the reader AND match the benchmark's natural format. The goal is to capture as many natural answer opportunities as the article supports without turning the article into a machine-answer page.

## When to Use

- `/article-skeleton`: determine which answerability structures are appropriate for each section
- `/article-draft`: execute answerability blocks with benchmark-native formatting
- `/article-benchmark-qa`: verify answerability didn't distort the article's structure
- `/article-publish-pack`: move machine-facing content to schema, not body text

## Instructions

### 1. Supported Structures (use only where benchmark-native)

- **Self-Contained RAG Citation Chunk** (40–60 word opening passage under a Question H2 carrying explicit subject entity + condition + bold verdict + metric, designed so Perplexity / SearchGPT / Google AIO can slice and cite it standalone without dangling pronouns)
- Direct answer sentence or summary
- **Buying Committee TCO / Risk Decision Ledger** (forwardable table/block helping the technical specifier convince the CFO/procurement approver)
- **Anti-Sell Disqualification Box** (honest boundary stating when a simpler/cheaper alternative is better)
- List summary
- Comparison table
- Step-by-step process
- Objection-resolution / FAQ block
- Definition block
- Pros / cons / limitations block

### 2. Source Check Every Block

Before finalizing any answerability block, verify:
- If the block makes a decision-critical claim, is the core data point from Tier 1 (factory, project, team, cert, client)?
- Could Wikipedia or a competitor write this block verbatim? If yes → rewrite or remove.
- Would the answer change if we replaced the brand name? If no → zero information gain.

### 3. Benchmark-Native Only

- No forced FAQ when the benchmark isn't FAQ-like
- No forced per-section takeaway when the benchmark doesn't use that rhythm
- No fixed number of AIO capture points. Use as many as the article naturally earns.
- Move machine-facing content to publish pack, schema, or FAQ candidates — never body text
- No forced table when prose is clearer

### Numeric Answerability Controls

Choose numeric answerability controls before adding tables, FAQs, definitions, or AIO-ready sentences:

| Control | Normal Range | Push Higher When | Push Lower When |
|---|---|---|---|
| Answerable moment target | 2-12 | SERP is question-heavy and the benchmark supports modular answer sections | benchmark is narrative/editorial or search intent is broad |
| Direct-answer ratio | 20-70 / 100 | question-led buyer guide or comparison article | direct answers would flatten tension or sound machine-written |
| Table/FAQ block target | 0-4 | benchmark uses modular comparison or FAQ sections | prose is clearer or body would start reading like a FAQ page |

Lower the numbers if the body starts reading like an FAQ page. Raise them if real buyer questions remain unanswered and can be handled in benchmark-native prose.

---

## Examples

### Input (proposed FAQ):
"Q: What is a metal room divider? A: A decorative screen used to separate spaces."

### Source check: FAIL
Any competitor could write this. Zero Tier 1 information.

### Output (rewritten, Tier 1 anchored):
"Q: What makes a custom metal room divider different from an off-the-shelf screen? 
A: A custom divider is engineered for your specific site conditions — ceiling height, traffic flow, privacy requirements, and installation method. At our 12,000m² facility, we manufacture each panel to ±0.1mm tolerance with 8 QC checkpoints, then photograph every panel before it ships. An off-the-shelf screen forces your space to adapt to the product; a custom divider is built around your space."

### Input (proposed table):
```
| Material | Use Case |
| 304 SS   | Indoor   |
| 316 SS   | Outdoor  |
```

### Output (Tier 1 anchored table + judgment):
```
| Material | Best For | Main Risk | Real Project |
| 304 SS   | Indoor, climate-controlled | Not for coastal/poolside | Singapore restaurant, 45 panels |
| 316 SS   | Outdoor, coastal, humid | Higher material cost | Riyadh hotel lobby, 200+ panels |

For most indoor dividers, 304 is enough. For coastal villas, poolside screens, 
or humid exterior corridors, 316 is the safer baseline — not an upgrade.
```

---

## Guardrails

### Anti-Patterns
- Adding FAQ to an article where the benchmark doesn't use FAQ
- Filling tables with generic data any competitor could replicate
- Using answerability structures as a substitute for genuine expertise
- Placing schema-optimized blocks in body text (schema goes in publish pack)

### Structures NOT Used (with reasons)
- Per-section takeaway box — rarely benchmark-native, feels mechanical
- AI Overview summary box — explicitly forbidden as a body-text module; use natural answer sentences inside prose instead
- "Key Takeaways" at top — not benchmark-native for most article types

### When to Ask
- Unsure if a structure is benchmark-native → re-check the benchmark articles
- A table feels forced but the data is useful → test as prose first; if prose works, skip the table
