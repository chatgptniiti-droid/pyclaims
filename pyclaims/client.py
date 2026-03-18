"""Main client for the dummy pyclaims SDK.

Example:
    >>> client = ClaimClient(api_key="demo", region="us")
    >>> claim = client.create_claim(amount_cents=1000, currency="USD")
    >>> claim.status
    'submitted'
"""

from typing import Optional
from .models import Claim, ClaimStatus, UploadReceipt

class ClaimClient:
    def __init__(self, api_key: str, region: str = "us", max_retries: int = 2):
        self.api_key = api_key
        self.region = region
        self.max_retries = max_retries

    def create_claim(self, amount_cents: int, currency: str = "USD") -> Claim:
        return Claim(id="clm_123", amount_cents=amount_cents, currency=currency)

    def submit_claim(self, amount_cents: int, currency: str = "USD") -> Claim:
        """Deprecated soon; kept for migration examples in future fixtures."""
        return self.create_claim(amount_cents=amount_cents, currency=currency)

    def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_123")

    def resolve_claim(self, claim_id: str) -> str:
        return "resolved"

    def get_claim_status(self, claim_id: str) -> ClaimStatus:
        return ClaimStatus(claim_id=claim_id, status="submitted")


class AsyncClaimClient:
    def __init__(self, api_key: str, region: str = "us", max_retries: int = 2):
        self.api_key = api_key
        self.region = region
        self.max_retries = max_retries

    async def create_claim(self, amount_cents: int, currency: str = "USD") -> Claim:
        return Claim(id="clm_async_123", amount_cents=amount_cents, currency=currency)

    async def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_async_123")
