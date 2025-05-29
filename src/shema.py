from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class UserCreate(BaseModel):
    role: Optional[str]="user"
    full_name: str
    birth_date: date
    driving_experience: Optional[int]=None
    citizenship: Optional[str]=None
    inn: Optional [str]=None
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    role: Optional[str]=None
    full_name: Optional [str]=None
    birth_date: Optional [date]=None
    driving_experience: Optional[int]
    citizenship: Optional[str]=None
    inn: Optional [str]=None
    email: Optional[EmailStr]=None
    password: Optional[str]=None

class UserResponse(BaseModel) :
    id: int
    role: str
    full_name: str
    birth_date: date
    driving_experience: Optional[int]
    citizenship: Optional[str]
    inn: Optional [str]
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class LoginRequest(BaseModel) :
    email: EmailStr
    password: str

