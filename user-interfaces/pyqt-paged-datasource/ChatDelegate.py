from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QStyledItemDelegate


class ChatDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        model = index.model()
        layout = model.get_layout(index)

        painter.save()

        y = option.rect.top()

        for line in layout["lines"]:
            painter.drawText(option.rect.left(), y + layout["line_height"], line)
            y += layout["line_height"]

        painter.restore()

    def sizeHint(self, option, index):
        model = index.model()
        layout = model.get_layout(index)
        return QSize(option.rect.width(), layout["height"])
