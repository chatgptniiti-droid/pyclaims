# Changelog

## 0.9.0

- `create_claim()` is now the preferred public path for claim creation.
- `submit_claim()` is deprecated. It remains as a compatibility alias that delegates to `create_claim()` and will be removed in a future release.
- `retry_on_429` parameter removed. Use `max_retries` on the client constructor instead.
- `upload_document()` now accepts an optional `content_type` parameter (default `"application/pdf"`), available on both `ClaimClient` and `AsyncClaimClient`.

## 0.8.0

- `ClaimClient` and `AsyncClaimClient` now accept a `timeout_seconds` constructor parameter (default `30`).
- `create_claim()` return type changed from `Claim` to `tuple[Claim, RequestMeta]`. Update call sites to unpack both values.
- `max_retries` constructor parameter added (default `2`).

## 0.7.0

- Initial release.
