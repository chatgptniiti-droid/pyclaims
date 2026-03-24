# pyclaims 0.9.0 — Release Summary

**Branch:** `release/0.9.0`
**Ticket:** [KAN-34](https://rohanp12326.atlassian.net/browse/KAN-34) — TC-B1-P02: Align pyclaims 0.9.0 docs for claim creation migration
**Epic:** [KAN-20](https://rohanp12326.atlassian.net/browse/KAN-20) — pyclaims SDK docs maintenance 0.8.0–0.9.0

---

## What changed

### Public API

| Change | Type | Details |
|---|---|---|
| `create_claim()` | Confirmed preferred path | Use this for all new and migrated integrations. Returns `(Claim, RequestMeta)`. |
| `submit_claim()` | Deprecated | Still works; delegates to `create_claim()`. Remove from integrations — will be removed in a future release. |
| `upload_document(content_type=)` | New parameter | Optional `content_type` added (default `"application/pdf"`) on both sync and async clients. |
| `retry_on_429` | Removed | No longer accepted. Use `max_retries` on the client constructor. |
| `timeout_seconds` | Carried from 0.8.0 | Constructor parameter on both `ClaimClient` and `AsyncClaimClient` (default `30`). |

### Documentation refreshed

| File | What changed |
|---|---|
| `docs/api/client.md` | Full rewrite: corrected constructor signature, return types, deprecation notices, added `AsyncClaimClient` section. |
| `docs/api_reference.md` | Expanded from a bare list to full field-level model documentation. |
| `docs/getting_started.md` | Fixed `create_claim()` return value unpacking; added `content_type` example; added `get_claim_status` example. |
| `docs/async.md` | Fixed `create_claim()` return value unpacking; added `content_type` example. |
| `docs/migration_guide.md` | Added 0.8.0 and 0.9.0 migration sections covering `submit_claim` → `create_claim`, `retry_on_429` removal, and the 0.8.0 return type change. |
| `docs/changelog.md` | Added 0.8.0 and 0.9.0 entries; all changes are now recorded. |
| `docs/releases/0_9_0_preview.md` | Updated from speculative draft language to confirmed release notes. |
| `docs/parameter_matrix.md` | Added `timeout_seconds`, `content_type`, `AsyncClaimClient`, and deprecation note for `submit_claim`. |

---

## Key doc issues resolved

1. **Stale constructor signature** — `docs/api/client.md` was missing `timeout_seconds` (added in 0.8.0).
2. **Wrong return type in examples** — multiple docs showed `claim = client.create_claim(...)` instead of `claim, meta = ...`. Fixed across getting started, async, and API reference.
3. **Absent `AsyncClaimClient` docs** — the async client had no reference entry. Added full section.
4. **Outdated migration guide** — was a placeholder. Now covers both 0.8.0 and 0.9.0 breaking and deprecated changes.
5. **Draft preview** — `0_9_0_preview.md` used speculative language ("may be introduced"). Updated to reflect the confirmed implementation.

---

## Commit context

- **Commit `df06b43`**: `docs: full 0.9.0 documentation pass for KAN-34`
- **Commit `a170f29`**: `docs: align client API docs to 0.9.0 for KAN-34`
- **Rohan Patil** — assignee and author.

---

## Acceptance criteria status (KAN-34)

| Criterion | Status |
|---|---|
| No stale examples promoting old usage as preferred | Done |
| Migration guidance explains what older integrations should change | Done |
| API reference and narrative docs are consistent | Done |
| Changelog reflects the release accurately | Done |
| Release preview file matches actual repo state | Done |
