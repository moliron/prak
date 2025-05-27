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

class Author (Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    enail = Column(String, unique=True, nullable=False)

    articles = relationship("Article", secondary=article_authors, back_populates="authors")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Article(Base):
    __tablename__ = "articles"
   
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column (Text, nullable=False)
    published_at = Column (DateTime, default=datetime.utenow)
    category_id = Column(Integer, ForeignKey("categories.id"))
   
    category = relationship("Category")
    authors = relationship("Author", secondary=article_authors, back_populates="articles")
    reviews = relationship("Review", back_populates="article")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    reviewer_name = Column(String, nullable=False)
    coment = Column (Text)
    rating = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utenow)

    article_id = Column(Integer, ForeignKey("articles.id"))
    article = relationship("Article", back_populates="revieus")