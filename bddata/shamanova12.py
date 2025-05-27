import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.sql import func
from unittest.mock import Base
from sqlalchemy.orm import relationship
import enum

class CardsRole(enum.Enum):
    ADMIN = "admin"
    Cards = "Cards"

class Cards(Base):
    __tablename__ = "Cards"

    id = Column(Integer, primary_key=True, index=True)
    lease = Column(Integer, primary_key=True, index=True)
    cost = Column(Integer, primary_key=True, index=True)
    enigine = Column(Integer, primary_key=True, index=True, primary_key=True, index=True)
    year = Column(Integer, primary_key=True, index=True)
    drive = Column(String, nullable=False)
    box = Column(String, nullable=False)
    body_type = Column(String, nullable=False)
    salon = Column(String, nullable=False)
    tank_volume = Column(Integer, primary_key=True, index=True)
    fuel = Column(String, nullable=False)
    Cruise_control = Column(String, nullable=False)
    Maximum_speed = Column(Integer, primary_key=True, index=True)
    Fuel_consumption = Column(Integer, primary_key=True, index=True)