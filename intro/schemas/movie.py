from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Película", max_length=15)
    overview: Optional[str] = Field(default="Resumen", max_length=100, min_length=5)
    year: int = Field(le=2024, default=2024)
    rating: Optional[float] = Field(ge=0)
    category: str = Field(max_length='15')