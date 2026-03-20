# Getting Started

## Quickstart (sync)

```python
from pyclaims import ClaimClient

client = ClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = client.create_claim(
    amount_cents=2500,
    currency="USD",
    idempotency_key="claim-0001",
    include_audit_trail=True,
)
print(claim.id, claim.status, meta.request_id, meta.audit_requested)
```

## Quickstart (async)

```python
from pyclaims import AsyncClaimClient

client = AsyncClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = await client.create_claim(
    amount_cents=2500,
    currency="USD",
    idempotency_key="claim-async-0001",
    include_audit_trail=True,
)
print(claim.id, claim.status, meta.request_id, meta.audit_requested)
```

`create_claim()` is the preferred path. It returns (Claim, RequestMeta).
`RequestMeta.audit_requested` is True when include_audit_trail is True.
`submit_claim()` is **deprecated** and retained only for compatibility.
`retry_on_429` is deprecated and ignored. See the migration guide for updates.

## Uploading a document

```python
receipt = client.upload_document("sample.pdf")
print(receipt.document_id)
```
