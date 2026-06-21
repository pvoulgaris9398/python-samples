import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QDockWidget,
    QLabel,
    QMainWindow,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dockable Tabs Example")
        self.setGeometry(100, 100, 800, 600)

        # 1. Set a central widget (can be anything, even just a placeholder)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_widget_layout)
        self.central_widget_layout.addWidget(QLabel("Main Window Content", self))

        # 2. Create the QDockWidget
        self.dock_widget = QDockWidget("Dockable Tabs", self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_widget)  #

        # 3. Create a QTabWidget instance
        self.tab_widget = QTabWidget()

        # 4. Create the tab views (QWidgets) and add them to the QTabWidget
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()

        self.tab_widget.addTab(self.tab1, "Tab 1")  #
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        # 5. Set the QTabWidget as the widget for the QDockWidget
        self.dock_widget.setWidget(self.tab_widget)  #

        # Optional: Allow the user to tabify other dock widgets if desired
        # self.setDockNestingEnabled(True) #

    def setup_tab1(self):
        layout = QVBoxLayout()
        label = QLabel("Content for Tab 1")
        layout.addWidget(label)
        self.tab1.setLayout(layout)

    def setup_tab2(self):
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setPlainText("Content for Tab 2, which has a QTextEdit widget.")
        layout.addWidget(text_edit)
        self.tab2.setLayout(layout)

    def setup_tab3(self):
        layout = QVBoxLayout()
        label = QLabel("Content for Tab 3")
        layout.addWidget(label)
        self.tab3.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
