# Getting Started

## Quickstart

```python
from pyclaims import ClaimClient

client = ClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = client.create_claim(
    amount_cents=2500,
    currency="USD",
    idempotency_key="claim-0001",
)
print(claim.id, claim.status, meta.request_id)
```

`create_claim()` is the preferred path for new integrations. `submit_claim()` is
deprecated and retained only for compatibility. `retry_on_429` is deprecated and
ignored. See the migration guide for steps to update older integrations.

## Uploading a document

```python
receipt = client.upload_document("sample.pdf")
print(receipt.document_id)
```
