from cProfile import Profile
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    region: str
    postal_code: str
    country: str

class Company(BaseModel):
    name: str
    industry: str
    description: str
    website: Optional[HttpUrl] = None

class Profil(BaseModel):
    username: str
    full_name: str
    bio: str
    status_message: str
    job_title: str
    department: str
    interests: List[str]
    skills: List[str]
    favorite_quote: Optional[str] = None
    notes: Optional[str] = None

class UserFull(BaseModel):
    id: int
    email: EmailStr
    phone: str
    registered_ad: datetime
    is_active: bool
    address: Address
    company: Company
    profile: Profile

user_Full = UserFull(
    id=123,
    email="ivan.petrov@example.com",
    phone="+7-495-123-45-67",
    registered_at=datetime.now(),
    is_active=True,
    address={
        "street": "ул.Ленина,Д.10",
        "city": "Москва",
        "region":"Московская область",
        "postal_code": "101000",
        "country":"Россия"
    },
company={
    "name" : "ООО «Технософт»",
    "industry": "Информационные технологии",
    "description": "Разработка программного обеспечения",
    "website": "https://technosoft.ru"
},
profile={
    "username": "ivanpetrov",
    "full name": "Иван Петров",
    "bio": "Студент",
    "status message": "Работаю над новым проектом",
    "job_title": "джуниор разработчик",
    "department": "Отдел разработки",
    "interests": ["Программирование", "Искусственный интеллект", "Брейнрот"],
    "skills": ["Python", "Django", "FastAPT"],
    "Favorite_quote": "Лирали ларила",
    "notes": "участвует в наставничестве новых сотрудников"
    }
)
print(user_Full)