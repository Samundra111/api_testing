import requests
import pytest

import os



def test_create_user(base_url,headers):
    payload = {
        "name": "Sam",
        "job": "QA Engineer"
    }
    response=requests.post(f"{base_url}/users",json=payload,headers=headers)
    data=response.json()
    assert response.status_code==201
    assert data['name']=="Sam"
    assert data['job']=="QA Engineer"
    assert "id" in data

def test_update_user(base_url,headers):
    payload={
        "name":"Updated Sam",
        "job":"Updated ho"
    } 
    response=requests.put(f"{base_url}/users/2",json=payload,headers=headers)
    assert response.status_code==200
    data=response.json()
    assert data['name']=="Updated Sam"
    assert data['job']=="Updated ho"

def test_delete_user(base_url,headers):
    response=requests.delete(f"{base_url}/users/2",headers=headers)
    assert response.status_code==204

