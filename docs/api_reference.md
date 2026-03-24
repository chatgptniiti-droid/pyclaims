# API Reference

## Clients

### `ClaimClient`

Main synchronous client. See [Client API](api/client.md#claimclient) for full method reference.

### `AsyncClaimClient`

Async counterpart of `ClaimClient`. All methods are coroutines. See [Client API](api/client.md#asyncclaimclient).

---

## Models

### `Claim`

Represents a created claim.

| Field | Type | Default | Description |
|---|---|---|---|
| `id` | `str` | — | Unique claim identifier (e.g. `"clm_123"`). |
| `amount_cents` | `int` | — | Claim amount in smallest currency unit. |
| `currency` | `str` | `"USD"` | ISO 4217 currency code. |
| `status` | `str` | `"submitted"` | Current claim status. |

### `ClaimStatus`

Returned by `get_claim_status()`.

| Field | Type | Description |
|---|---|---|
| `claim_id` | `str` | ID of the claim. |
| `status` | `str` | Current status string. |

### `UploadReceipt`

Returned by `upload_document()`.

| Field | Type | Default | Description |
|---|---|---|---|
| `document_id` | `str` | — | Unique identifier for the uploaded document. |
| `status` | `str` | `"queued"` | Processing status of the upload. |

### `RequestMeta`

Returned alongside `Claim` from `create_claim()`.

| Field | Type | Default | Description |
|---|---|---|---|
| `request_id` | `str` | — | Unique identifier for the API request. |
| `retries` | `int` | `0` | Number of retries performed for the request. |
