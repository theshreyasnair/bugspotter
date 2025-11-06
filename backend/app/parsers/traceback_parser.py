def parse_traceback(traceback_str: str) -> dict:
    lines = traceback_str.strip().splitlines()

    if not lines:
        return {"Error" : "empty traceback"}
    else:
        last = lines[-1].lstrip(". ").strip()
        if ":" in last:
            error_type, message = last.split(":", 1)
            error_type = error_type.strip()
            message = message.strip()
        else:
            error_type = last.strip()
            message = ""

    return {
        "error_type" : error_type,
        "message" : message
    }