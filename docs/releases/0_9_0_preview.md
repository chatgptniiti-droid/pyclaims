# 0.9.0 Release Notes

## Overview

pyclaims 0.9.0 completes the claim creation API migration started in 0.8.0, formalises the preferred public interface, and removes deprecated parameters.

## Breaking changes

- **`retry_on_429` removed.** Passing this parameter will raise a `TypeError`. Replace with `max_retries` on the client constructor.

## Deprecations

- **`submit_claim()` deprecated.** The method still works and delegates to `create_claim()`, but will be removed in a future release. Migrate call sites to `create_claim()`.

## New and updated behaviour

- `create_claim()` is the confirmed preferred public path for claim creation on both `ClaimClient` and `AsyncClaimClient`.
- `upload_document()` now accepts an optional `content_type` parameter (default `"application/pdf"`) on both sync and async clients.

## Upgrade notes

See the [Migration Guide](../migration_guide.md) for step-by-step instructions on updating from 0.8.x.
