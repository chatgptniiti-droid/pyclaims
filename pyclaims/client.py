from .models import Claim, ClaimStatus, UploadReceipt, RequestMeta


class ClaimClient:
    def __init__(
        self,
        api_key: str,
        region: str = "us",
        max_retries: int = 2,
        sso_provider: str | None = None,
    ):
        self.api_key = api_key
        self.region = region
        self.max_retries = max_retries
        self.sso_provider = sso_provider

    def create_claim(
        self,
        amount_cents: int,
        currency: str = "USD",
        idempotency_key: str | None = None,
    ) -> tuple[Claim, RequestMeta]:
        claim = Claim(
            id="clm_123",
            amount_cents=amount_cents,
            currency=currency,
        )
        meta = RequestMeta(
            request_id="req_123",
            retries=0,
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

    def stream_events(self, claim_id: str):
        """Stream claim lifecycle events for the given claim.

        Intended for long-running claim monitoring workflows.
        Yields status-oriented event objects in order as they arrive.
        """
        yield {"claim_id": claim_id, "event": "submitted"}
        yield {"claim_id": claim_id, "event": "processing"}
        yield {"claim_id": claim_id, "event": "resolved"}


class AsyncClaimClient:
    def __init__(
        self,
        api_key: str,
        region: str = "us",
        max_retries: int = 2,
        sso_provider: str | None = None,
    ):
        self.api_key = api_key
        self.region = region
        self.max_retries = max_retries
        self.sso_provider = sso_provider

    async def create_claim(
        self,
        amount_cents: int,
        currency: str = "USD",
        idempotency_key: str | None = None,
    ) -> tuple[Claim, RequestMeta]:
        claim = Claim(
            id="clm_async_123",
            amount_cents=amount_cents,
            currency=currency,
        )
        meta = RequestMeta(
            request_id="req_async_123",
            retries=0,
        )
        return claim, meta

    async def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_async_123")