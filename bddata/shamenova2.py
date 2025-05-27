from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

class AuthorCreate(BaseModel):
    full_name: str
    email: EmailStr

class AuthorOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr

class Config:
    orm_mode = True

class CategoryCreate(BaseModel):
    name: str

class Categoryout (BaseModel):
    id: int
    name: str

class Config:
    orm_mode = True

class ReviewCreate(BaseModel):
    reviewer_name: str
    coment: Optional[str] = None
    rating: float = Field(..., ge=6, le=5)
class Reviewout(BaseModel):
    id: int
    reviewer_name: str
    coment: Optional[str]
    rating: float
    created_at: datetime
class Config:
    orm_mode = True 
class ArticleCreate(BaseModel):
    title: str
    content: str
    category_id: int
    author_ids: List[int]
class Articleout(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime
    category: Categoryout
    authors: List[AuthorOut]
    reviews: List[Reviewout] = []
class Config:
    orm_mode = True

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category_id: Optional[int] = None
    author_ids: Optional[List[int]] = None
    