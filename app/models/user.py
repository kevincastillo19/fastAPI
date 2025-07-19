from app.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "user"
    id = Column(
        Integer, primary_key=True, autoincrement=True, comment="Id del registro"
    )
    name = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
