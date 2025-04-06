#B23DCVT302 - Tran Gia Nam - Nhom 3
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("330x450")
        self.configure(bg="black")
        self.expression = ""
        self.result_var = tk.StringVar(value="0")

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = tk.Label(
            self, textvariable=self.result_var,
            font=("San Francisco Pro", 30),
            bg="black", fg="white",
            anchor="e", padx=15, pady=10
        )
        display.pack(fill="both")

    def create_buttons(self):
        button_matrix = [
            ["AC", "±", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row in button_matrix:
            frame = tk.Frame(self, bg="black")
            frame.pack(expand=True, fill="both", padx=5, pady=3)  # Thêm khoảng cách giữa các hàng

            for char in row:
                btn = tk.Button(
                    frame, text=char, font=("San Francisco Pro", 20),
                    fg="white", bg=self.get_color(char),
                    relief="flat", command=lambda x=char: self.on_click(x)
                )
                btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)  # Thêm khoảng cách giữa các nút

    def get_color(self, text):
        if text in ["+", "-", "*", "/", "="]:
            return "#FF9F0A"  # Màu cam
        elif text in ["AC", "±", "%"]:
            return "#5C5C5F"  # Màu xám
        else:
            return "#2A2A2C"  # Màu đen

    def on_click(self, char):
        if char == "AC":
            self.expression = ""
            self.result_var.set("0")
        elif char == "=":
            try:
                result = eval(self.expression)
                result = round(result, 6) if isinstance(result, float) else result
                self.result_var.set(str(result))
                self.expression = str(result)
            except:
                self.result_var.set("Lỗi")
                self.expression = ""
        elif char == "±":
            if self.expression:
                self.expression = self.expression[1:] if self.expression.startswith("-") else "-" + self.expression
                self.result_var.set(self.expression)
        else:
            self.expression += char
            self.result_var.set(self.expression)

if __name__ == "__main__":
    Calculator().mainloop()
