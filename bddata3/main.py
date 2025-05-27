from fastapi import FastAPI

from bddata3.model import car

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