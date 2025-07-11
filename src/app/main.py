from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
# from app.models import Task, TaskCreate
from routers import *


app = FastAPI()

for router in routers:

    app.include_router(router)
