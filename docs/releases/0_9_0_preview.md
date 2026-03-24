# 0.9.0 Release Notes

## What's New

### `create_claim()` is now the preferred public method

`create_claim()` replaces `submit_claim()` as the canonical entry point for claim creation. Both `ClaimClient` and `AsyncClaimClient` now return a `(Claim, RequestMeta)` tuple instead of a bare `Claim`, giving callers access to request-level metadata (`request_id`, `retries`).

### `timeout_seconds` constructor parameter

`ClaimClient` and `AsyncClaimClient` now accept a `timeout_seconds` parameter (default: `30`) for per-request timeout control.

### `upload_document()` accepts `content_type`

Both clients now accept a `content_type` parameter (default: `'application/pdf'`) on `upload_document()`.

## Deprecations

- **`submit_claim()`** — deprecated compatibility alias for `create_claim()`. Will be removed in a future major release. Migrate callers to `create_claim()`.
- **`retry_on_429`** — removed. Retry behaviour is now controlled solely via `max_retries`.
