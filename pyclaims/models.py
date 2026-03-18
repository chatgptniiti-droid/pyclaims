from dataclasses import dataclass
from typing import Optional

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

@dataclass
class TerminalClaimState:
    claim_id: str
    status: str
    final: bool = True

@dataclass
class AuditEntry:
    at: str
    status: str
    note: Optional[str] = None
