from PyQt6.QtCore import QModelIndex
from PyQt6.QtWidgets import QListView


class ChatView(QListView):
    PREFETCH_THRESHOLD = 20  # rows from bottom

    def __init__(self):
        super().__init__()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        model = self.model()
        if model:
            model.setWidth(self.viewport().width())

    def scrollContentsBy(self, dx, dy):
        super().scrollContentsBy(dx, dy)

        self.check_prefetch()

    def check_prefetch(self):
        model = self.model()
        if not model:
            return

        scrollbar = self.verticalScrollBar()
        if scrollbar.value() > scrollbar.maximum() - self.PREFETCH_THRESHOLD:
            if model.canFetchMore(QModelIndex()):
                model.fetchMore(QModelIndex())
