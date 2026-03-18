# TC-B2-P01

Constructor signature changes.

Logical diff:
- `ClaimClient(api_key, region='us')`
- becomes `ClaimClient(api_key, region='us', timeout_seconds=30)`

Targets:
- `README.md`
- `docs/getting_started.md`

Expected HuTouch behavior:
- refresh snippets and import lines where needed
- note default timeout behavior
