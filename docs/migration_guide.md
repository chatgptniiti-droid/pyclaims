# Migration Guide

## Migrating to 0.9.0

### `submit_claim()` → `create_claim()`

`submit_claim()` is now a deprecated compatibility alias. It delegates to `create_claim()` with no behavioural difference and will be removed in a future release.

Update all call sites:

```python
# Before (deprecated)
claim, meta = client.submit_claim(amount_cents=2500, currency="USD")

# After (preferred)
claim, meta = client.create_claim(amount_cents=2500, currency="USD")
```

The return type is the same: `tuple[Claim, RequestMeta]`.

### `retry_on_429` removed

The `retry_on_429` parameter is no longer accepted. Retry behaviour is now controlled exclusively by the `max_retries` constructor parameter.

```python
# Before
client = ClaimClient(api_key="...", retry_on_429=True)

# After — remove retry_on_429; use max_retries if needed
client = ClaimClient(api_key="...", max_retries=2)
```

### `upload_document()` — `content_type` added

`upload_document()` now accepts an optional `content_type` parameter (default `"application/pdf"`). Existing callers that pass only `path` are unaffected.

---

## Migrating to 0.8.0

### `create_claim()` now returns `(Claim, RequestMeta)`

In 0.8.0 `create_claim()` changed its return type from a plain `Claim` to a `(Claim, RequestMeta)` tuple. Update any call sites that assigned to a single variable:

```python
# Before (0.7.x)
claim = client.create_claim(amount_cents=1000)

# After (0.8.0+)
claim, meta = client.create_claim(amount_cents=1000)
```

### `ClaimClient` — `timeout_seconds` added

`ClaimClient` and `AsyncClaimClient` now accept a `timeout_seconds` parameter (default `30`). No changes required for existing code; the parameter is optional.
