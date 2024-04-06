from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional 
from router import user
from db import models
from db.database import engine


app = FastAPI()
app.include_router(user.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

models.Base.metadata.create_all(engine)