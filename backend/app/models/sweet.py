import uuid
from sqlalchemy import Column, String, Numeric, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class Sweet(Base):
    __tablename__ = "sweet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(100), nullable=False, index=True)
    category = Column(String(50), nullable=False, index=True)
    price = Column(Numeric(8, 2), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
