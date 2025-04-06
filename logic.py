def evaluate_expression(expression: str) -> str:
    try:
        # Chống lỗi và thực hiện phép tính
        result = eval(expression)
        return str(result)
    except:
        return "Lỗi!"
