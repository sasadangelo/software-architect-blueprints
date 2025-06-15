from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from database import init_db, get_session
from schemas.user import UserCreate, UserLogin, UserOut
from services.auth import register_user, authenticate_user
from utils.security import create_access_token
from datetime import timedelta
from config import settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # o qualsiasi altra logica di startup
    yield
    # qui puoi fare cleanup se vuoi, ad esempio chiudere connessioni


app = FastAPI(lifespan=lifespan)


@app.post("/register", response_model=UserOut)
def register(user: UserCreate, session: Session = Depends(get_session)):
    return register_user(user, session)


@app.post("/login")
def login(data: UserLogin, session: Session = Depends(get_session)):
    user = authenticate_user(data.email, data.password, session)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(
        {"sub": str(user.id)}, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}
