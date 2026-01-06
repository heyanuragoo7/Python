from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Base User schema
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Schema for creating a user (includes password)
class UserCreate(UserBase):
    password: str

# Schema for user response (excludes password)
class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# Schema for updating user
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

# Schema for login
class UserLogin(BaseModel):
    username: str
    password: str

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None