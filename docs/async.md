# Async Usage

`AsyncClaimClient` mirrors `ClaimClient` with async/await semantics. All methods are coroutines and must be awaited.

## Creating a claim

```python
from pyclaims import AsyncClaimClient

client = AsyncClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = await client.create_claim(amount_cents=5000, currency="USD")
print(claim.id, claim.status)
print(meta.request_id)
```

`create_claim()` returns a `(Claim, RequestMeta)` tuple — unpack both values.

## Uploading a document

```python
receipt = await client.upload_document("invoice.pdf")
print(receipt.document_id)
```

To specify a content type:

```python
receipt = await client.upload_document("scan.png", content_type="image/png")
```
