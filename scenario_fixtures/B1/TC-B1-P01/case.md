# TC-B1-P01

Goal: simulate a public API change that should update docs and changelog.

Base repo before state:
- `ClaimClient.__init__(api_key, region='us', max_retries=2)`
- `create_claim(amount_cents, currency='USD') -> Claim`

Apply these logical changes:
- add `timeout_seconds` to `ClaimClient.__init__`
- change `create_claim(...)` to return `(Claim, RequestMeta)` or docs-friendly equivalent note
- update README, `docs/api/client.md`, and `docs/changelog.md`

Expected HuTouch behavior:
- identify public API impact
- update constructor and method docs
- refresh quickstart snippet
- add changelog entry
