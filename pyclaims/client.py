"""Main client for the dummy pyclaims SDK.

Example:
    >>> client = ClaimClient(api_key="demo", region="us", timeout_seconds=30)
    >>> claim, meta = client.create_claim(
    ...     amount_cents=1000,
    ...     currency="USD",
    ...     idempotency_key="claim-001",
    ...     include_audit_trail=True,
    ... )
    >>> claim.status
    'submitted'
    >>> meta.request_id.startswith("req_")
    True
    >>> meta.audit_requested
    True
"""

from __future__ import annotations

import warnings

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
        idempotency_key: str | None = None,
        include_audit_trail: bool = False,
    ) -> tuple[Claim, RequestMeta]:
        """Create a claim.

        Args:
            amount_cents: Claim amount in cents.
            currency: ISO currency code. Defaults to USD.
            idempotency_key: Optional unique key used to safely retry the same
                logical request without creating a duplicate claim.
            include_audit_trail: When True, request metadata records that audit
                details were requested for downstream workflows.

        Returns:
            A tuple of (Claim, RequestMeta).
        """
        suffix = (idempotency_key or "123")[-6:]
        claim = Claim(
            id=f"clm_{suffix}",
            amount_cents=amount_cents,
            currency=currency,
        )
        meta = RequestMeta(
            request_id=f"req_{suffix}",
            retries=0,
            timeout_seconds_used=self.timeout_seconds,
            audit_requested=include_audit_trail,
        )
        return claim, meta

    def submit_claim(
        self,
        amount_cents: int,
        currency: str = "USD",
        retry_on_429: bool = True,
    ) -> tuple[Claim, RequestMeta]:
        """Deprecated: use create_claim() instead.

        Args:
            amount_cents: Claim amount in cents.
            currency: ISO currency code. Defaults to USD.
            retry_on_429: Deprecated compatibility flag retained only for older
                integrations. It is ignored by the current implementation.

        Returns:
            A tuple of (Claim, RequestMeta).
        """
        warnings.warn(
            "submit_claim() is deprecated; use create_claim() instead. "
            "retry_on_429 is also deprecated and will be removed in a future release.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.create_claim(
            amount_cents=amount_cents,
            currency=currency,
        )

    def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_123")

    def resolve_claim(self, claim_id: str) -> str:
        return "resolved"

    def get_claim_status(self, claim_id: str) -> ClaimStatus:
        return ClaimStatus(claim_id=claim_id, status="submitted")


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
        idempotency_key: str | None = None,
        include_audit_trail: bool = False,
    ) -> tuple[Claim, RequestMeta]:
        """Create a claim asynchronously.

        Args:
            amount_cents: Claim amount in cents.
            currency: ISO currency code. Defaults to USD.
            idempotency_key: Optional unique key used to safely retry the same
                logical request without creating a duplicate claim.
            include_audit_trail: When True, request metadata records that audit
                details were requested for downstream workflows.

        Returns:
            A tuple of (Claim, RequestMeta).
        """
        suffix = (idempotency_key or "async123")[-6:]
        claim = Claim(
            id=f"clm_async_{suffix}",
            amount_cents=amount_cents,
            currency=currency,
        )
        meta = RequestMeta(
            request_id=f"req_async_{suffix}",
            retries=0,
            timeout_seconds_used=self.timeout_seconds,
            audit_requested=include_audit_trail,
        )
        return claim, meta

    async def upload_document(self, path: str) -> UploadReceipt:
        return UploadReceipt(document_id="doc_async_123")