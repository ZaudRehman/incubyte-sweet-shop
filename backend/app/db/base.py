from sqlalchemy.orm import declarative_base, declared_attr

class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

Base = declarative_base(cls=BaseModel)
