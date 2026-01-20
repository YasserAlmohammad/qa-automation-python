import re
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def add(a, b):
    return a + b


def is_email(s: str) -> bool:
    if not isinstance(s, str):
        return False
    return bool(_EMAIL_RE.match(s))


def safe_div(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b