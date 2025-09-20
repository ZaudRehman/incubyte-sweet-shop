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

def test_purchase_sweet(auth_token_user, sweet_id):
    with TestClient(app) as client:
        response = client.post(f"/api/sweets/{sweet_id}/purchase", 
                             json={"quantity": 1},
                             headers={"Authorization": f"Bearer {auth_token_user}"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["new_quantity"] >= 0

def test_restock_sweet(auth_token_admin, sweet_id):
    with TestClient(app) as client:
        response = client.post(f"/api/sweets/{sweet_id}/restock", 
                             json={"quantity": 10},
                             headers={"Authorization": f"Bearer {auth_token_admin}"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["new_quantity"] >= 10

def test_purchase_sweet_insufficient_stock(auth_token_user):
    # Create a sweet with 0 quantity
    from app.models.sweet import Sweet
    from decimal import Decimal
    
    db = TestingSessionLocal()
    sweet = Sweet(
        name="Out of Stock Sweet",
        category="Test",
        price=Decimal("5.99"),
        quantity=0
    )
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    sweet_id = str(sweet.id)
    db.close()
    
    with TestClient(app) as client:
        response = client.post(f"/api/sweets/{sweet_id}/purchase", 
                             json={"quantity": 1},
                             headers={"Authorization": f"Bearer {auth_token_user}"})
    assert response.status_code == 400
    assert "Not enough quantity in stock" in response.json()["detail"]

def test_restock_sweet_requires_admin(auth_token_user, sweet_id):
    with TestClient(app) as client:
        response = client.post(f"/api/sweets/{sweet_id}/restock", 
                             json={"quantity": 10},
                             headers={"Authorization": f"Bearer {auth_token_user}"})
    assert response.status_code == 403

def test_purchase_sweet_requires_auth(sweet_id):
    with TestClient(app) as client:
        response = client.post(f"/api/sweets/{sweet_id}/purchase", json={"quantity": 1})
    assert response.status_code == 401

def test_purchase_nonexistent_sweet(auth_token_user):
    with TestClient(app) as client:
        response = client.post("/api/sweets/00000000-0000-0000-0000-000000000000/purchase", 
                             json={"quantity": 1},
                             headers={"Authorization": f"Bearer {auth_token_user}"})
    assert response.status_code == 404