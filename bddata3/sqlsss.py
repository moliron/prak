from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer)
    Username = Column(String)
    email = Column(String)
    password = Column(String)

class Cards(Base):
    __tablename__ = "cards"

    id = Column(Integer)
    lease = Column(Integer)
    cost = Column(Integer)
    enigine = Column(Integer)
    year = Column(Integer)
    drive = Column(String)
    box = Column(String)
    body_type = Column(String)
    salon = Column(String)
    tank_volume = Column(Integer)
    fuel = Column(String)
    Cruise_control = Column(String)
    Maximum_speed = Column(Integer)
    Fuel_consumption = Column(Integer)

class lease(Base):
    __tablename__ = "lease"

    id = Column(Integer)
    start_laese = Column(Integer)
    end_laese = Column(Integer)
    place = Column(String)