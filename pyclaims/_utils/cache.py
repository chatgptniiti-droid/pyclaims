def normalize_cache_key(key: str) -> str:
    return key.strip().lower().replace(" ", ":")

def remember_response(internal_response: dict) -> dict:
    # Private helper intentionally undocumented.
    return {"cached": True, "payload": internal_response}
