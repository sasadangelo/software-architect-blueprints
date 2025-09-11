# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import os


class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DATABASE_URL = "sqlite:///./test.db"


settings = Settings()
