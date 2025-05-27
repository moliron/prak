from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id - Column(Integer, primary_key=True, index=True)
    name = Column (String, index=True)
    email = Column(String, unique=True, index=True)
    
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column (String, nullable=True)
    completed = Column(Boolean, default=False)
    user_id = Column (Integer, ForeignKey("users.id"))

    user = relationship("User")