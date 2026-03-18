# Client API

## ClaimClient

### `ClaimClient(api_key, region='us', max_retries=2)`

Main synchronous client.

### `create_claim(amount_cents, currency='USD')`

Creates a claim and returns a `Claim`.

### `submit_claim(amount_cents, currency='USD')`

Legacy alias for `create_claim`.

### `upload_document(path)`

Uploads a document and returns `UploadReceipt`.

### `resolve_claim(claim_id)`

Resolves a claim and returns a string status.

### `get_claim_status(claim_id)`

Returns a `ClaimStatus`.
