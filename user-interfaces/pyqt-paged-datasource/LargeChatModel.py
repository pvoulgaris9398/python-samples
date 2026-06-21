from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from TextLayoutEngine import TextLayoutEngine


class LargeChatModel(QAbstractListModel):
    BATCH_SIZE = 100  # how many rows to fetch at once

    def __init__(self, backend, font, parent=None):
        super().__init__(parent)

        self.backend = backend
        self.font = font

        self.total_rows = backend.total_rows
        self.loaded_rows = 0

        self.messages = []
        self.layout_cache = {}
        self.width = 400

        self.layout_engine = TextLayoutEngine(font)

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
        remaining = self.total_rows - self.loaded_rows
        count = min(self.BATCH_SIZE, remaining)

        new_data = self.backend.fetch(self.loaded_rows, count)

        self.beginInsertRows(
            QModelIndex(), self.loaded_rows, self.loaded_rows + count - 1
        )

        self.messages.extend(new_data)
        self.loaded_rows += count

        self.endInsertRows()

    def setWidth(self, width):
        if self.width != width:
            self.width = width
            self.layout_cache.clear()

    def get_layout(self, index):
        row = index.row()

        if row in self.layout_cache:
            return self.layout_cache[row]

        text = self.messages[row]
        layout = self.layout_engine.layout(text, self.width)

        self.layout_cache[row] = layout
        return layout
