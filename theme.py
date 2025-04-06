def load_stylesheet(mode="light"):
    if mode == "dark":
        return """
            QWidget {
                background-color: #2b2b2b;
                color: white;
            }
            QPushButton {
                background-color: #444;
                border: none;
                color: white;
                padding: 10px;
            }
            QLineEdit {
                background-color: #333;
                color: white;
                border: none;
                padding: 10px;
            }
        """
    else:
        return """
            QWidget {
                background-color: #f0f0f0;
                color: black;
            }
            QPushButton {
                background-color: #ddd;
                border: none;
                color: black;
                padding: 10px;
            }
            QLineEdit {
                background-color: white;
                color: black;
                border: none;
                padding: 10px;
            }
        """
