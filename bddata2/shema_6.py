from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from datetime import datetime

from shema_5 import TaskCreate, TaskFull, TaskShort

app = FastAPI()

tasks_db = []

@app.post("/tasks", response_model=TaskShort)
def create_task(task: TaskCreate):
    task_full = TaskFull(
        id=uuid4() ,
        is_completed=False,
        created_at=datetime.now(),
        updated_at=None,
        title=task.title,
        description=task.description,
        priority=task.priority,
        deadline=task.deadline
    )

    tasks_db.append(task_full)
    return TaskShort(**task_full.diet())

@app.get ("/tasks", response_model=list [TaskShort])
def list_tasks():
    return [TaskShort(**task) for task in tasks_db]

@app.get ("/tasks/(task_id)", response_model=TaskFull)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return TaskFull(**task)
    raise HTTPException(status_code=404, detail="задача не найдена")