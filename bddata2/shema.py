from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

user = User(
    id=123,
    name="danila",
    email="qwerty123",
    is_active=True,
    created_at="2025-05-20T09:00:00"
)

print(user)