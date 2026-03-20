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
    timeout_seconds_used: Optional[int] = None
    audit_requested: bool = False
<<<<<<< HEAD
    audit_reference: Optional[str] = None
=======
    audit_context: dict[str, str] = field(default_factory=dict)
>>>>>>> feature/add-audit-context


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