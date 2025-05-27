import email
from fileinput import filename
from typing import List
from unittest.mock import Base
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from shamenova import Article, Author, Category, Review
from shamenova2 import lease, leaseCreate, leaseOut, leaseUpdate

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

@app.post("/lease", response_model=leaseOut) 
def create_lease(lease: leaseCreate, db: Session = Depends(get_db)):
    db_lease = lease(
        file_name=lease.full_name,
        email=lease.email
    )
    db.add(db_lease)
    db.commit()
    db.refresh(db_lease)
    return db_lease

@app.post("/lease, response_model=CategoryOut")
def create_Cards(lease: leaseCreate, db: Session = Depends(get_db)):
    db_lease = Category(**lease.diet())
    db.add(db_lease)
    db.commit()
    db.refresh(db_lease)
    return db_lease

@app.post("/lease", response_model=lease)
def create_lease(lease: lease, db: Session = Depends(get_db)):
    db_lease = lease(
        title=lease.title,
        content=lease.content,
        category_id=lease.category_id
    )
    db_lease.authors = db.query(Author).filter(Author.id. in_(lease.author_ids)).all()
    db.add(db_lease)
    db.commit()
    db.refresh(db_lease)
    return db_lease

@app.post("/lease", response_model=leaseOut) # type: ignore
def create_lease(lease: leaseCreate, db: Session = Depends(get_db)):
    db_lease = lease(
        title=lease.title,
        content=lease.content,
        category_id=lease.category_id
    )
    authors = []
    for author_id in lease.author_ids:
        author= db.query(Author).filter(Author.id == author_id).first()
        if author:
            authors.append(author)
    db.add(db_lease)
    db.commit()
    db.refresh(db_lease)
    return db_lease

@app.get("/lease", response_model=List[lease])
def list_lease(db: Session = Depends(get_db)):
    return db.query(lease).all()

@app.post("/lease/{article_id}/lease", response_mobel=lease)
def add_review(article_id: int, review: leaseCreate,db: Session = Depends(get_db)):
    db_article = db.query(lease).get(article_id)
    if not db_article:
        raise HTTPException(status_code=484, detail="CTaTen we Haiigena")
    db_lease = Review(**review.dict(), article_id=article_id)
    db.add(db_lease)
    db.commit()
    db.refresh(db_lease)
    return db_lease

@app.patch("/lease{User_id}", response_model=leaseOut)
def update_lease(User_id: int,ubdate_data: leaseUpdate,db: Session = Depends(get_db)):
    db_lease = db.query(lease).get(User_id)
    if not db_lease:
        raise HTTPException(status_code=404, detail="статья не найдена")
    if ubdate_data.title is not None:
        db_lease.title = ubdate_data.title
    if ubdate_data.content is not None:
        db_lease. content = ubdate_data.content
    if ubdate_data.category_id is not None:
        db_lease.category_id = ubdate_data.category_id
    if ubdate_data.author_ids is not None:
        db_lease.authors = db.query(Author).filter(Author.id.in_(ubdate_data.author_ids)).all()

    db.commit()
    db.refresh(db_lease)
    return db_lease

@app.delete("/lease{lease_id}",response_model=dict)
def deletelease(lease_id: int,db: Session = Depends(get_db)):
    db_lease = db.query(lease).get(lease_id)
    if not db_lease:
        raise HTTPException(status_code=484, detail="Отзыв не найден")
    db.delete(db_lease)
    db.commit()
    return {"message": "Отзыв успешно удалён"}
