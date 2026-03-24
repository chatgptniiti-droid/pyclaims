from dataclasses import dataclass


@dataclass
class Claim:
    id: str
    amount_cents: int
    currency: str = "USD"
    status: str = "submitted"


@dataclass
class ClaimStatus:
    claim_id: str
    status: str


@dataclass
class UploadReceipt:
    document_id: str
    status: str = "queued"


@dataclass
class RequestMeta:
    request_id: str
    retries: int = 0