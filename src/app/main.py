from fastapi import FastAPI, HTTPException
from app.models import Task, TaskCreate
from typing import List

app = FastAPI()

# Временное хранилище задач в памяти
tasks = []
current_id = 1

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в To-Do API!"}

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global current_id
    new_task = Task(id=current_id, **task.dict(), completed=False)
    tasks.append(new_task)
    current_id += 1
    return new_task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks:
        if task.id == task_id:
            task.title = updated_task.title
            task.description = updated_task.description
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(idx)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")