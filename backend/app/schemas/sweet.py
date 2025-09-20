from pydantic import BaseModel, condecimal, conint, constr
from typing import Optional
import uuid

class SweetBase(BaseModel):
    name: constr(min_length=2, max_length=100)
    category: constr(min_length=2, max_length=50)
    price: condecimal(gt=0, max_digits=8, decimal_places=2)
    quantity: conint(ge=0)

class SweetCreate(SweetBase):
    pass

class SweetUpdate(BaseModel):
    name: Optional[constr(min_length=2, max_length=100)] = None
    category: Optional[constr(min_length=2, max_length=50)] = None
    price: Optional[condecimal(gt=0, max_digits=8, decimal_places=2)] = None
    quantity: Optional[conint(ge=0)] = None

class SweetOut(SweetBase):
    id: uuid.UUID

    class Config:
        orm_mode = True

# Inventory operation schemas
class PurchaseRequest(BaseModel):
    quantity: conint(gt=0)

class RestockRequest(BaseModel):
    quantity: conint(gt=0)

class InventoryOperationResponse(BaseModel):
    success: bool
    new_quantity: int
