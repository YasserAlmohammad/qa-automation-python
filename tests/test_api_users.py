import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_user_success(base_url):
    response = requests.get(f"{base_url}/users/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "username" in data

#test error case for user not found
def test_get_user_not_found(base_url):
    response = requests.get(f"{base_url}/users/9999")

    assert response.status_code == 404

@pytest.mark.parametrize(
    "user_id,expected_status",
    [
        (1, 200),
        (2, 200),
        (9999, 404),
    ],
)
def test_get_user_by_id(base_url, user_id, expected_status):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == expected_status

@pytest.mark.parametrize("user_id", [1, 2])
def test_get_user_response_contains_required_fields(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert "username" in data
    assert "email" in data
