# API Reference

## Clients

- `ClaimClient` — synchronous client
- `AsyncClaimClient` — async client

## Models

- `Claim` — represents a created claim (`id`, `amount_cents`, `currency`, `status`)
- `ClaimStatus` — claim status result (`claim_id`, `status`)
- `UploadReceipt` — document upload result (`document_id`, `status`)
- `RequestMeta` — request-level metadata returned alongside claim operations (`request_id`, `retries`)

## Errors

- `PyClaimsError` — base exception for all pyclaims errors
- `InvalidTransitionError` — raised when an invalid claim state transition is attempted
