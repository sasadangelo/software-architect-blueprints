from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

# Import assoluto dal src
from main import app
from database import get_session

# --- Test database in-memory ---
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)


# Override get_session per i test
def get_test_session():
    with Session(test_engine) as session:
        yield session


app.dependency_overrides[get_session] = get_test_session

# Crea tabelle nel DB di test
SQLModel.metadata.create_all(test_engine)

client = TestClient(app)

# --- Test data ---
TEST_USER = {
    "email": "testuser@example.com",
    "password": "mypassword",
    "roles": ["member"],
}


class TestAuth:
    def test_register_user(self):
        response = client.post("/auth/register", json=TEST_USER)
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == TEST_USER["email"]
        assert "id" in data
        assert data["roles"] == TEST_USER["roles"]
        assert data["is_email_verified"] is False

    def test_register_duplicate_user(self):
        client.post("/auth/register", json=TEST_USER)
        response = client.post("/auth/register", json=TEST_USER)
        assert response.status_code == 400
        assert response.json()["detail"] == "Email already registered"

    def test_login_user(self):
        client.post("/auth/register", json=TEST_USER)
        response = client.post(
            "/auth/login",
            json={"email": TEST_USER["email"], "password": TEST_USER["password"]},
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_login_invalid_password(self):
        client.post("/auth/register", json=TEST_USER)
        response = client.post(
            "/auth/login",
            json={"email": TEST_USER["email"], "password": "wrongpassword"},
        )
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid credentials"
