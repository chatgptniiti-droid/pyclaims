# Parameter Matrix

| Symbol | Example |
|---|---|
| `ClaimClient` | `ClaimClient(api_key="demo", region="us", timeout_seconds=30)` |
| `create_claim` | `client.create_claim(amount_cents=1000, currency="USD", idempotency_key="claim-0001")` |
| `submit_claim` | `client.submit_claim(...)` (deprecated compatibility alias; retry_on_429 ignored) |
