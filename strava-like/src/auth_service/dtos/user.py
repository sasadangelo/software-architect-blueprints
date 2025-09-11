# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel, EmailStr
from typing import List
from models.user import Role


class UserDTO(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: Optional[str] = None
    roles: List[Role] = ["member"]
    is_email_verified: bool = False
