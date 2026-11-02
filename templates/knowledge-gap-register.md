# Knowledge Gap Register — [Article Name]

**Article:** `[article-slug]`  
**Project:** `[project-slug]`  
**Stage:** `/article-evidence-opinions`  
**Created:** [YYYY-MM-DD]  
**Last updated:** [YYYY-MM-DD]

This register is the central validation ledger for the article. Every claim, spec, comparison, or number that enters the draft must pass through this register before `/article-skeleton` begins.

---

## Executive Summary

| Metric | Value |
|---|---|
| Total Knowledge Gap Flags | [N] |
| Priority 1 (decision-critical / safety) | [N] |
| Priority 2 (technical / market) | [N] |
| Priority 3 (background / guidance) | [N] |
| Verified | [N] |
| Incorrect / Corrected | [N] |
| Needs Clarification | [N] |
| Blocked | [N] |
| Coverage | [%] |

---

## Validation Methodology

**Source hierarchy (highest precedence wins):**
1. Official manufacturer datasheets and manuals
2. Official government data and regulatory documents
3. Industry standards (UL, IEC, IEEE, NEC, etc.)
4. Peer-reviewed research and technical reports
5. Verified installer/industry reports
6. Reputable publisher guides

**Cross-reference protocol:**
- **Priority 1**: 2+ independent sources required
- **Priority 2**: 2+ authoritative sources required
- **Priority 3**: 1+ authoritative source required

**Error taxonomy:**
- `VERIFIED` — claim matches source
- `INCORRECT` — claim contradicts source; must be corrected
- `FALSE CLAIM` — claim is factually wrong or misleading
- `FALSE COMPARATIVE CLAIM` — comparison is wrong (e.g., "highest" when it is not)
- `MATH ERROR` — arithmetic is wrong
- `UNITS ERROR` — units are wrong or mismatched
- `NEEDS CLARIFICATION` — partially verified; requires installer/manufacturer confirmation
- `BLOCKED` — cannot be verified; must be removed or weakened

---

## Knowledge Gap Flags

### Priority 1 — Decision-Critical / Safety

| Flag ID | Section / H2 | Original Claim | Validation Status | Actual Data | Sources | Source Count | Confidence | Correction Action | Risk |
|---|---|---|---|---|---|---|---|---|---|
| P1-001 | | | | | | | | | |
| P1-002 | | | | | | | | | |

### Priority 2 — Technical / Market

| Flag ID | Section / H2 | Original Claim | Validation Status | Actual Data | Sources | Source Count | Confidence | Correction Action | Risk |
|---|---|---|---|---|---|---|---|---|---|
| P2-001 | | | | | | | | | |
| P2-002 | | | | | | | | | |

### Priority 3 — Background / Guidance

| Flag ID | Section / H2 | Original Claim | Validation Status | Actual Data | Sources | Source Count | Confidence | Correction Action | Risk |
|---|---|---|---|---|---|---|---|---|---|
| P3-001 | | | | | | | | | |
| P3-002 | | | | | | | | | |

---

## Layman Translation Library

For each technical spec or concept that appears in the article, provide a five-step translation:

### [Concept/Spec Name]

1. **Technical Term:** [exact term]
2. **Layman Definition:** [one-sentence plain English]
3. **Real Impact:** [what it means for the reader's home/project]
4. **Comparison:** [how it compares to alternatives]
5. **Usage Recommendation:** [when to choose / avoid]

---

## Calculation & Units Audit

| Calculation | Original Result | Corrected Result | Error Type | Action |
|---|---|---|---|---|
| | | | | |

---

## User Overrides / Editorial Decisions

| Flag ID | Original Finding | User Decision | Rationale | Owner |
|---|---|---|---|---|
| | | | | |

---

## Blocked Claims

| Flag ID | Claim | Why Blocked | Disposition |
|---|---|---|---|
| | | | |

---

## Quality Assurance Checklist

- [ ] All Priority 1 flags verified with required source count
- [ ] All Priority 2 flags verified with required source count
- [ ] All Priority 3 flags verified with required source count
- [ ] All `INCORRECT` / `FALSE CLAIM` flags have correction actions
- [ ] All `NEEDS CLARIFICATION` flags have an owner
- [ ] All `BLOCKED` claims have disposition
- [ ] All calculations audited for math and units
- [ ] All technical terms have layman translations
- [ ] All user overrides documented
