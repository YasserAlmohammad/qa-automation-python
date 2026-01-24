import pytest
from src.utils import add, is_email, safe_div

pytestmark = pytest.mark.unit

@pytest.fixture
def valid_emails():
    return [
        "a@b.com",
        "user.name@test.org",
        "test123@example.net",
    ]

@pytest.fixture(scope="session")
def email_test_config():
    # Example of shared configuration or test context
    return {
        "allow_spaces": False,
        "allow_multiple_at": False,
    }

def test_add():
    assert add(2, 3) == 5



def test_is_email_valid_cases_fixture(valid_emails):
    for email in valid_emails:
        assert is_email(email) is True

@pytest.mark.parametrize(
    "email,expected",
    [
        (" a@b.com", False),   # leading space
        ("a@b.com ", False),   # trailing space
        ("a@@b.com", False),   # double @
        ("a@b..com", True),    # still matches regex (we'll refine later)
        ("", False),
        (None, False),
        (123, False),
    ],
)

def test_is_email_with_config(email, expected, email_test_config):
    # For now, config is not actively used,
    # but shows how fixtures + parametrization work together
    assert is_email(email) is expected

@pytest.mark.parametrize("email", ["a@b.com", "user.name@test.org", "test123@example.net"])
def test_is_email_valid_cases(email):
    assert is_email(email) is True

def test_safe_div_ok():
    assert safe_div(10, 2) == 5

# Division by zero should raise an explicit error
# instead of returning an invpylid value or crashing silently
def test_safe_div_zero_raises():
    with pytest.raises(ValueError):
        safe_div(10, 0)