# Parameter Matrix

| Symbol | Parameters / Notes |
|---|---|
| `ClaimClient` | `ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)` |
| `AsyncClaimClient` | `AsyncClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)` |
| `create_claim` | `amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False` (returns `Claim, RequestMeta`) |
| `RequestMeta` | `request_id, retries, timeout_seconds_used, audit_requested` (`audit_requested` mirrors include_audit_trail) |
| `submit_claim` | `amount_cents, currency='USD', retry_on_429=True` (**deprecated**; `retry_on_429` ignored) |
