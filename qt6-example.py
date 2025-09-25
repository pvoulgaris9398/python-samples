import sys

# For some reason, although I definitely installed PyQt6
# the intellisense _does not work_
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)


def main():
    app = QApplication([])
    window = QWidget()

    window.setWindowTitle("Python PyQt Test App")
    window.setGeometry(100, 100, 400, 300)

    layout = QHBoxLayout()
    layout.addWidget(QPushButton("Left"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(QPushButton("Right"))
    window.setLayout(layout)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
