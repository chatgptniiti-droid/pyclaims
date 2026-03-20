# Client API

## ClaimClient

### `ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Main synchronous client.

### `create_claim(amount_cents, currency='USD', idempotency_key=None)`

Creates a claim. `idempotency_key` is optional and lets you safely retry the
same logical request without creating a duplicate claim.

Returns a tuple of (Claim, RequestMeta). RequestMeta includes request_id,
retries, and timeout_seconds_used.

### `submit_claim(amount_cents, currency='USD', retry_on_429=True)`

Deprecated compatibility alias for `create_claim()`. `retry_on_429` is
deprecated and ignored by the current implementation.

Returns a tuple of (Claim, RequestMeta).

### `upload_document(path)`

Uploads a document and returns `UploadReceipt`.

### `resolve_claim(claim_id)`

Resolves a claim and returns a string status.

### `get_claim_status(claim_id)`

Returns a `ClaimStatus`.
