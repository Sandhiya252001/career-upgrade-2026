def parse_log_line(line: str):
    """
    Expected format:
    2026-05-14 10:20:30 INFO User logged in
    """

    try:
        parts = line.strip().split(" ", 3)

        timestamp = f"{parts[0]} {parts[1]}"
        log_level = parts[2]
        message = parts[3]

        return {
            "timestamp": timestamp,
            "log_level": log_level,
            "message": message
        }

    except Exception:
        return None