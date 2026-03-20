# 0.9.0 Preview

This release aligns the public claim creation flow with create_claim().

Planned updates:
- create_claim() is the preferred claim creation method and now supports idempotency_key.
- submit_claim() remains as a deprecated compatibility alias.
- retry_on_429 is deprecated and ignored by the current implementation.
