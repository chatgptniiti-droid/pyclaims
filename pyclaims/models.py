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
    """Metadata returned with claim requests.

    `audit_requested` mirrors include_audit_trail. Additional audit metadata fields
    are under review and not confirmed in the current implementation.
    """
    request_id: str
    retries: int = 0
    timeout_seconds_used: Optional[int] = None
    audit_requested: bool = False
    # TODO: Audit metadata extensions (e.g., audit_reference vs audit_context) are under review.



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