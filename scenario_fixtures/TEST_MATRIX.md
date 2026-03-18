# Scenario B test matrix

| Group | What you test | Base files to inspect first |
|---|---|---|
| B1 | Did code changes lead to the correct docs patch? | `pyclaims/client.py`, `pyclaims/models.py`, `docs/api/client.md`, `docs/changelog.md` |
| B2 | Were examples/snippets refreshed correctly? | `docs/getting_started.md`, `docs/examples/upload.md`, `docs/parameter_matrix.md`, `docs/architecture.md` |
| B3 | Did HuTouch find real doc gaps and avoid fake ones? | `docs/api/client.md`, `docs/config.md`, `docs/releases/0_9_0_preview.md`, `enterprise_docs/` |
| B4 | Can HuTouch handle manual prompts end-to-end? | `scenario_fixtures/B4/*/case.md` plus recent changes in package/docs |
