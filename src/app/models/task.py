from . import *

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
