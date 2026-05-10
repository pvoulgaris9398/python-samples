from PyQt6.QtCore import QObject, pyqtSignal


class FetchSignals(QObject):
    finished = pyqtSignal(int, list)
