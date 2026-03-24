# pyclaims 0.9.0 — Release Summary

**Date:** 2026-03-24
**Branch:** `release/0.9.0`
**Ticket:** KAN-34 (Done) — TC-B1-P02: Align pyclaims 0.9.0 docs for claim creation migration
**Epic:** KAN-20 — pyclaims SDK docs maintenance 0.8.0–0.9.0
**Assignee:** Rohan Patil

---

## What's in this release

### API changes

| Symbol | Change | Action required |
|---|---|---|
| `create_claim()` | Confirmed preferred public path | Use for all new and migrated integrations |
| `submit_claim()` | **Deprecated** — delegates to `create_claim()` | Migrate call sites; will be removed in a future release |
| `upload_document(content_type=)` | New optional parameter (default `"application/pdf"`) | No action needed; existing callers unaffected |
| `retry_on_429` | **Removed** — raises `TypeError` | Replace with `max_retries` on the client constructor |

### Final public API surface

**`ClaimClient` / `AsyncClaimClient` constructor**

```python
ClaimClient(api_key, region='us', timeout_seconds=30, max_retries=2)
```

**Claim creation (preferred)**

```python
claim, meta = client.create_claim(amount_cents=2500, currency="USD")
```

**Document upload**

```python
receipt = client.upload_document("invoice.pdf", content_type="application/pdf")
```

**Async usage**

```python
claim, meta = await client.create_claim(amount_cents=2500, currency="USD")
receipt = await client.upload_document("invoice.pdf")
```

### Models (final)

| Model | Fields |
|---|---|
| `Claim` | `id`, `amount_cents`, `currency`, `status` |
| `ClaimStatus` | `claim_id`, `status` |
| `UploadReceipt` | `document_id`, `status` |
| `RequestMeta` | `request_id`, `retries` |

---

## Documentation updated

| File | Summary |
|---|---|
| `docs/api/client.md` | Full constructor and method reference for both sync and async clients |
| `docs/api_reference.md` | Complete model field documentation |
| `docs/getting_started.md` | Corrected `create_claim()` return unpacking; added `content_type` and status examples |
| `docs/async.md` | Corrected `create_claim()` return unpacking; added `content_type` example |
| `docs/migration_guide.md` | Step-by-step migration for 0.8.0 and 0.9.0 changes |
| `docs/changelog.md` | 0.8.0 and 0.9.0 entries added |
| `docs/releases/0_9_0_preview.md` | Updated from draft to confirmed release notes |
| `docs/parameter_matrix.md` | Updated with `timeout_seconds`, `content_type`, `AsyncClaimClient`, deprecation note |

---

## Acceptance criteria (KAN-34)

| Criterion | Status |
|---|---|
| No stale examples promoting deprecated usage as the preferred path | Done |
| Migration guidance explains what older integrations must change | Done |
| API reference and narrative docs are consistent | Done |
| Changelog reflects the release accurately | Done |
| Release preview matches actual repo state | Done |
