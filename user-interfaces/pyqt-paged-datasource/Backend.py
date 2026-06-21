"""
Simulated "backend"
- Could be a database, log file, API, with many of records
"""


class Backend:
    def __init__(self, total_rows):
        self.total_rows = total_rows

    def fetch(self, start, count):
        # Simulate expensive fetch
        return [
            f"Log line {i}: This is a variable-length message with some extra text."
            for i in range(start, min(start + count, self.total_rows))
        ]
