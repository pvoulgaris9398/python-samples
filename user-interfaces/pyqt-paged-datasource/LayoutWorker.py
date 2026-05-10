from PyQt6.QtCore import QRunnable
from PyQt6.QtGui import QFontMetrics


class LayoutWorker(QRunnable):
    def __init__(self, rows, width, font, signals):
        super().__init__()

        self.rows = rows
        self.width = width
        self.font = font
        self.signals = signals

    def run(self):
        metrics = QFontMetrics(self.font)

        results = {}

        for row_index, text in self.rows.items():
            lines = []

            current = ""

            for word in text.split():
                test = (current + " " + word).strip()

                if metrics.horizontalAdvance(test) <= self.width:
                    current = test
                else:
                    lines.append(current)
                    current = word

            if current:
                lines.append(current)

            line_height = metrics.lineSpacing()

            results[row_index] = {
                "lines": lines,
                "height": line_height * len(lines),
                "line_height": line_height,
            }

        self.signals.finished.emit(results)
