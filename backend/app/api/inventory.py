from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.init_db import get_db
from app.models.sweet import Sweet
from app.schemas.sweet import PurchaseRequest, RestockRequest, InventoryOperationResponse
from app.core.security import get_current_user

router = APIRouter()

def is_admin(user: dict):
    return user.get("role") == "admin"

@router.post("/{sweet_id}/purchase", response_model=InventoryOperationResponse)
def purchase_sweet(
    sweet_id: str,
    purchase: PurchaseRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sweet not found")

    if sweet.quantity < purchase.quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough quantity in stock")

    sweet.quantity -= purchase.quantity
    db.commit()
    db.refresh(sweet)
    return InventoryOperationResponse(success=True, new_quantity=sweet.quantity)

@router.post("/{sweet_id}/restock", response_model=InventoryOperationResponse)
def restock_sweet(
    sweet_id: str,
    restock: RestockRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if not is_admin(current_user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")

    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sweet not found")

    sweet.quantity += restock.quantity
    db.commit()
    db.refresh(sweet)
    return InventoryOperationResponse(success=True, new_quantity=sweet.quantity)
