from pydantic import BaseModel;
from typing import Optional;

class MovieModel(BaseModel):
    movie_id: Optional[str]
    title: str
    release_year: int
    genre: str
    price: float
