import logging

from pandas import DataFrame
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataFrameModel(QAbstractTableModel):
    def __init__(self, data: DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()) -> int:
        if parent == QModelIndex:
            return len(self._data)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        if parent == QModelIndex:
            return len(self._data.columns)

        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            logging.info("data")
            return str(self._data.iloc[index.row(), index.column()])

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

        return None
