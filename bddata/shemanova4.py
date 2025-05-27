from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table, Float
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

article_authors = Table(
    "article_authors",
    Base.metadata,
    Column("article_id", ForeignKey("articles.id"), primary_key=True),
    Column("author_id", ForeignKey("authors.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    enail = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)

    articles = relationship("Article", secondary=article_authors, back_populates="authors")

class Cards(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    lease = Column(Integer, primary_key=True)
    cost = Column(Integer, primary_key=True)
    enigine = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    drive = Column(String, unique=True, nullable=False)
    box = Column(String, unique=True, nullable=False)
    body_type = Column(String, unique=True, nullable=False)
    salon = Column(String, unique=True, nullable=False)
    tank_volume = Column(Integer, primary_key=True)
    fuel = Column(String, unique=True, nullable=False)
    Cruise_control = Column(String, unique=True, nullable=False)
    Maximum_speed = Column(Integer, primary_key=True)
    fuel_consumption = Column(Integer, primary_key=True)

class Lease(Base):
    __tablename__ = "lease"
   
    id = Column(Integer, primary_key=True)
    start_laese = Column(Integer, primary_key=True)
    end_laese = Column(Integer, primary_key=True)
    place = Column(String, unique=True, nullable=False)
   
    category = relationship("Category")
    authors = relationship("Author", secondary=article_authors, back_populates="articles")
    reviews = relationship("Review", back_populates="article")