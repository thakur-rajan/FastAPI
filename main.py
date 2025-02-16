from fastapi import FastAPI,Depends
from database import engine
from sqlalchemy.orm import Session
from blogs.routers import blogRouter
from blogs.models import BlogModel
from users.routers import userRouter
from users.models import UserModel


app=FastAPI()

# models.Base.metadata.create_all(engine)
app.include_router(userRouter)
app.include_router(blogRouter)
UserModel.metadata.create_all(bind=engine)
BlogModel.metadata.create_all(bind=engine)
