# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from sqlmodel import Session, select
from fastapi import HTTPException
from database import engine
from models import UserDAO
from dtos import UserDTO
from utils.security import hash_password, verify_password


class AuthService:
    def register_user(self, user_dto: UserDTO) -> UserDTO:
        # Create a new DB session
        with Session(engine) as session:
            try:
                # Check if email is already registered
                existing = session.exec(
                    select(UserDAO).where(UserDAO.email == user_dto.email)
                ).first()
                if existing:
                    raise HTTPException(
                        status_code=400, detail="Email already registered"
                    )

                # Hash the password before storing
                hashed = hash_password(user_dto.password)
                user_dao = UserDAO(
                    email=user_dto.email, hashed_password=hashed, roles=user_dto.roles
                )

                # Add user to session and commit
                session.add(user_dao)
                session.commit()
                session.refresh(user_dao)  # Load generated fields like id

                # Return DTO
                return UserDTO(
                    id=user_dao.id,
                    email=user_dao.email,
                    roles=user_dao.roles,
                    is_email_verified=user_dao.is_email_verified,
                )
            except Exception:
                # Rollback on error
                session.rollback()
                raise

    def authenticate_user(self, email: str, password: str) -> UserDAO | None:
        # Create a new DB session
        with Session(engine) as session:
            # Retrieve user by email
            user = session.exec(select(UserDAO).where(UserDAO.email == email)).first()
            # Verify password
            if user and verify_password(password, user.hashed_password):
                return user
            return None
