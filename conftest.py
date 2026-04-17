import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# These stay here for the fixtures to use
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-api-key": API_KEY}


@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def headers():
    return HEADERS

@pytest.fixture
def auth_token(base_url,headers):
    payload={
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }
    response=requests.post(f"{base_url}/login",payload,headers=headers)
    token=response.json()['token']
    return token
@pytest.fixture
def auth_headers(headers,auth_token):
    combined_headers=headers.copy()
    combined_headers['authorization']=f"Bearer {auth_token}"
    return combined_headers

@pytest.fixture
def get_all_user():
    return requests.get(f"{BASE_URL}/users", headers=HEADERS)

@pytest.fixture
def user_id_1():
    return requests.get(f"{BASE_URL}/users/1", headers=HEADERS)