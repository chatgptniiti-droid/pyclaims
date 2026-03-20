# Client API

## ClaimClient

### `ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Main synchronous client.

### `create_claim(amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False)`

Creates a claim.

- amount_cents: Claim amount in cents.
- currency: ISO currency code. Defaults to "USD".
- idempotency_key: Optional unique key for retry-safe claim creation. Defaults to None.
- include_audit_trail: When True, request metadata records that audit details were requested. Defaults to False.

Returns a tuple of (Claim, RequestMeta).
RequestMeta fields: request_id, retries, timeout_seconds_used, audit_requested.
`audit_requested` is True when include_audit_trail is True.

```python
from pyclaims import ClaimClient

client = ClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = client.create_claim(
    amount_cents=1000,
    currency="USD",
    idempotency_key="claim-001",
    include_audit_trail=True,
)
print(claim.id, meta.request_id, meta.audit_requested)
```

### `submit_claim(amount_cents, currency='USD', retry_on_429=True)`

**Deprecated.** Use `create_claim()`.
`retry_on_429` defaults to True and is ignored by the current implementation.
Returns a tuple of (Claim, RequestMeta).

## AsyncClaimClient

### `AsyncClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)`

Main asynchronous client.

### `create_claim(amount_cents, currency='USD', idempotency_key=None, include_audit_trail=False)`

Creates a claim asynchronously.

- amount_cents: Claim amount in cents.
- currency: ISO currency code. Defaults to "USD".
- idempotency_key: Optional unique key for retry-safe claim creation. Defaults to None.
- include_audit_trail: When True, request metadata records that audit details were requested. Defaults to False.

Returns a tuple of (Claim, RequestMeta).
RequestMeta fields: request_id, retries, timeout_seconds_used, audit_requested.
`audit_requested` is True when include_audit_trail is True.

```python
from pyclaims import AsyncClaimClient

client = AsyncClaimClient(api_key="demo", region="us", timeout_seconds=30)
claim, meta = await client.create_claim(
    amount_cents=1000,
    currency="USD",
    idempotency_key="claim-async-001",
    include_audit_trail=True,
)
print(claim.id, meta.request_id, meta.audit_requested)
```
