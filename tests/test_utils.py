import pytest
from src.utils import add, is_email, safe_div


def test_add():
    assert add(2, 3) == 5


@pytest.mark.parametrize(
    "value,expected",
    [
        ("a@b.com", True),
        ("abc", False),
        ("a@b", False),
        ("a.b", False),
    ],
)
def test_is_email(value, expected):
    assert is_email(value) is expected


def test_safe_div_ok():
    assert safe_div(10, 2) == 5


def test_safe_div_zero_raises():
    with pytest.raises(ValueError):
        safe_div(10, 0)