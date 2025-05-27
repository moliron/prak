import email
from fileinput import filename
from typing import List
from unittest.mock import Base
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from shamenova import Article, Author, Category, Review
from shamenova2 import User, UserCreate, UserOut, UserUpdate

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

@app.post("/User", response_model=UserOut) 
def create_User(user: UserCreate, db: Session = Depends(get_db)):
    db_User = User(
        file_name=User.full_name,
        email=User.email
    )
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

@app.post("/User, response_model=CategoryOut")
def create_User(User: UserCreate, db: Session = Depends(get_db)):
    db_User = Category(**User.diet())
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

@app.post("/User", response_model=User)
def create_User(User: User, db: Session = Depends(get_db)):
    db_User = User(
        title=User.title,
        content=User.content,
        category_id=User.category_id
    )
    db_User.authors = db.query(Author).filter(Author.id. in_(User.author_ids)).all()
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

@app.post("/User", response_model=UserOut) # type: ignore
def create_User(User: UserCreate, db: Session = Depends(get_db)):
    db_User = User(
        title=User.title,
        content=User.content,
        category_id=User.category_id
    )
    authors = []
    for author_id in User.author_ids:
        author= db.query(Author).filter(Author.id == author_id).first()
        if author:
            authors.append(author)
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

@app.get("/User", response_model=List[User])
def list_User(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/User/{article_id}/User", response_mobel=User)
def add_review(article_id: int, review: UserCreate,db: Session = Depends(get_db)):
    db_article = db.query(User).get(article_id)
    if not db_article:
        raise HTTPException(status_code=484, detail="CTaTen we Haiigena")
    db_User = Review(**review.dict(), article_id=article_id)
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

@app.patch("/User{User_id}", response_model=UserOut)
def update_User(User_id: int,ubdate_data: UserUpdate,db: Session = Depends(get_db)):
    db_User = db.query(User).get(User_id)
    if not db_User:
        raise HTTPException(status_code=404, detail="статья не найдена")
    if ubdate_data.title is not None:
        db_User.title = ubdate_data.title
    if ubdate_data.content is not None:
        db_User. content = ubdate_data.content
    if ubdate_data.category_id is not None:
        db_User.category_id = ubdate_data.category_id
    if ubdate_data.author_ids is not None:
        db_User.authors = db.query(Author).filter(Author.id.in_(ubdate_data.author_ids)).all()

    db.commit()
    db.refresh(db_User)
    return db_User

@app.delete("/User{User_id}",response_model=dict)
def delete_User(User_id: int,db: Session = Depends(get_db)):
    db_User = db.query(User).get(User_id)
    if not db_User:
        raise HTTPException(status_code=484, detail="Отзыв не найден")
    db.delete(db_User)
    db. commit()
    return {"message": "Отзыв успешно удалён"}
