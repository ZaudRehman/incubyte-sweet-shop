import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.db.init_db import get_db
import os

DATABASE_URL = os.getenv("DATABASE_URL_TEST", "sqlite:///./test.db")

# Create sync engine and session for testing
engine_test = create_engine(DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)

@pytest.fixture
def auth_token_user():
    """Create a test user and return auth token"""
    from app.core.security import create_access_token
    return create_access_token({"sub": "testuser", "username": "testuser", "email": "test@example.com", "role": "user"})

@pytest.fixture
def auth_token_admin():
    """Create a test admin and return auth token"""
    from app.core.security import create_access_token
    return create_access_token({"sub": "admin", "username": "admin", "email": "admin@example.com", "role": "admin"})

def test_register_user_success():
    with TestClient(app) as client:
        response = client.post("/api/auth/register", json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "strongpassword123"
        })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"

def test_register_duplicate_username_email():
    with TestClient(app) as client:
        client.post("/api/auth/register", json={
            "username": "dupuser",
            "email": "dupuser@example.com",
            "password": "somepassword123"
        })
        response = client.post("/api/auth/register", json={
            "username": "dupuser",
            "email": "dupuser@example.com",
            "password": "somepassword123"
        })
    assert response.status_code == 400
    assert response.json()["detail"] == "Username or email already registered"

def test_login_user_success():
    with TestClient(app) as client:
        client.post("/api/auth/register", json={
            "username": "loginuser",
            "email": "loginuser@example.com",
            "password": "mypassword123"
        })
        response = client.post("/api/auth/login", data={
            "username": "loginuser",
            "password": "mypassword123"
        })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password():
    with TestClient(app) as client:
        client.post("/api/auth/register", json={
            "username": "wrongpassuser",
            "email": "wpuser@example.com",
            "password": "correctpassword123"
        })
        response = client.post("/api/auth/login", data={
            "username": "wrongpassuser",
            "password": "wrongpassword"
        })
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect email/username or password"

def test_login_with_email():
    with TestClient(app) as client:
        client.post("/api/auth/register", json={
            "username": "emailuser",
            "email": "emailuser@example.com",
            "password": "password123"
        })
        response = client.post("/api/auth/login", data={
            "username": "emailuser@example.com",
            "password": "password123"
        })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_register_validation():
    with TestClient(app) as client:
        # Test short password
        response = client.post("/api/auth/register", json={
            "username": "testuser2",
            "email": "test2@example.com",
            "password": "123"
        })
    assert response.status_code == 422  # Validation error

def test_register_invalid_email():
    with TestClient(app) as client:
        response = client.post("/api/auth/register", json={
            "username": "testuser3",
            "email": "invalid-email",
            "password": "password123"
        })
    assert response.status_code == 422  # Validation error
