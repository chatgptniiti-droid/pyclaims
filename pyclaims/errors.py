class PyClaimsError(Exception):
    """Base package error."""

class InvalidTransitionError(PyClaimsError):
    """Raised when a claim is moved into an invalid state."""
