# Content Workspace

Generated project profiles and article workspaces live here.

Expected shape (v3 skill-only):

```text
content-workspace/
  <project-slug>/
    project-profile.draft.md
    project-profile.research.md
    project-profile.md
    project-profile.json
    state.json
    topic-cluster.md
    source-library/
      README.md
    articles/
      <article-slug>/
        topic-card.md
        benchmark-candidates.md
        benchmark-success-formula.md
        benchmark-asset-ledger.md
        evidence-opinion-pack.md
        skeleton.md
        narrative-arc.md
        draft.md
        truth-qa.md
        information-gain-qa.md
        benchmark-drift-audit.md
        reader-qa.md
        repair-plan.md          (only if a QA gate blocked)
        enriched-draft.md
        image-plan.md
        publish-package.md
        performance-review.md   (30/60/90 days post-publish)
```

Not every file appears at the beginning. `/profile-discover` should only create the draft profile and state file.

See `example-metal-divider/` for a minimal, fully synthetic end-to-end example.
