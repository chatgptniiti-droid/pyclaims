# TC-B3-P02

Behavioral change only.

Logical diff:
- `resolve_claim()` returns a terminal state object instead of a plain string
- may raise `InvalidTransitionError`

Expected HuTouch behavior:
- detect doc gap even though method name stays same
