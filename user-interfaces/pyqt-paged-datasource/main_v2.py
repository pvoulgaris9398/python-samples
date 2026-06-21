from Backend import Backend

# from ChatDelegate import ChatDelegate
from ChatView import ChatView
from LargeChatModelEx import LargeChatModelEx
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

app = QApplication([])

backend = Backend(total_rows=1_000_000)  # 1 million rows
font = QFont("Arial", 10)

model = LargeChatModelEx(backend, font)

view = ChatView()
view.setModel(model)
# view.setItemDelegate(ChatDelegate())

view.show()

app.exec()
