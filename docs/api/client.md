# Client API

## ClaimClient

Main synchronous client for the pyclaims SDK.

### `ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` | — | API key for authentication. |
| `region` | `str` | `'us'` | Region to route requests to. |
| `timeout_seconds` | `int` | `30` | Per-request timeout in seconds. |
| `max_retries` | `int` | `2` | Maximum number of automatic retries on transient failures. |

---

### `create_claim(amount_cents, currency='USD') → tuple[Claim, RequestMeta]`

Creates a new claim. This is the preferred public method for claim creation.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `amount_cents` | `int` | — | Claim amount in the smallest currency unit. |
| `currency` | `str` | `'USD'` | ISO 4217 currency code. |

**Returns:** `(Claim, RequestMeta)`

```python
client = ClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = client.create_claim(amount_cents=2500, currency="USD")
print(claim.id, claim.status)
print(meta.request_id)
```

---

### `submit_claim(amount_cents, currency='USD') → tuple[Claim, RequestMeta]`

> **Deprecated.** This is a compatibility alias for `create_claim()`. Update integrations to call `create_claim()` directly.

Delegates to `create_claim()` with no behavioural difference. Will be removed in a future release.

---

### `upload_document(path, content_type='application/pdf') → UploadReceipt`

Uploads a supporting document for a claim.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `path` | `str` | — | Local file path to upload. |
| `content_type` | `str` | `'application/pdf'` | MIME type of the document. |

**Returns:** `UploadReceipt`

```python
receipt = client.upload_document("invoice.pdf")
print(receipt.document_id, receipt.status)
```

---

### `resolve_claim(claim_id) → str`

Marks a claim as resolved.

| Parameter | Type | Description |
|---|---|---|
| `claim_id` | `str` | ID of the claim to resolve. |

**Returns:** Status string (e.g. `"resolved"`).

---

### `get_claim_status(claim_id) → ClaimStatus`

Retrieves the current status of a claim.

| Parameter | Type | Description |
|---|---|---|
| `claim_id` | `str` | ID of the claim to look up. |

**Returns:** `ClaimStatus`

```python
status = client.get_claim_status("clm_123")
print(status.status)
```

---

## AsyncClaimClient

Async counterpart of `ClaimClient`. All methods are coroutines and must be awaited.

### `AsyncClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Same parameters as `ClaimClient`.

---

### `async create_claim(amount_cents, currency='USD') → tuple[Claim, RequestMeta]`

Creates a new claim asynchronously.

```python
client = AsyncClaimClient(api_key="demo", region="us")
claim, meta = await client.create_claim(amount_cents=5000, currency="USD")
print(claim.id)
```

---

### `async upload_document(path, content_type='application/pdf') → UploadReceipt`

Uploads a supporting document asynchronously.

```python
receipt = await client.upload_document("invoice.pdf")
print(receipt.document_id)
```
