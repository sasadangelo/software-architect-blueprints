import os


class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DATABASE_URL = "sqlite:///./test.db"


settings = Settings()
