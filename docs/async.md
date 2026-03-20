# Async Usage

```python
from pyclaims import AsyncClaimClient

client = AsyncClaimClient(api_key="demo", region="us")
claim, meta = await client.create_claim(
    amount_cents=5000,
    currency="USD",
    idempotency_key="claim-async-5000",
    include_audit_trail=True,
)
print(claim.id, meta.request_id, meta.audit_requested)
```

`create_claim()` is the preferred async path. It returns (Claim, RequestMeta).
`audit_requested` is True when include_audit_trail is True.
