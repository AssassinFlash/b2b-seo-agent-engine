# H2 Heading Strategy

**Article:** `<article-slug>`  
**Project:** `<project-slug>`  
**Stage:** `/article-skeleton`  
**Date:** `<YYYY-MM-DD>`  

---

## Strategy Summary

| Control | Chosen value | Justification |
|---|---|---|
| Target H2 count | `<n>` | `<why>` |
| 7:3 ratio | 70% clean SEO / 30% micro-tension | `<why>` |
| AIO capture target | `<n>` answerable moments | `<why>` |
| Format repetition tolerance | Max `<n>` consecutive similar sections | `<why>` |

**Core principle:** Every H2 is a search-facing question by default. Each H2 must be indexable by Google AIO/PAA (70% standard search entities) and clickable by humans (30% micro-tension hook).

---

## Upstream Research Reference

`/article-skeleton` does **not** perform live extraction. All candidates come from upstream artifacts. For each source, confirm it was read and record the key evidence location.

| Source artifact | What was extracted | Evidence location | Candidate count | Status |
|---|---|---|---|---|
| `intent-research.md` | Consolidated candidate pool + intent mapping | `content-workspace/<project>/articles/<slug>/intent-research.md` |  |  |
| `content-type-library.md` | Library categories + selected exemplar H2 patterns | `content-workspace/<project>/articles/<slug>/content-type-library.md` |  |  |
| `topic-card.md` Outline Sketch | Seed H2s and search intent | `content-workspace/<project>/articles/<slug>/topic-card.md` |  |  |
| `benchmark-candidates.md` | Selected primary exemplars and H2 patterns | `content-workspace/<project>/articles/<slug>/benchmark-candidates.md` |  |  |
| `benchmarks/<source>-raw-observations.md` | Raw structural and heading observations from selected benchmarks | `content-workspace/<project>/articles/<slug>/benchmarks/*-raw-observations.md` |  |  |
| User-provided external H2s | Operator-supplied heading optimizations | operator input |  |  |

### Upstream gap log
If any required upstream artifact is missing or insufficient, record the gap and the workaround here. Do not silently omit.

| Source | Gap / issue | Workaround used |
|---|---|---|
|  |  |  |

---

## Final H2 Table

| # | Final H2 | 70% SEO Base | 30% Hook | Source | Buying Committee Role | Voice Lens | Format | Self-Contained RAG Chunk? | Arc Node |
|---|---|---|---|---|---|---|---|---|---|
| H2-01 | `<final H2 text>` | `<clean SEO question>` | `<trigger word / phrase>` | `<topic-card / benchmark / PAA / Reddit / user-input / synthesized>` | `<Specifier / Procurement / Approver / Champion Ledger>` | `<lens>` | `<prose / table / list / calculator / annotator>` | `<yes (40-60w entity+condition+verdict+metric) / no>` | `<arc node>` |
| H2-02 |  |  |  |  |  |  |  |  |  |
| H2-03 |  |  |  |  |  |  |  |  |  |
| H2-04 |  |  |  |  |  |  |  |  |  |
| H2-05 |  |  |  |  |  |  |  |  |  |
| H2-06 |  |  |  |  |  |  |  |  |  |
| H2-07 |  |  |  |  |  |  |  |  |  |
| H2-08 |  |  |  |  |  |  |  |  |  |

**Micro-tension word bank (use sparingly):** Actually, Really, Mistake, Costly, Trap, Number One, Lock You Out, Sneaky, Hidden, Wrong.

---

## Raw Candidate Inventory

Upstream H2 assets integrated:
- [ ] `intent-research.md` consolidated candidate pool
- [ ] `content-type-library.md` selected exemplar H2 patterns
- [ ] `topic-card.md` Outline Sketch
- [ ] `benchmark-candidates.md` selected primary exemplars
- [ ] `benchmarks/<source>-raw-observations.md` per-benchmark raw observations
- [ ] `benchmark-success-formula.md` Structural Blueprint / Question Ladder
- [ ] User-provided external H2 optimization

| # | Raw candidate | Source | Extraction evidence | Reader question type | Buyer intent | Content angle | Relevance | Final H2 # or discard |
|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |

**Required evidence format for live channels:**
- Google PAA: exact query URL + DOM selector used
- Google Autocomplete: exact API URL used
- Reddit: exact search query + thread URL(s)

---

## External Input Absorption (if applicable)

| External H2 | Source | Reverse-engineered SEO base | Reverse-engineered hook | Conflict with benchmark/profile? | Absorbed as-is / adapted / rejected |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## Rhythm Audit

| Check | Result |
|---|---|
| No two consecutive sections repeat the same format by default habit | ✅ / ❌ |
| Heavy section followed by lighter section | ✅ / ❌ |
| Voice lens varies across neighboring sections | ✅ / ❌ |
| Question ladder traces from arrival to CTA without jumps | ✅ / ❌ |
| Each H2 can be answered in 1–2 sentences for AIO | ✅ / ❌ |
| Intentional repetition is justified by benchmark rhythm | ✅ / ❌ |

---

## Benchmark Alignment Check

| Benchmark pattern | Where it appears in final H2s | Transformed for project role? |
|---|---|---|
| `<pattern>` | `<H2 #>` | ✅ / ❌ |

---

## Phase 1 Completion Checklist

- [ ] `topic-card.md` Outline Sketch read and candidates extracted
- [ ] `benchmark-candidates.md` H2 patterns read and candidates extracted
- [ ] `benchmarks/<source>-extraction.md` actual H2s read and candidates extracted
- [ ] `intent-research.md` read and candidate pool extracted
- [ ] `content-type-library.md` read and exemplar patterns extracted
- [ ] Upstream Research Reference completed
- [ ] Upstream gap log completed (or explicitly empty)
- [ ] All user-provided external H2s reviewed
- [ ] Failure log completed (or explicitly empty)
- [ ] 7:3 rewrite applied to all kept candidates
- [ ] Final H2s approved by operator before skeleton section contracts

---

## Output Handoff

This strategy feeds directly into `skeleton.md` section contracts. Each final H2 must be embedded as the section heading in the corresponding contract.

- [ ] All H2s are questions
- [ ] Each H2 has documented 70% SEO base + 30% hook
- [ ] Each H2 has Buying Committee role + voice lens + format + Self-Contained RAG Chunk status assigned
- [ ] All core product/solution paths from `project-profile.md` confirmed
- [ ] Rhythm audit passed
- [ ] Research Execution Log proves Phase 1 was actually executed
