from fastapi import APIRouter, HTTPException
from models.user import User

user_router = APIRouter(prefix='/user')
users = {} # TODO: change to postgres

@user_router.get('/{user_id}')
async def get_user(user_id:int):
    if user_id in users:
        return users[user_id]
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@user_router.post("/",  response_model=User)
async def create_user(user:User):
    global current_id
    new_user = User(id=current_id, **user.model_dump(), completed=False)
    users.update({current_id:new_user})
    current_id += 1
    return new_user

@user_router.get("/")
async def show_user():
    return {"":""}

@user_router.delete("/{user_id}")
async def delete_user(user_id):
    if user_id in users:
        users.pop(user_id)
        return {"message":"Пользователь удален"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")