from pyclaims import ClaimClient

def test_create_claim():
    client = ClaimClient(api_key="demo")
    claim = client.create_claim(amount_cents=100)
    assert claim.currency == "USD"
    assert claim.amount_cents == 100
