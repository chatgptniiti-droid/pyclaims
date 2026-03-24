# Getting Started

## Quickstart

```python
from pyclaims import ClaimClient

client = ClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = client.create_claim(amount_cents=2500, currency="USD")
print(claim.id, claim.status)
print(meta.request_id)
```

`create_claim()` returns a `(Claim, RequestMeta)` tuple. Always unpack both values.

## Uploading a document

```python
receipt = client.upload_document("sample.pdf")
print(receipt.document_id)
```

To specify a MIME type other than the default (`application/pdf`):

```python
receipt = client.upload_document("report.png", content_type="image/png")
```

## Checking claim status

```python
status = client.get_claim_status("clm_123")
print(status.status)
```
