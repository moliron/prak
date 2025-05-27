from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

class User(BaseModel):
    id: int
    Username: str
    email: str
    password: str

class Cards(BaseModel):
    id : int
    lease : int
    cost : int
    enigine : int
    year : int
    drive: str
    box: str
    body_type: str
    salon: str
    tank_volume : int
    fuel: str
    Cruise_control: str
    Maximum_speed : str
    Fuel_consumption : int

class Lease(BaseModel):
    id : int
    start_laese : int
    end_laese : int
    place: str

class Config:
    orm_mode = True

class Config:
    orm_mode = True

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category_id: Optional[int] = None
    author_ids: Optional[List[int]] = None
    