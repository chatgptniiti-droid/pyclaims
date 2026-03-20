# Migration Guide

## 0.9.0

### Move from submit_claim() to create_claim()

`create_claim()` is the preferred path. `submit_claim()` remains as a deprecated
compatibility alias.

**Before (sync)**

```python
client.submit_claim(amount_cents=2500, currency="USD", retry_on_429=True)
```

**After (sync)**

```python
claim, meta = client.create_claim(
    amount_cents=2500,
    currency="USD",
    idempotency_key="claim-0001",
    include_audit_trail=True,
)
print(meta.request_id, meta.audit_requested)
```

**Before (async)**

```python
await client.submit_claim(amount_cents=2500, currency="USD", retry_on_429=True)
```

**After (async)**

```python
claim, meta = await client.create_claim(
    amount_cents=2500,
    currency="USD",
    idempotency_key="claim-async-0001",
    include_audit_trail=True,
)
print(meta.request_id, meta.audit_requested)
```

### Use idempotency_key for retry-safe creation

`idempotency_key` is optional. Provide a stable value to retry the same logical
request without creating a duplicate claim.

### include_audit_trail adds an audit metadata signal

When `include_audit_trail=True`, the returned `RequestMeta.audit_requested`
value is True.

### retry_on_429 is deprecated and ignored

If you previously passed `retry_on_429`, you can remove it. The parameter is
ignored by the current implementation and will be removed in a future release.
