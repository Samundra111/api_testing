import pytest
import requests

def test_login_success(base_url,headers):
    payload={"email":'eve.holt@reqres.in',
             "password":"cityslicka"}
    response=requests.post(f"{base_url}/login",payload,headers=headers)
    assert response.status_code==200
    data=response.json()
    assert 'token' in data
    print(f"Token:{data['token']}")

## TEST 2 missing password

def test_missing_password(base_url,headers):
    payload={
        "email":"eve.holt@reqres.in",
        "password":""
    }
    response=requests.post(f"{base_url}/login",payload,headers=headers)
    assert response.status_code==400
    data=response.json()
    assert "error" in data
    print("error:",data['error'])
    
## TEST missing email

def test_missing_email(base_url,headers):
    payload={
        "password":"cityslicka"
    }
    response=requests.post(f"{base_url}/login",payload,headers=headers)
    assert response.status_code==400
    data=response.json()
    assert "error" in data
    print("error:",data['error'])

def test_user_response(base_url,auth_headers):
    response=requests.get(f"{base_url}/users",headers=auth_headers)
    response_time=response.elapsed.total_seconds()
    print(f"Response time:{response_time} seconds")
    assert response_time<2.0
