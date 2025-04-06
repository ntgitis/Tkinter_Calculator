class HistoryManager:
    def __init__(self):
        self.history = []

    def add(self, expression: str, result: str):
        self.history.append(f"{expression} = {result}")

    def get_history(self):
        return self.history

    def clear(self):
        self.history.clear()
