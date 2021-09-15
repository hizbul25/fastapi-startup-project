#!/usr/bin/python3

from fastapi import FastAPI
from core import auth, blog, user
from database.configuration import engine
from models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Startup Project",
    description="API with high performance built with FastAPI & SQLAlchemy, help to improve connection with your Backend Side.",
    version="1.0.0",
)

app.include_router(auth.router, prefix='/login', tags=['Authentication'])
app.include_router(blog.router, prefix='/blogs', tags=['Blog'])
app.include_router(user.router, prefix='/users', tags=['User'])
