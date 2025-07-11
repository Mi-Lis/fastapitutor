from . import *

class User(BaseModel):
    id: int
    f: str
    i: str
    o: str
    email:str
    is_active:bool
    password:str