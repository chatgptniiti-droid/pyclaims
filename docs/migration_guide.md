# Migration Guide

## 0.9.0

### Move from submit_claim() to create_claim()

`create_claim()` is the preferred path. `submit_claim()` remains as a deprecated
compatibility alias.

**Before**

```python
client.submit_claim(amount_cents=2500, currency="USD")
```

**After**

```python
client.create_claim(amount_cents=2500, currency="USD")
```

### Use idempotency_key for retry-safe creation

`idempotency_key` is optional. Provide a stable value to retry the same logical
request without creating a duplicate claim.

```python
client.create_claim(
    amount_cents=2500,
    currency="USD",
    idempotency_key="claim-0001",
)
```

### retry_on_429 is deprecated and ignored

If you previously passed `retry_on_429`, you can remove it. The parameter is
ignored by the current implementation and will be removed in a future release.
