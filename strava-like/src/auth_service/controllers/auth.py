# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from fastapi import APIRouter, HTTPException
from dtos import UserDTO
from services.auth import AuthService
from utils.security import create_access_token
from config import settings
from datetime import timedelta


class AuthController:
    def __init__(self):
        self.router = APIRouter(prefix="/auth", tags=["auth"])
        self.auth_service = AuthService()  # Service manages the DB session internally

        # Register routes
        self.router.add_api_route(
            "/register", self.register, methods=["POST"], response_model=UserDTO
        )
        self.router.add_api_route("/login", self.login, methods=["POST"])

    async def register(self, user: UserDTO):
        # The service handles session creation, commit/rollback internally
        return self.auth_service.register_user(user)

    async def login(self, data: UserDTO):
        # Authenticate user using the service
        user = self.auth_service.authenticate_user(data.email, data.password)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Create JWT token
        token = create_access_token(
            {"sub": str(user.id)},
            timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        return {"access_token": token, "token_type": "bearer"}
