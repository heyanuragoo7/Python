from pydentic import EmailStr, BaseModel
from typing import Union

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    
