from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QTextEdit
from logic import evaluate_expression
from theme import load_stylesheet
from history import HistoryManager


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính")
        self.setFixedSize(300, 540)
        self.history = HistoryManager()
        self.current_theme = "light"  # theme mặc định
        self.create_ui()
        self.apply_theme()

    def create_ui(self):
        layout = QVBoxLayout()

        # Nút chuyển giao diện
        self.theme_button = QPushButton("🌙 Đổi giao diện")
        self.theme_button.setStyleSheet("font-size: 14px; padding: 8px;")
        self.theme_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_button)

        # Ô hiển thị kết quả
        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)
        self.result_field.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.result_field)

        # Các nút bấm
        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)
        ]

        for btn in buttons:
            if len(btn) == 3:
                text, row, col = btn
                rowspan, colspan = 1, 1
            else:
                text, row, col, rowspan, colspan = btn

            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 15px;")
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col, rowspan, colspan)

        layout.addLayout(grid_layout)

        # Hiển thị lịch sử
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.history_display)

        self.setLayout(layout)

    def on_button_click(self):
        text = self.sender().text()
        if text == 'C':
            self.result_field.clear()
        elif text == '=':
            expression = self.result_field.text()
            result = evaluate_expression(expression)
            self.result_field.setText(result)
            self.history.add(expression, result)
            self.update_history_display()
        else:
            self.result_field.setText(self.result_field.text() + text)

    def update_history_display(self):
        self.history_display.clear()
        for entry in reversed(self.history.get_history()[-10:]):
            self.history_display.append(entry)

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(load_stylesheet(self.current_theme))
        if self.current_theme == "dark":
            self.theme_button.setText("☀️ Đổi giao diện")
        else:
            self.theme_button.setText("🌙 Đổi giao diện")
