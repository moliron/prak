from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

incoming_data = {
    "id": "54651654",
    "name": "Bob",
    "email": "bob@example.com",
    "is_active": "true",
    "created_at": "2025-05-19T15:30:00"
}

user = User(**incoming_data)
print(user)