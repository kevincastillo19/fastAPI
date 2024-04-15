from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Id del registro")
    title = Column(String(150), nullable=False)
    overview = Column(String(250), nullable=False, default="Resumen")
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)