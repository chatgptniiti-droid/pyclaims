# Client API

## ClaimClient

### `ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Main synchronous client.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` | — | API key for authentication |
| `region` | `str` | `'us'` | Target region |
| `timeout_seconds` | `int` | `30` | Request timeout in seconds |
| `max_retries` | `int` | `2` | Maximum retry attempts |

---

### `create_claim(amount_cents, currency='USD') -> tuple[Claim, RequestMeta]`

Creates a claim. This is the preferred public method for claim creation as of 0.9.0.

Returns a `(Claim, RequestMeta)` tuple. `RequestMeta` carries request-level metadata such as `request_id` and `retries`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `amount_cents` | `int` | — | Claim amount in cents |
| `currency` | `str` | `'USD'` | Currency code |

---

### `submit_claim(amount_cents, currency='USD') -> tuple[Claim, RequestMeta]`

**Deprecated.** Compatibility alias for `create_claim()`. Use `create_claim()` instead.

Will be removed in a future major release.

---

### `upload_document(path, content_type='application/pdf') -> UploadReceipt`

Uploads a document and returns an `UploadReceipt`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `path` | `str` | — | Local file path |
| `content_type` | `str` | `'application/pdf'` | MIME type of the document |

---

### `resolve_claim(claim_id) -> str`

Resolves a claim and returns a string status.

---

### `get_claim_status(claim_id) -> ClaimStatus`

Returns a `ClaimStatus` for the given claim ID.

---

## AsyncClaimClient

Async variant of `ClaimClient`. All methods are coroutines and must be awaited.

### `AsyncClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Same constructor parameters as `ClaimClient`.

---

### `await create_claim(amount_cents, currency='USD') -> tuple[Claim, RequestMeta]`

Async version of `ClaimClient.create_claim()`. Returns `(Claim, RequestMeta)`.

---

### `await upload_document(path, content_type='application/pdf') -> UploadReceipt`

Async version of `ClaimClient.upload_document()`.
