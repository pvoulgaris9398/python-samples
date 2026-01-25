from __future__ import annotations

import sys

import view_models as vm
import views as v
from PyQt6.QtWidgets import QApplication

"""
To Do:
- Add logic to make this a tab control and add dynamically
created views
- Move logic for creating/destroying _views_ to some
sort of window manager
- See how this all works in Python and PyQt
"""
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    app = QApplication(sys.argv)

    model = vm.create_prices_model()
    view = v.create_view(model)

    view.show()
    app.exec()
