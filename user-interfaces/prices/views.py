from PyQt6.QtWidgets import QTableView


def create_view(model):
    view = QTableView()
    view.setWindowTitle("Prices Module")
    view.setSizePolicy(
        view.sizePolicy().horizontalPolicy(), view.sizePolicy().verticalPolicy()
    )
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
    view.resize(1000, 600)
    view.setModel(model)
    return view
