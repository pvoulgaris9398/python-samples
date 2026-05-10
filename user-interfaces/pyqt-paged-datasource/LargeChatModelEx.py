from FetchSignals import FetchSignals
from FetchWorker import FetchWorker
from LayoutSignals import LayoutSignals
from LayoutWorker import LayoutWorker
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt, QThreadPool


class LargeChatModelEx(QAbstractListModel):
    BATCH_SIZE = 500  # how many rows to fetch at once

    def __init__(self, backend, font, parent=None):
        super().__init__(parent)

        self.backend = backend
        self.font = font

        self.threadpool = QThreadPool.globalInstance()

        self.messages = {}
        self.layout_cache = {}

        self.loaded_rows = 0
        self.total_rows = backend.total_rows

        self.fetching = False

        self.prefix_heights = []

        self.default_height = 20

        self.width = 400

    # ---- Basic model ----
    def rowCount(self, parent=QModelIndex()):
        return self.loaded_rows

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return self.messages[index.row()]

        return None

    # ---- Lazy loading ----
    def canFetchMore(self, parent):
        return self.loaded_rows < self.total_rows

    def fetchMore(self, parent):
        if self.fetching:
            return

        self.fetching = True

        start = self.loaded_rows
        count = min(self.BATCH_SIZE, self.total_rows - self.loaded_rows)

        signals = FetchSignals()
        signals.finished.connect(self.on_fetch_finished)

        worker = FetchWorker(self.backend, start, count, signals)

        self.threadpool.start(worker)

    def setWidth(self, width):
        if self.width != width:
            self.width = width
            self.layout_cache.clear()

    def on_fetch_finished(self, start, rows):
        count = len(rows)

        self.beginInsertRows(QModelIndex(), start, start + count - 1)

        for i, text in enumerate(rows):
            self.messages[start + i] = text

        self.loaded_rows += count

        self.endInsertRows()

        self.fetching = False

        self.precompute_layout(start, rows)

    def precompute_layout(self, start, rows):
        indexed = {start + i: text for i, text in enumerate(rows)}

        signals = LayoutSignals()
        signals.finished.connect(self.on_layout_finished)

        worker = LayoutWorker(indexed, self.width, self.font, signals)

        self.threadpool.start(worker)

    def on_layout_finished(self, layouts):
        for row, layout in layouts.items():
            self.layout_cache[row] = layout

        self.rebuild_prefix_sums()

        top_left = self.index(min(layouts.keys()))
        bottom_right = self.index(max(layouts.keys()))

        self.dataChanged.emit(top_left, bottom_right)

    def rebuild_prefix_sums(self):
        self.prefix_heights = []

        running = 0

        for row in range(self.loaded_rows):
            if row in self.layout_cache:
                h = self.layout_cache[row]["height"]
            else:
                h = self.default_height

            running += h

            self.prefix_heights.append(running)
