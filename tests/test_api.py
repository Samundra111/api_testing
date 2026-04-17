import requests
import pytest

def test_user_1_fixture(user_id_1):
    assert user_id_1.status_code == 200
    data = user_id_1.json()
    assert data['data']['id'] == 1

def test_user_2_direct(base_url, headers):
    # Pass base_url and headers as arguments!
    response = requests.get(f"{base_url}/users/2", headers=headers)
    assert response.status_code == 200
    assert response.json()['data']['first_name'] == "Janet"

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_status_code(base_url, headers, user_id):
    # Pass them here too!
    response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    assert response.status_code == 200

@pytest.mark.parametrize("user_id, expected_last_name", [
    (1, "Bluth"), (2, "Weaver"), (3, "Wong")
])
def test_last_name(base_url, headers, user_id, expected_last_name):
    # And here!
    response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    data = response.json()
    assert data['data']['last_name'] == expected_last_name