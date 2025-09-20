from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.init_db import get_db
from app.models.sweet import Sweet
from app.schemas.sweet import SweetCreate, SweetOut, SweetUpdate
from app.core.security import get_current_user

router = APIRouter()

def is_admin(user: dict):
    return user.get("role") == "admin"

@router.post("/", response_model=SweetOut, status_code=status.HTTP_201_CREATED)
def create_sweet(
    sweet_in: SweetCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if not is_admin(current_user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    sweet = Sweet(**sweet_in.dict())
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

@router.get("/", response_model=List[SweetOut])
def read_sweets(db: Session = Depends(get_db)):
    sweets = db.query(Sweet).all()
    return sweets

@router.get("/search", response_model=List[SweetOut])
def search_sweets(
    name: Optional[str] = Query(None, min_length=1, max_length=100),
    category: Optional[str] = Query(None, min_length=1, max_length=50),
    price_min: Optional[float] = Query(None, ge=0),
    price_max: Optional[float] = Query(None, ge=0),
    db: Session = Depends(get_db),
):
    query = db.query(Sweet)
    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))
    if price_min is not None:
        query = query.filter(Sweet.price >= price_min)
    if price_max is not None:
        query = query.filter(Sweet.price <= price_max)
    results = query.all()
    return results

@router.put("/{sweet_id}", response_model=SweetOut)
def update_sweet(
    sweet_id: str,
    sweet_in: SweetUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if not is_admin(current_user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sweet not found")
    update_data = sweet_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(sweet, field, value)
    db.commit()
    db.refresh(sweet)
    return sweet

@router.delete("/{sweet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sweet(
    sweet_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if not is_admin(current_user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sweet not found")
    db.delete(sweet)
    db.commit()
    return
