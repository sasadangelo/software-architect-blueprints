from typing import Optional, List
from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.sqlite import JSON
from enum import Enum


class Role(str, Enum):
    ROOT = "root"
    ADMIN = "admin"
    MEMBER = "member"
    PREMIUM = "premium"
    COACH = "coach"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_email_verified: bool = False
    roles: List[str] = Field(sa_column=Column(JSON), default_factory=lambda: ["member"])
