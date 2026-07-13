import time

start_time = time.monotonic()


def get_uptime_seconds() -> float:
    return time.monotonic() - start_time
