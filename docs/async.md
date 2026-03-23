# Async Usage

```python
from pyclaims import AsyncClaimClient

client = AsyncClaimClient(api_key="demo", region="us")
claim = await client.create_claim(amount_cents=5000, currency="USD")
print(claim.id)
```
