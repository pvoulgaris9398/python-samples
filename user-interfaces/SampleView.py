from __future__ import annotations

import sys

import DataFrameModel as models
import prices.data_providers as dp
import SampleModel
from PyQt6.QtWidgets import (
    QApplication,
    QDockWidget,
    QMainWindow,
    QTableView,
    QTabWidget,
)


def create_view_model():
    return SampleModel.SampleModel()


def create_view(model):
    view = QTableView()

    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
    view.resize(1000, 600)
    view.setModel(model)
    return view


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    app = QApplication(sys.argv)

    dockView = QDockWidget("Dockable Tabs")

    tabs = QTabWidget()
    tabs.addTab(create_view(create_view_model()), "Sample # 3")
    tabs.addTab(create_view(models.DataFrameModel(dp.get_prices())), "Sample # 2")
    tabs.addTab(create_view(create_view_model()), "Sample # 3")

    dockView.setWidget(tabs)

    mainWindow = QMainWindow()
    mainWindow.setWindowTitle("Sample View")
    mainWindow.setSizePolicy(
        mainWindow.sizePolicy().horizontalPolicy(),
        mainWindow.sizePolicy().verticalPolicy(),
    )
    mainWindow.resize(1000, 600)

    mainWindow.setCentralWidget(dockView)

    mainWindow.show()
    app.exec()
