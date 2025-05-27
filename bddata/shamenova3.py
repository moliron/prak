import email
from fileinput import filename
from typing import List
from unittest.mock import Base
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from shamenova import Article, Author, Category, Review
from shamenova2 import ArticleCreate, ArticleUpdate, Articleout, AuthorCreate, AuthorOut, CategoryCreate, ReviewCreate, Reviewout

app = FastAPI()

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} 
)
Base.metadata.create_all(bind=engine)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.clone()

@app.post("/authors", response_model=AuthorOut) 
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(
        filename-author. full_name,
        email-author. email
    )
    db.add()
    db.commit()
    db.refresh(db_author)
    return db_author

@app.post("/categories”, response_model=CategoryOut")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.diet())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.post("/articles", response_model=Articleout)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = Article(
        title=article.title,
        content=article. content,
        category_id=article.category_id
    )
    db_article.authors = db.query(Author).filter(Author.id. in_(article.author_ids)).all()
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.post("/articles", response_model=Articleout) # type: ignore
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = Article(
        title=article.title,
        content=article.content,
        category_id=article.category_id
    )
    authors = []
    for author_id in article.author_ids:
        author= db.query(Author).filter(Author.id == author_id).first()
        if author:
            authors.append(author)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.get("/articles", response_model=List[Articleout])
def list_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()

@app.post("/articles/{article_id}/reviews", response_mobel=Reviewout)
def add_review(article_id: int, review: ReviewCreate,db: Session = Depends(get_db)):
    db_article = db.query(Article).get(article_id)
    if not db_article:
        raise HTTPException(status_code=484, detail="CTaTen we Haiigena")
    db_review = Review(**review.dict(), article_id=article_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@app.patch("/articles{article_id}", response_model=AuthorOut)
def update_article(article_id: int,ubdate_data: ArticleUpdate,db: Session = Depends(get_db)):
    db_article = db.query(Article).get(article_id)
    if not db_article:
        raise HTTPException(status_code=404, detail="статья не найдена")
    if ubdate_data.title is not None:
        db_article.title = ubdate_data.title
    if ubdate_data.content is not None:
        db_article. content = ubdate_data.content
    if ubdate_data.category_id is not None:
        db_article.category_id = ubdate_data.category_id
    if ubdate_data.author_ids is not None:
        db_article.authors = db.query(Author).filter(Author.id.in_(ubdate_data.author_ids)).all()

    db.commit()
    db.refresh(db_article)
    return db_article

@app.delete("/reviews{review_id}",response_model=dict)
def delete_review(review_id: int,db: Session = Depends(get_db)):
    db_review = db.query(Review).get(review_id)
    if not db_review:
        raise HTTPException(status_code=484, detail="Отзыв не найден")
    db.delete(db_review)
    db. commit()
    return {"message": "Отзыв успешно удалён"}
