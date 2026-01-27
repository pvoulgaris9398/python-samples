from __future__ import annotations

import sys

import SampleModel
from PyQt6.QtWidgets import QApplication, QTableView


def create_view_model():
    return SampleModel.SampleModel()


def create_view(model):
    view = QTableView()
    view.setWindowTitle("Sample View")
    view.setSizePolicy(
        view.sizePolicy().horizontalPolicy(), view.sizePolicy().verticalPolicy()
    )
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
    view.resize(1000, 600)
    view.setModel(model)
    return view


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    app = QApplication(sys.argv)

    model = create_view_model()
    view = create_view(model)

    view.show()
    app.exec()
