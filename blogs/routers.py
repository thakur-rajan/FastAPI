from fastapi import APIRouter,status,Depends,Response
from fastapi.responses import JSONResponse
from .schema import BlogSchema,ListBlogSchema,DeleteBlogSchema,UpdateBlogSchema
from database import get_db
from .api import createBlogApi,listBlogApi,deleteBlogApi,updateBlogApi
from sqlalchemy.orm import Session
blogRouter=APIRouter(
    prefix="/blog/v1",
    tags=['blogs']
)
@blogRouter.post('/create-blog/',status_code=status.HTTP_201_CREATED)

def createBlog(blogData:BlogSchema,response:Response,db:Session=Depends(get_db)):
    
    return createBlogApi(blogData,response,db)

@blogRouter.post('/get-blog/',status_code=status.HTTP_200_OK)

def listBlogRouter(blogData:ListBlogSchema,response:Response,db:Session=Depends(get_db)):

    return listBlogApi(blogData,response,db)

@blogRouter.delete('/delete-blog/',status_code=status.HTTP_204_NO_CONTENT)
def deleteBlogRouter(blogdata:DeleteBlogSchema,response:Response,db:Session=Depends(get_db)):
    
    return deleteBlogApi(blogdata,response,db)

@blogRouter.patch('/update-blog/',status_code=status.HTTP_201_CREATED)
def updateBlogRouter(blogData:UpdateBlogSchema,response:Response,db:Session=Depends(get_db)):
    
    return updateBlogApi(blogData,response,db)