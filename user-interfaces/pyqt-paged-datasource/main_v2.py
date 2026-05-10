import sys

from Backend import Backend
from ChatDelegateEx import ChatDelegateEx
from ChatView import ChatView
from LargeChatModelEx import LargeChatModelEx
from MainWindow import MainWindow
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

app = QApplication([])

backend = Backend(total_rows=1_000_000)  # 1 million rows
font = QFont("Arial", 10)

model = LargeChatModelEx(backend, font)

view = ChatView()
view.setModel(model)
view.setItemDelegate(ChatDelegateEx())

window = MainWindow("", view)

window.show()

sys.exit(app.exec())
