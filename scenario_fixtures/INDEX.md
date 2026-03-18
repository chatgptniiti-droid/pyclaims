# Scenario fixture index

This folder maps directly to Scenario B in the UAT doc:

- **B1** docs update triggered from code change
- **B2** example/snippet regeneration after API changes
- **B3** missing-doc detection
- **B4** manual-trigger but end-to-end doc maintenance

Each fixture folder contains:
- `case.md` — what changed and what HuTouch should infer
- optional `patch_*` snippets — fake after-state examples
- optional broken/incomplete files to trigger edge or error behavior

## Recommended use

1. Start from the base repo.
2. Pick a case folder.
3. Compare the described "before" state in the base repo with the "after" snippets in that case.
4. Ask HuTouch to identify impacted docs, missing docs, snippets, confidence, and warnings.
