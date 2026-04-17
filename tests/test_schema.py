import requests
from pydantic import BaseModel

class User(BaseModel):
    id:int
    email:str
    first_name:str
    last_name:str
    avatar:str
class UserResponse(BaseModel):
    data:User

def test_user_schema(base_url,headers):
    response=requests.get(f"{base_url}/users/1",headers=headers)
    data=response.json()
    user=UserResponse(**data)
    assert user.data.id==1
    assert user.data.first_name=="George"
