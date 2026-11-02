---
name: article-visual-fit
description: "Use when: /article-visual has candidate assets back from search / image-to-image / HTML synthesis and needs a lightweight promote/reserve/reject/needs-human judgment. This skill is a supporting review gate inside the visual pipeline, not a standalone article stage."
user-invocable: false
---

# Article Visual Fit

## Purpose

Review candidate assets for article usefulness after `/article-visual` has already written the spec and the multimodal AI has returned candidates. This skill is **not** a stage in the main article workflow. It is a lightweight decision gate inside the visual pipeline when the answer is not obvious.

It answers one narrow question:

> Does this candidate help this article explain, prove, compare, orient, or pace the reader?

Use it after `visual-material-hunt` (search branch) or after image-to-image / HTML outputs come back, and before `/article-visual` promotes or embeds anything.

## Inputs

- `draft.md` or `enriched-draft.md` for the exact paragraph and reader moment.
- `skeleton.md` for section function and visual opportunity hints.
- `evidence-opinion-pack.md` for project facts and proof points.
- `visual-asset-candidates.md/json` for candidate source URLs, asset URLs, risk flags, and source evidence.
- Existing `image-plan.md`, if the review is a revision pass.

## Output

Write `visual-fit-review.md` in the article workspace when the decision is not obvious. If the candidate set is tiny, a short section inside `image-plan.md` is enough.

Each reviewed candidate must receive one decision:

| Decision | Meaning |
|---|---|
| `promote` | Use in `image-plan.md` because it improves a specific article moment. |
| `reserve` | Keep as backup, but do not make it the recommended option. |
| `reject` | Do not use; it is decorative, misleading, weak, or irrelevant. |
| `needs-human` | Candidate might work, but visual quality/licensing/context needs operator judgment. |

## Review Gates

Apply these gates in order. Stop early when a candidate clearly fails.

1. **Article job**: Name the job: orientation, explanation, comparison, proof, or pacing relief. If there is no job, reject.
2. **Paragraph fit**: Identify the exact paragraph or section moment it supports. If placement is vague, reserve or reject.
3. **Source truth**: The source context must support what the article will imply. Do not turn a supplier listing into a claimed project case.
4. **Reader value**: The reader should understand something faster, trust a claim more, compare options better, or get a useful pause.
5. **Flow safety**: The visual must not interrupt the benchmark rhythm, over-template the article, or force a machine-like layout.
6. **Availability realism**: Direct asset URL, source URL, and risk flags must be honest. If licensing or visual quality is uncertain, mark `needs-human`.

## Article-Specific Bias

- Prefer fewer stronger visuals over many average visuals.
- A table or HTML expression block can beat a real photo when the section is about choosing, comparing, or understanding.
- A generic marketplace photo can support a concept, but it cannot prove the current business did the project.
- A weak real photo is not automatically better than no image.
- Opening visuals are optional. Do not force an image near the start just because one exists.

## Output Format

```markdown
# Visual Fit Review - <article slug>

## Article Need Summary

- Visual moments that actually need support:
  - [section / paragraph]: [visual job]

## Candidate Decisions

| Candidate | Decision | Article job | Best placement | Why | Risk / condition |
|---|---|---|---|---|---|
| proof-a-01 | promote | proof | after QC claim | shows real inspection context | needs source caption |

## Image Plan Handoff

- Promote into image-plan routes:
  - [candidate_id] -> [visual opportunity] -> [primary / backup / reserve route]
- Keep as reserve:
  - [candidate_id] → [reason]
- Reject:
  - [candidate_id] → [reason]
```

## Common Mistakes

- Reviewing image beauty instead of article usefulness.
- Accepting every real image as proof.
- Rejecting all marketplace images even when they only need to illustrate a general concept.
- Creating a fixed image count target.
- Adding visuals because the article feels long, without naming the reader job.
- Treating `needs-human` as a failure. It is the right label when licensing, cropping, or visual quality cannot be verified from text.
