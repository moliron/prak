import email
from fileinput import filename
from typing import List
from unittest.mock import Base
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from shamenova import Article, Author, Category, Review
from shamenova2 import Cards, CardsCreate, CardsOut, CardsUpdate

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

@app.post("/Cards", response_model=CardsOut) 
def create_Cards(Cards: CardsCreate, db: Session = Depends(get_db)):
    db_Cards = Cards(
        file_name=Cards.full_name,
        email=Cards.email
    )
    db.add(db_Cards)
    db.commit()
    db.refresh(db_Cards)
    return db_Cards

@app.post("/Cards, response_model=CategoryOut")
def create_Cards(Cards: CardsCreate, db: Session = Depends(get_db)):
    db_Cards = Category(**Cards.diet())
    db.add(db_Cards)
    db.commit()
    db.refresh(db_Cards)
    return db_Cards

@app.post("/Cards", response_model=Cards)
def create_Cards(Cards: Cards, db: Session = Depends(get_db)):
    db_Cards = Cards(
        title=Cards.title,
        content=Cards.content,
        category_id=Cards.category_id
    )
    db_Cards.authors = db.query(Author).filter(Author.id. in_(Cards.author_ids)).all()
    db.add(db_Cards)
    db.commit()
    db.refresh(db_Cards)
    return db_Cards

@app.post("/Cards", response_model=CardsOut) # type: ignore
def create_Cards(Cards: CardsCreate, db: Session = Depends(get_db)):
    db_Cards = Cards(
        title=Cards.title,
        content=Cards.content,
        category_id=Cards.category_id
    )
    authors = []
    for author_id in Cards.author_ids:
        author= db.query(Author).filter(Author.id == author_id).first()
        if author:
            authors.append(author)
    db.add(db_Cards)
    db.commit()
    db.refresh(db_Cards)
    return db_Cards

@app.get("/Cards", response_model=List[Cards])
def list_Cards(db: Session = Depends(get_db)):
    return db.query(Cards).all()

@app.post("/Cards/{article_id}/Cards", response_mobel=Cards)
def add_review(article_id: int, review: CardsCreate,db: Session = Depends(get_db)):
    db_article = db.query(Cards).get(article_id)
    if not db_article:
        raise HTTPException(status_code=484, detail="CTaTen we Haiigena")
    db_Cards = Review(**review.dict(), article_id=article_id)
    db.add(db_Cards)
    db.commit()
    db.refresh(db_Cards)
    return db_Cards

@app.patch("/Cards{User_id}", response_model=CardsOut)
def update_Cards(User_id: int,ubdate_data: CardsUpdate,db: Session = Depends(get_db)):
    db_Cards = db.query(Cards).get(User_id)
    if not db_Cards:
        raise HTTPException(status_code=404, detail="статья не найдена")
    if ubdate_data.title is not None:
        db_Cards.title = ubdate_data.title
    if ubdate_data.content is not None:
        db_Cards. content = ubdate_data.content
    if ubdate_data.category_id is not None:
        db_Cards.category_id = ubdate_data.category_id
    if ubdate_data.author_ids is not None:
        db_Cards.authors = db.query(Author).filter(Author.id.in_(ubdate_data.author_ids)).all()

    db.commit()
    db.refresh(db_Cards)
    return db_Cards

@app.delete("/Cards{Cards_id}",response_model=dict)
def delete_User(Cards_id: int,db: Session = Depends(get_db)):
    db_Cards = db.query(Cards).get(Cards_id)
    if not db_Cards:
        raise HTTPException(status_code=484, detail="Отзыв не найден")
    db.delete(db_Cards)
    db. commit()
    return {"message": "Отзыв успешно удалён"}
