# Parameter Matrix

## Constructors

| Symbol | Example |
|---|---|
| `ClaimClient` | `ClaimClient(api_key="demo", region="us", timeout_seconds=30, max_retries=2)` |
| `AsyncClaimClient` | `AsyncClaimClient(api_key="demo", region="us", timeout_seconds=30, max_retries=2)` |

## Methods

| Symbol | Example |
|---|---|
| `create_claim` | `claim, meta = client.create_claim(amount_cents=1000, currency="USD")` |
| `submit_claim` *(deprecated)* | `claim, meta = client.submit_claim(amount_cents=1000)` — use `create_claim()` instead |
| `upload_document` | `receipt = client.upload_document("file.pdf", content_type="application/pdf")` |
| `resolve_claim` | `client.resolve_claim("clm_123")` |
| `get_claim_status` | `status = client.get_claim_status("clm_123")` |
