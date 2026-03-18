# TC-B1-P02

Goal: rename, add param, and deprecate old method.

Logical diff:
- `submit_claim` renamed to `create_claim`
- new parameter `idempotency_key`
- `retry_on_429` deprecated

Docs to inspect:
- `docs/getting_started.md`
- `docs/migration_guide.md`
- `docs/api_reference.md`

Expected HuTouch behavior:
- produce migration notes
- call out deprecations, not only raw signature updates
