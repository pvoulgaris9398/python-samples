from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QStyle, QStyledItemDelegate


class ChatDelegateEx(QStyledItemDelegate):
    PADDING = 6

    def paint(self, painter, option, index):
        model = index.model()

        painter.save()

        rect = option.rect

        # ---- Selected background ----
        if option.state & QStyle.StateFlag.State_Selected:
            painter.fillRect(rect, option.palette.highlight())

        # ---- Get cached layout ----
        layout = model.layout_cache.get(index.row())

        # ---- Layout not ready yet ----
        if layout is None:
            painter.drawText(
                rect.adjusted(self.PADDING, self.PADDING, -self.PADDING, -self.PADDING),
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
                "Loading...",
            )

            painter.restore()
            return

        # ---- Paint cached lines ----
        y = rect.top() + self.PADDING

        for line in layout["lines"]:
            painter.drawText(
                rect.left() + self.PADDING, y + layout["line_height"], line
            )

            y += layout["line_height"]

        painter.restore()

    def sizeHint(self, option, index):
        model = index.model()

        layout = model.layout_cache.get(index.row())

        # Layout already computed
        if layout:
            return QSize(option.rect.width(), layout["height"] + self.PADDING * 2)

        # Placeholder estimate
        return QSize(option.rect.width(), model.default_height)
