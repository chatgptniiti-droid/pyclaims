Client Reference
================

create_claim() is the preferred claim creation API for sync and async usage.
submit_claim() is **deprecated** and kept for compatibility.
retry_on_429 is deprecated and ignored.

ClaimClient
-----------

- ``create_claim(amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False)``
  - Returns a tuple of (Claim, RequestMeta).
  - RequestMeta fields: request_id, retries, timeout_seconds_used, audit_requested.
  - audit_requested is True when include_audit_trail is True.
  - Audit metadata extensions beyond `audit_requested` are under review and not confirmed in the current implementation.
- ``submit_claim(amount_cents, currency='USD', retry_on_429=True)``
  - **Deprecated.** retry_on_429 is ignored.

AsyncClaimClient
----------------

- ``create_claim(amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False)``
  - Returns a tuple of (Claim, RequestMeta).
  - RequestMeta fields: request_id, retries, timeout_seconds_used, audit_requested.
  - audit_requested is True when include_audit_trail is True.
  - Audit metadata extensions beyond `audit_requested` are under review and not confirmed in the current implementation.

.. autoclass:: pyclaims.client.ClaimClient
   :members:

.. autoclass:: pyclaims.client.AsyncClaimClient
   :members:
