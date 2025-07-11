from pydantic import BaseModel

class TaskUser(BaseModel):
    user_id:int
    task_id:int