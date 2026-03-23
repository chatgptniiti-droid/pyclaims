# 0.9.0 Preview

This release aligns the public claim creation flow with create_claim().

Planned updates:
- create_claim() is the preferred claim creation method and supports idempotency_key.
- create_claim() supports include_audit_trail and returns RequestMeta.audit_requested.
- Audit metadata extensions beyond `audit_requested` are under review and not confirmed in the current implementation.
- submit_claim() remains as a deprecated compatibility alias.
- retry_on_429 is deprecated and ignored by the current implementation.
