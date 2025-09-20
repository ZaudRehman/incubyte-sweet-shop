from pydantic import BaseModel, EmailStr, constr
from typing import Optional, Literal
import uuid

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8)

class UserOut(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    role: Literal["user", "admin"]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = "user"
