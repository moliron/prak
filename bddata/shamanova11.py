import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.sql import func
from unittest.mock import Base
from sqlalchemy.orm import relationship
import enum

class CardsRole(enum.Enum):
    ADMIN = "admin"
    lease = "lease"

class lease(Base):
    __tablename__ = "lease"

    id = Column(Integer, primary_key=True, index=True)
    start_laese = Column(Integer, primary_key=True, index=True)
    end_laese = Column(Integer, primary_key=True, index=True)
    place = Column(String, nullable=False)