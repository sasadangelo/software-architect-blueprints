# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from controllers import AuthController
from database import init_db


# --- Lifespan per inizializzare il DB ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inizializza DB (crea tabelle se non esistono)
    init_db()
    yield
    # eventuale cleanup


app = FastAPI(lifespan=lifespan)

# --- Monta il router AuthController ---
# Passiamo la dependency `get_session` al costruttore
auth_controller = AuthController()
app.include_router(auth_controller.router)


# --- Root endpoint di test ---
@app.get("/")
def root():
    return {"message": "AuthService is running"}
