from PyQt6.QtWidgets import (
    QAbstractScrollArea,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self, windowTitle, view):
        super().__init__()
        self.setWindowTitle(windowTitle)

        layout = QVBoxLayout(self)
        self.view = view

        self.view.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )

        layout.addWidget(self.view)

        self.resize(300, 400)
