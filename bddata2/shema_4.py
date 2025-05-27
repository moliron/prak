from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    genre: str

class PrintedBook(BookBase):
    pages: int
    cover_type: str
    weight_grams: Optional[int] = None

class OnlineBook(BookBase):
    file_format: str
    film_size_mb: float
    download_url: HttpUrl