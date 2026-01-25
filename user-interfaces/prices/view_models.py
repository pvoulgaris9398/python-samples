from __future__ import annotations

import data_providers
import pandas as pd
from pandas.api.types import is_datetime64_any_dtype
from PyQt6.QtCore import (  # noqa: F401
    QAbstractTableModel,
    QModelIndex,
    Qt,
    pyqtSignal,
)


def create_prices_model():
    df = data_providers.get_prices()
    return PricesModel(df)


class PricesModel(QAbstractTableModel):
    customDataModified = pyqtSignal(int, int)

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        if parent == QModelIndex():
            return len(self._dataframe.columns)

        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            value = self._dataframe.iloc[index.row(), index.column()]
            if is_datetime64_any_dtype(value):
                return value.strftime("%m/%d/%Y")
            else:
                return str(value)

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role=Qt.ItemDataRole
    ):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._dataframe.columns[section])
            if orientation == Qt:
                return str(self._dataframe.index[section])

        return None
