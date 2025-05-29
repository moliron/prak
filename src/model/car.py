import os
import shutil
from typing import List, Optional
from uuid import uuid4
from wsgiref.types import StartResponse
from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from pydantic import BaseModel
from sqlalchemy.orm import Session
from bddata.shamenova3 import get_db
from bddata.shemanova9 import BodyType, Car, DriveType, EngineType, FuelType, InteriorType, TransmissionType, UserRole, require_role
from modols import User

router = APIRouter()

@router.get("/{id}", response_model=StartResponse)
def get_car(id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(car.id == id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Не найдено  ")
    return car


class ReferenceTypeResponse(BaseModel):
    id: int
    name: str

class Config:
    from_attributes = True

class ReferenceTypeCreate(BaseModel):
    name: str

class ReferenceTypeUpdate(BaseModel): 
    name: Optional[str] = None

# Схемы для каждой справочной таблицы

class BodyTypeResponse(ReferenceTypeResponse):
    pass

class FuelTypeResponse(ReferenceTypeResponse):
    pass

class DriveTypeResponse(ReferenceTypeResponse): 
    pass

class TransmissionTypeResponse(ReferenceTypeResponse): 
    pass

class InteriorTypeResponse (ReferenceTypeResponse):
    pass

class EngineTypeResponse(ReferenceTypeResponse):
    pass


class CarBase(BaseModel):
    name: str 
    year: int
    engine_id: int
    drive_id: int
    transmission_id: int 
    interior_id: int
    fuel_tank_capacity: float
    fuel_type_id: int
    cruise_control: bool
    body_type_id: int
    max_speed: int
    fuel_consumption: float 
    price: float

class CarCreate(CarBase):
    pass

class CarUpdate(BaseModel): 
    name: Optional [str] = None 
    year: Optional[int] = None 
    engine_id: Optional [int] = None 
    drive_id: Optional[int] = None 
    transmission_id: Optional[int] = None
    interior_id: Optional[int] = None 
    fuel_tank_capacity: Optional[float] = None 
    fuel_type_id: Optional[int] = None
    cruise_control: Optional [bool] = None
    body_type_id: Optional[int] = None
    max_speed: Optional[int] = None
    fuel_consumption: Optional [float] = None
    price: Optional [float] = None
    url_image: Optional[str] = None


class CarResponse(CarBase):
    id: int
    url_image: Optional[str] = None
    engine: EngineTypeResponse
    drive: DriveTypeResponse
    transmission: TransmissionTypeResponse
    interior: InteriorTypeResponse
    fuel_type: FuelTypeResponse
    body_type: BodyTypeResponse

class Config:
    from_attributes = True



@router.get("/", response_model = List[CarResponse]) 
def get_cars(
    db: Session = Depends(get_db),
    body_type_id: list[int] | None = Query(default=None),
    fuel_type_id: list[int] | None = Query(default=None),
    drive_id: list[int] | None = Query(default=None),
    transmission_id: list[int] | None = Query(default=None),
    interior_id: list[int] | None = Query(default=None),
    engine_id: list[int] | None = Query(default=None),
    cruise_control: list[int] | None = Query(default=None),
):
    query = db. query(Car)
    if body_type_id:
        query = query. filter(Car.drive_id.in_(body_type_id))
    if fuel_type_id:
        query = query. filter(Car.drive_id.in_(fuel_type_id))
    if drive_id:
        query = query. filter(Car.drive_id.in_(drive_id))
    if transmission_id:
        query = query. filter(Car.drive_id.in_(transmission_id))
    if interior_id:
        query = query. filter(Car.drive_id.in_(interior_id))
    if engine_id:
        query = query. filter(Car.drive_id.in_(engine_id))
    if cruise_control is not None:
        query = query. filter(Car.drive_id.in_(cruise_control))
    return query. all()

@router.post("/", Pesponse_model=CarResponse, status_code=261)
def create_car(
    car: CarCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN))
):
    if not db.query(EngineType).filter(EngineType.id == car.engine_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный engine_id")

    if not db.query(DriveType).filter(DriveType.id == car.drive_id).filter:
        raise HTTPException(status_code=400, detail="Henpaswnbuuit drive_id")

    if not db.query(TransmissionType).filter(TransmissionType.id == car.transmission_id).first():
        raise HTTPException(status_code=400, detail="HenpaswabHul transmission_id")

    if not db.query(InteriorType).filter(InteriorType.id == car.interior_id).first():
        raise HTTPException(status_code=400, detail="HenpaswabHul interior_id")

    if not db.query(FuelType) .Filter(FuelType.id == car. fuel_type_id).first():
        raise HTTPException(status_code=400, detail="HenpaswnbHult fuel_type_id")

    if not db.query(BodyType) .Filter(BodyType.id == car.body_type_id).first():
        raise HTTPException(status_code=400, detail="HenpaswnbHult body type_id")
    db_car = Car(**Car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

IMAGE_DIR = "static/images"
os.makedirs(IMAGE_DIR, exist_ok= True)
ALLOWED_EXTENSIONS = {".jpg","jpeg",".png",".gif"}
MAX_FILE_SIZE = 5 * 1024 * 1024

@router.post("/{id}/image", response_model=CarResponse)
async def upload_car_image(
    id: int,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN))
):
    db_car = db.query(Car).filter(Car.id == id).first()
    if not db_car:
        raise HTTPException(status_code=404, detai="")

    file_ext = os.path.splitext (image. filename) [1] .lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detai="")

    image.file.seek(0, os.SEEK_END)
    file_size = image. file.tell()
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detai="")
    image.file.seek(0)

    if db_car.url_image:
        old_file_path = db_car.url_image.replace("/static/", "static/")
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

    file_name = f"car_{db_car.id}_{uuid4()}{file_ext}"
    file_path = os.path.join(IMAGE_DIR, file_name)


    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db_car.url_image = f"/static/images/{file_name}"
    db.commit()
    db.refresh(db_car)
    return db_car

