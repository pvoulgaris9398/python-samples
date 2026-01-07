from __future__ import annotations

import sys

import pandas as pd
from PyQt6.QtCore import (  # noqa: F401
    QAbstractTableModel,
    QModelIndex,
    QSize,
    Qt,
    pyqtSignal,
)
from PyQt6.QtWidgets import QApplication, QTableView


class PandasModel(QAbstractTableModel):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    df = pd.read_csv(r"C:\Users\Peter\_work\_tempdata\titanic.csv")

    view = QTableView()
    view.setWindowTitle("Pandas DataFrame in QTableView")
    view.setSizePolicy(
        view.sizePolicy().horizontalPolicy(), view.sizePolicy().verticalPolicy()
    )
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
    model = PandasModel(df)
    view.setModel(model)
    view.show()
    app.exec()
