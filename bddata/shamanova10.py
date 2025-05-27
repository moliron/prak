import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.sql import func
from unittest.mock import Base
from sqlalchemy.orm import relationship
import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    full_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    driving_experience = Column (Integer, nullable=True)
    citizenship = Column (String, nullable=True)
    inn = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column (String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    orders = relationship("Order", back_populates="user")


class Order (Base):
    __tablename__ ="orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column (Integer, ForeignKey("users.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    status = Column(String, default="pending")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    address = Column (String, nullable=False)
    total_price = Column (Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utenow)
    user = relationship("User", back_populates="orders")
    car = relationship("Car", back_populates="orders")
