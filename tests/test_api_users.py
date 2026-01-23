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
