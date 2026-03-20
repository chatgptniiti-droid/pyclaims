# API Reference

## ClaimClient

- `create_claim(amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False)` (preferred)
  - Returns a tuple of (Claim, RequestMeta).
  - RequestMeta fields: request_id, retries, timeout_seconds_used, audit_requested.
  - audit_requested is True when include_audit_trail is True.
- `submit_claim(amount_cents, currency='USD', retry_on_429=True)` (**deprecated**; retry_on_429 ignored)
  - Returns a tuple of (Claim, RequestMeta).

## AsyncClaimClient

- `create_claim(amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False)`
  - Returns a tuple of (Claim, RequestMeta).
  - RequestMeta fields: request_id, retries, timeout_seconds_used, audit_requested.
  - audit_requested is True when include_audit_trail is True.

## Models

- Claim
- ClaimStatus
- UploadReceipt
- RequestMeta
