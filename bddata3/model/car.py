from wsgiref.types import StartResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bddata.shamenova3 import get_db
from bddata.shemanova9 import Car

router = APIRouter()

@router.get("/{id}", response_model=StartResponse)
def get_car(id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(car.id == id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Не найдено  ")
    return car