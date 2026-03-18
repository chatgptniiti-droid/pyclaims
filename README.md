# pyclaims — Scenario B dummy project

This dummy Python SDK is designed to test **Scenario B: Auto-Updating Python Library Documentation After Code Changes**.

It includes:

- a small `pyclaims` package
- human docs in Markdown
- generated-doc placeholders under `docs/reference/`
- example docs and quickstarts
- enterprise-only docs boundary
- scenario fixtures that simulate code diffs, missing docs, noise, ambiguity, and repo errors

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pytest
```

## Layout

- `pyclaims/` — SDK package
- `docs/` — user-facing docs
- `docs/reference/` — generated-reference stubs
- `enterprise_docs/` — enterprise-only docs
- `scenario_fixtures/` — one folder per Scenario B test case
- `tools/` — helper scripts for scanning symbols and docs
- `tests/` — sanity tests for the base SDK

## Important

The base repo is the **starting point**. To test a specific UAT case, inspect the corresponding folder in `scenario_fixtures/` and apply the described change mentally, with Git branches, or by copying the sample snippets into the working tree.

See `scenario_fixtures/INDEX.md` for the mapping to:
- B1 = docs update triggered from code change
- B2 = snippet regeneration
- B3 = missing-doc detection
- B4 = manual-trigger end-to-end flow
