from pydantic import BaseModel
   
class BlogSchema(BaseModel):
    title:str
    body:str
    published:bool
    articleName:str

class ListBlogSchema(BaseModel):
    blogId:str

class DeleteBlogSchema(BaseModel):
    blogId:str    


class UpdateBlogSchema(BaseModel):
    blogId:str
    title:str
    body:str
    published:bool
    articleName:str        