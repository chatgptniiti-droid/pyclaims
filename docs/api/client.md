# Client API

## ClaimClient

### `ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Main synchronous client.

### `create_claim(amount_cents, currency='USD')`

Creates a claim.

Returns a tuple of (Claim, RequestMeta).
RequestMeta includes request_id and retries.

### `submit_claim(amount_cents, currency='USD')`

Legacy alias for `create_claim`.

### `upload_document(path)`

Uploads a document and returns `UploadReceipt`.

### `resolve_claim(claim_id)`

Resolves a claim and returns a string status.

### `get_claim_status(claim_id)`

Returns a `ClaimStatus`.
