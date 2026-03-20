import warnings

from pyclaims import ClaimClient


def test_create_claim_returns_claim_and_meta():
    client = ClaimClient(api_key="demo")
    claim, meta = client.create_claim(
        amount_cents=100,
        idempotency_key="claim-001",
    )

    assert claim.currency == "USD"
    assert claim.amount_cents == 100
    assert claim.id.startswith("clm_")
    assert meta.request_id.startswith("req_")
    assert meta.timeout_seconds_used == 30


def test_submit_claim_is_deprecated_but_still_works():
    client = ClaimClient(api_key="demo")

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        claim, meta = client.submit_claim(
            amount_cents=200,
            currency="USD",
            retry_on_429=True,
        )

    assert claim.amount_cents == 200
    assert meta.request_id.startswith("req_")
    assert any("deprecated" in str(w.message).lower() for w in caught)