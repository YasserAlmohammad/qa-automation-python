def add(a, b):
    return a + b


def is_email(s: str) -> bool:
    return "@" in s and "." in s


def safe_div(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b