from PyQt6.QtCore import QRunnable


class FetchWorker(QRunnable):
    def __init__(self, backend, start, count, signals):
        super().__init__()

        self.backend = backend
        self.start = start
        self.count = count
        self.signals = signals

    def run(self):
        rows = self.backend.fetch(self.start, self.count)

        self.signals.finished.emit(self.start, rows)
