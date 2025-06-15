from pydantic import BaseModel, EmailStr
from typing import List
from models.user import Role


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    roles: List[Role]
    is_email_verified: bool
