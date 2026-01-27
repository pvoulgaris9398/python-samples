from PyQt6.QtCore import (  # noqa: F401
    QAbstractTableModel,
    QModelIndex,
    Qt,
    pyqtSignal,
)


class SampleModel(QAbstractTableModel):
    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)

    def rowCount(self, parent=QModelIndex()) -> int:
        # print(parent)
        if parent == QModelIndex():
            return 3

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        # print(parent)
        if parent == QModelIndex():
            return 4

        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        # print(index)
        # print(role)
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.ToolTipRole:
            return "This is my tooltip!"

        elif role == Qt.ItemDataRole.DisplayRole:
            match index:
                case QModelIndex(column=0):
                    return "Color"
                case QModelIndex(column=1):
                    return "Make"
                case QModelIndex(column=2):
                    return "Model"
                case _:
                    return "Default"

        else:
            return "foo"

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role=Qt.ItemDataRole
    ):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                match section:
                    case 0:
                        return "Color"
                    case 1:
                        return "Make"
                    case 2:
                        return "Model"
                    case 3:
                        return "Year"
                    case _:
                        return "Default"
            if orientation == Qt:
                return "The Other Header"

        return None
