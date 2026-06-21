from PyQt6.QtGui import QFontMetrics


class TextLayoutEngine:
    def __init__(self, font):
        self.font = font
        self.cache = {}  # key: (text, width) → layout result

    def layout(self, text, max_width):
        key = (text, max_width)
        if key in self.cache:
            return self.cache[key]

        metrics = QFontMetrics(self.font)

        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = (current_line + " " + word).strip()
            if metrics.horizontalAdvance(test_line) <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        line_height = metrics.lineSpacing()
        total_height = line_height * len(lines)

        result = {
            "lines": lines,
            "height": total_height,
            "line_height": line_height,
        }

        self.cache[key] = result
        return result
