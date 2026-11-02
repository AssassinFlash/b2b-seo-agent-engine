# Truth QA

**Stage:** `/article-truth-qa`  
**Mode:** `<strict | light / non-blocking>`  
**Date:** `<YYYY-MM-DD>`  
**Status:** `PASS | PASS with watchlist | BLOCK`  
**Next:** `<next command>`

---

## Scope

State whether this run is strict or light.

- **Strict mode:** claim-by-claim verification, calculation/unit/comparative/safety checks, external verification where needed.
- **Light / non-blocking mode:** relies on upstream `evidence-opinion-pack.md`, checks obvious contradictions / red lines / draft-born watchlist, and does not independently reverify every claim.

## Inputs Checked

- `draft.md`
- `evidence-opinion-pack.md` (and `knowledge/fact-library.json` dynamic claim rotation)
- `project-profile.md` red lines & Named E-E-A-T Author/Reviewer boundaries
- `Draft Control Metadata` Truth QA Watchlist
- `upstream-revision-suggestions.md` if present

> **Post-PASS Action**: Once Truth QA passes, run `python3 scripts/sync_draft_born_claims.py content-workspace/<project-slug> <article-slug>` to sync verified claims and update `used_in_articles` / `usage_count` in `knowledge/fact-library.json`.

---

## Pack-Backed Claim Mapping

| Draft claim family | Evidence source / anchor | Status | Action |
|---|---|---|---|
|  |  | verified / weak / contradiction / watchlist |  |

---

## Draft-Born Claim Watchlist

For performance-first drafts, draft-born hooks and estimates may pass in light mode if plausible and not contradicted. In strict mode, resolve each item by verification, softening, or removal.

| Claim | Treatment | Decision |
|---|---|---|
|  | performance hook / quantified stance / estimate / unsupported factual claim | pass / watchlist / verify / weaken / remove / block |

---

## Red Line Check

- Product specs:
- Certifications:
- Factory claims:
- Customer or case claims:
- Savings or performance claims:
- Market claims:
- Brand stance / tone boundaries:

---

## Calculation / Units / Comparative / Safety Findings

### calculation-audit

| Original value / range | Recalculated value or evidence anchor | Delta | Status |
|---|---|---|---|
|  |  |  | pass / watchlist / block |

### unit-mismatch findings

- 

### comparative-claim re-validation

| Claim | Comparison set | Evidence | Status |
|---|---|---|---|
|  |  |  |  |

### safety-critical-spec checklist

| Claim family | Source count / evidence anchors | Status |
|---|---:|---|
|  |  |  |

### upstream-revision-follow-up

| Suggestion | Status | Action |
|---|---|---|
|  | implemented / rejected / not implemented |  |

---

## Verdict

`PASS | PASS with watchlist | BLOCK`

Explain the decision. In light mode, do not overclaim: state that the run is fast, evidence-pack-based, and non-exhaustive.
