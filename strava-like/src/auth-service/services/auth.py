from fastapi import HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password, verify_password


def register_user(user_in: UserCreate, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == user_in.email)).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user_in.password)
    new_user = User(email=user_in.email, hashed_password=hashed)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def authenticate_user(email: str, password: str, session: Session):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
