from .models import Claim, ClaimStatus, UploadReceipt, RequestMeta


class ClaimClient:
    def __init__(
        self,
        api_key: str,
        region: str = "us",
        timeout_seconds: int = 30,
        max_retries: int = 2,
    ):
        self.api_key = api_key
        self.region = region
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries

    def create_claim(
        self,
        amount_cents: int,
        currency: str = "USD",
        include_audit_trail: bool = False,
    ) -> tuple[Claim, RequestMeta]:
        claim = Claim(
            id="clm_123",
            amount_cents=amount_cents,
            currency=currency,
        )
        meta = RequestMeta(
            request_id="req_123",
            retries=0,
            audit_requested=include_audit_trail,
        )
        return claim, meta

    def submit_claim(
        self,
        amount_cents: int,
        currency: str = "USD",
    ) -> tuple[Claim, RequestMeta]:
        return self.create_claim(amount_cents=amount_cents, currency=currency)

    def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_123")

    def resolve_claim(self, claim_id: str) -> str:
        return "resolved"

    def get_claim_status(self, claim_id: str) -> ClaimStatus:
        return ClaimStatus(claim_id=claim_id, status="submitted")

    def get_claim_status_history(self, claim_id: str) -> list[ClaimStatus]:
        return [
            ClaimStatus(claim_id=claim_id, status="submitted"),
            ClaimStatus(claim_id=claim_id, status="processing"),
            ClaimStatus(claim_id=claim_id, status="resolved"),
        ]


class AsyncClaimClient:
    def __init__(
        self,
        api_key: str,
        region: str = "us",
        timeout_seconds: int = 30,
        max_retries: int = 2,
    ):
        self.api_key = api_key
        self.region = region
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries

    async def create_claim(
        self,
        amount_cents: int,
        currency: str = "USD",
        include_audit_trail: bool = False,
    ) -> tuple[Claim, RequestMeta]:
        claim = Claim(
            id="clm_async_123",
            amount_cents=amount_cents,
            currency=currency,
        )
        meta = RequestMeta(
            request_id="req_async_123",
            retries=0,
            audit_requested=include_audit_trail,
        )
        return claim, meta

    async def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_async_123")