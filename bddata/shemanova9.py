from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, DateTime, Table, Float
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class BodyType(Base):
    __tablename__ = "body_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class FuelType(Base):
    __tablename__ = "fuel_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class DriveType(Base):
    __tablename__ = "drive_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class TransmissionType(Base):
    __tablename__ = "transmission_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class InteriorType(Base):
    __tablename__ = "interior_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class EngineType(Base):
    __tablename__ = "engine_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year = Column (Integer, nullable=False)
    engine_id = Column(Integer, ForeignKey("engine_types.id"), nullable=False)
    drive_id = Column(Integer, ForeignKey ("drive_types.id"), nullable=False)
    transmission_id = Column(Integer, ForeignKey("transmission_types.id"), nullable=False)
    interdor_id = Column (Integer, ForeignKey("interior_types.id"), nullable=False)
    uel_tank_capacity = Column (Float, nullable=False)
    fuel_type_id = Column(Integer, ForeignKey("fuel_types.id"), nullable=False)
    cruise_control = Column(Boolean, default=False)
    body_type_id = Column(Integer, ForeignKey("body_types.id"), nullable=False)
    max_speed = Column(Integer, nullable=False)
    uel_consumption = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    url_image = Column(String, nullable=True)

    engine = relationship("EngineType")
    drive = relationship("DriveType")
    transmission = relationship("TransmissionType")
    interior = relationship("InteriorType")
    fuel_type = relationship("FuelType")
    body_type = relationship("BodyType")
    orders = relationship("Order", back_populates="car")
