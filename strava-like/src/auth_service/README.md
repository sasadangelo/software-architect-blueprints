# AuthService - Strava-like Project

This is an **authentication microservice** for your Strava-like application, built with **FastAPI** and **SQLModel**.
It provides user management, registration, login, and JWT authentication for protected endpoints.

---

## Features

Currently supported:

- Local user registration (`/register`)
- Local user login (`/login`) with JWT Bearer token

Planned / recommended future features:

- Social login (Google, Facebook)
- Password recovery via email
- User profile (`/profile`) with GET, PATCH/PUT
- Account deletion (`/profile/delete`)
- Refresh token (`/refresh`)
- Role and permissions management

---

## Installation

### Requirements

- Python >= 3.10
- Poetry
- SQLite (or another database if you want to change)

### Install with Poetry

```bash
cd strava-like/src/auth-service
poetry install
source .venv/bin/activate
```

### Environment variables

You can use a `.env` file:

```bash
SECRET_KEY=supersecret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./test.db
```

## Running the server

```bash
uvicorn main:app --reload
```

* Server runs at: http://127.0.0.1:8000
* Endpoints: /register, /login

## Testing Endpoints

### Register

```bash
curl -X POST http://127.0.0.1:8000/register \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "1234"}'
```

### Login

```bash
curl -X POST http://127.0.0.1:8000/login \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "1234"}'
```

### Response:

```bash
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```


Use this token in the Authorization: Bearer <JWT_TOKEN> header for future protected endpoints.

## Database

* Default: SQLite (test.db)
* Tables:
  * user → stores user info
  * user_role_link → links users with roles
* You can inspect the DB using SQLite CLI or DB Browser for SQLite

## Future Improvements

* OAuth login (Google, Facebook)
* Password reset via email
* Profile management
* Refresh tokens for long-lived sessions
* Role-based access control
