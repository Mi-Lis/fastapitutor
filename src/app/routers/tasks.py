from models.task import *
from typing import List

from fastapi import APIRouter, HTTPException

current_id = 1
tasks_router = APIRouter(prefix='/user/{user_id}/tasks')
tasks = {} # TODO: change to postgres

@tasks_router.get('/{task_id}')
async def get_task(task_id:int):
    if task_id in tasks:
        return tasks[task_id]
    raise HTTPException(status_code=404, detail="Задача не найдена")

@tasks_router.post("/{task_id}", response_model=Task)
def create_task(task_id:int, task:Task):
    if task_id in tasks:
        return
    global current_id
    new_task = Task(id=current_id, **task.model_dump(), completed=False)
    tasks.update({current_id:new_task})
    current_id += 1
    return new_task

@tasks_router.get("/", response_model=List[Task])
def read_tasks(limit:int=5):
    if limit<len(tasks):
        return tasks[:limit]
    raise HTTPException(status_code=404, detail="Задачи не найдены")

@tasks_router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task):
    tasks[task_id].title = updated_task.title
    tasks[task_id].description = updated_task.description
    return tasks[task_id]

@tasks_router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id in tasks:
        tasks.pop(task_id)
        return {"messege":"Delete Success"}
    raise HTTPException(status_code=404, detail="Задача не найдена")