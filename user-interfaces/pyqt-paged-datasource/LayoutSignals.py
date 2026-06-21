from PyQt6.QtCore import QObject, pyqtSignal


class LayoutSignals(QObject):
    finished = pyqtSignal(dict)
