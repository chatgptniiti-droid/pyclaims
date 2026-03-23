# Changelog

## 0.9.0
- create_claim() is the preferred claim creation method and supports idempotency_key for retry-safe requests.
- create_claim() includes include_audit_trail and returns RequestMeta.audit_requested.
- Audit metadata extensions beyond `audit_requested` are under review and not confirmed in the current implementation.
- submit_claim() is deprecated and remains only as a compatibility alias.
- retry_on_429 is deprecated and ignored by the current implementation.

## 0.8.0
- ClaimClient now supports timeout_seconds (default: 30).
- create_claim() now returns (Claim, RequestMeta) instead of only Claim.

## 0.7.0
- Initial dummy release.
