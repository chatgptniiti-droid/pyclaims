# Getting Started

## Quickstart

```python
from pyclaims import ClaimClient

client = ClaimClient(api_key="demo", region="us")
claim = client.create_claim(amount_cents=2500, currency="USD")
print(claim.id, claim.status)
```

## Uploading a document

```python
receipt = client.upload_document("sample.pdf")
print(receipt.document_id)
```
