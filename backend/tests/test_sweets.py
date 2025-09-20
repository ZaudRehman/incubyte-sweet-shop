import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.db.init_db import get_db
import os

DATABASE_URL = os.getenv("DATABASE_URL_TEST", "sqlite:///./test.db")

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

@pytest.fixture
def sweet_id():
    """Create a test sweet and return its ID"""
    from app.models.sweet import Sweet
    from decimal import Decimal
    
    db = TestingSessionLocal()
    sweet = Sweet(
        name="Test Sweet",
        category="Test Category",
        price=Decimal("5.99"),
        quantity=10
    )
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    sweet_id = str(sweet.id)
    db.close()
    return sweet_id

def test_create_sweet_requires_admin(auth_token_admin):
    with TestClient(app) as client:
        response = client.post("/api/sweets/", 
                             json={
                                 "name": "Mango Delight",
                                 "category": "Fruit",
                                 "price": 2.50,
                                 "quantity": 100
                             },
                             headers={"Authorization": f"Bearer {auth_token_admin}"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Mango Delight"
    assert data["quantity"] == 100

def test_read_sweets(auth_token_user):
    with TestClient(app) as client:
        response = client.get("/api/sweets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_sweets(auth_token_user):
    with TestClient(app) as client:
        response = client.get("/api/sweets/search?name=Mango")
    assert response.status_code == 200
    sweets = response.json()
    for sweet in sweets:
        assert "Mango" in sweet["name"] or "mango" in sweet["name"].lower()

def test_create_sweet_requires_auth():
    with TestClient(app) as client:
        response = client.post("/api/sweets/", json={
            "name": "Unauthorized Sweet",
            "category": "Test",
            "price": 2.50,
            "quantity": 100
        })
    assert response.status_code == 401

def test_create_sweet_user_forbidden(auth_token_user):
    with TestClient(app) as client:
        response = client.post("/api/sweets/", 
                             json={
                                 "name": "User Sweet",
                                 "category": "Test",
                                 "price": 2.50,
                                 "quantity": 100
                             },
                             headers={"Authorization": f"Bearer {auth_token_user}"})
    assert response.status_code == 403

def test_update_sweet(auth_token_admin, sweet_id):
    with TestClient(app) as client:
        response = client.put(f"/api/sweets/{sweet_id}", 
                            json={
                                "name": "Updated Sweet",
                                "price": 7.99
                            },
                            headers={"Authorization": f"Bearer {auth_token_admin}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Sweet"
    assert float(data["price"]) == 7.99

def test_delete_sweet(auth_token_admin, sweet_id):
    with TestClient(app) as client:
        response = client.delete(f"/api/sweets/{sweet_id}",
                               headers={"Authorization": f"Bearer {auth_token_admin}"})
    assert response.status_code == 204

def test_search_sweets_by_category(auth_token_user):
    with TestClient(app) as client:
        response = client.get("/api/sweets/search?category=Chocolate")
    assert response.status_code == 200
    sweets = response.json()
    for sweet in sweets:
        assert "Chocolate" in sweet["category"] or "chocolate" in sweet["category"].lower()

def test_search_sweets_by_price_range(auth_token_user):
    with TestClient(app) as client:
        response = client.get("/api/sweets/search?price_min=1.0&price_max=10.0")
    assert response.status_code == 200
    sweets = response.json()
    for sweet in sweets:
        assert 1.0 <= float(sweet["price"]) <= 10.0