from fastapi import Depends, FastAPI
from bddata.shamenova3 import get_db
from bddata.shemanova9 import BodyType, DriveType, EngineType, FuelType, InteriorType, TransmissionType
import router
from src.model import car
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

app = FastAPI(
    title ="название",
    description="API",
    version="1.0.0"
)

tasks = []

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return{"message":"задача добавлена"}

@app.put("/")
def ubdata_item(old:str, new:str):
    if old in tasks:
        index = tasks.index(old)
        tasks[index] = new
        return {"message": "обновлено", "item": new}
    
@app.delete("/")
def delete_item(item: str):
    if item in tasks:
        tasks.remove(item)
        return {"message": "удалено",
                "item":""}
    
app.include_router(car.router, prefix="/cars", tags=["cars"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/filter-options/")
def get_filter_options(db: Session = Depends(get_db)):
    return {
        "body_types": db.query(BodyType).all(),
        "fuel_types": db.query(FuelType).all(),
        "drive_types": db.query(DriveType).all(),
        "transmission_types": db.query(TransmissionType).all(),
        "interior_types": db.query(InteriorType).all(),
        "engine_types": db.query(EngineType).all(),
    }