from PyQt6.QtCore import QAbstractListModel, QThreadPool


class HugeModel(QAbstractListModel):
    BATCH_SIZE = 500

    def __init__(self, backend, font):
        super().__init__()

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
