def remember_response(api_response: dict) -> dict:
    return {"cached": True, "payload": api_response}
