from dataclasses import Field

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address

user_data = {
    'id':1,
    'name': 'Alice',
    'isActive': True
}

user = User(id='45689', name='Dor', email='alice@mail.com', is_active=False, address=Address(city='Moscow', zip_code='57843'))

print(user)
print(user.id + 1)
print(user.address.zip_code)
print(user.model_dump_json())