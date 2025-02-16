from .schema import BlogSchema,ListBlogSchema,DeleteBlogSchema,UpdateBlogSchema
# from .routers import createBlog,getBlog
from .models import BlogModel
from fastapi import Response,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from .helperfunction import validateBlogData,validateListData,validateDeleteData,validateBlogExistance,validateUpdateData

def createBlogApi(blogData:BlogSchema,response:Response,db:Session=Depends(get_db)):
    try:
        userData=blogData.dict()
        validation = validateBlogData(userData, db)
        if not validation.get('status'):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                'status': False,
                'message': validation.get('message'),
                'code': validation.get('code')
            }
        validateData=validation.get('data')
        new_blog = BlogModel(**validateData)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)

        return {
            'status':True,
            'Message':"Blog Created successful",
            'code':"CREATED-20000"
        }

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {    
            'status': False,
            'message': f"Internal server error: {str(e)}"
        }
    
    return True
def listBlogApi(blogdata:ListBlogSchema,response:Response,db:Session):
    
    try:
       userData=blogdata.dict()
    #    print("999999999999999999999999")       
       validation=validateListData(userData,db)
       if not validation.get('status'):
           response.status_code=status.HTTP_400_BAD_REQUEST
           return{
               'status':False,
               'message':validation.get('message'),
               'code':validation.get('code')
            }
       lis=[]
       logId=validation.get('blogId')
       if logId:
           blogDetail=db.query(BlogModel).filter(BlogModel.blogId==logId).all()
       else:
           blogDetail=db.query(BlogModel).all()        
       for data in blogDetail:
           dic={}
           dic['blogId']=data.blogId
           dic['articleName']=data.articleName
           dic['title']=data.title
           dic['body']=data.body
           dic['published']=data.published
           lis.append(dic)
       return {
             'status':True,
             'message':'Data found successfully',
             'code':'USERDETAIL-20001',
             'data':lis
        }  
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {    
            'status': False,
            'message': f"Internal server error: {str(error)}"
            
        }
           

def deleteBlogApi(blogData:DeleteBlogSchema,response:Response,db:Session):
    try: 
        userData=blogData.dict()
        validation=validateDeleteData(userData,db)
        if not validation.get('status'):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return{
                'status':False,
                'message':validation.get('message'),
                'code':validation.get('code')
            }
        blogId=validation.get('blogId')
        if blogId:
            blogDetail=db.query(BlogModel).filter(BlogModel.blogId==blogId).first()
            db.delete(blogDetail)
            db.commit()
            return{
                'status':True,
                'message':'Deleted successfully',
                'code':'DELETEBLOGID-20002'
            }    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {    
            'status': False,
            'message': f"Internal server error: {str(e)}"
        }                

def updateBlogApi(blogData:UpdateBlogSchema,response:Response,db:Session):
    try:
        userData=blogData.dict()
        validation=validateUpdateData(userData,db)
        if not validation.get('status'):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return{
                'status':False,
                'message':validation.get('message'),
                'code':validation.get('code')
            }
        blogId=userData.get('blogId')
        userValidation=validateBlogExistance(blogId,db)
        if not userValidation.get('status'):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return{
                'status':False,
                'message':userValidation.get('message'),
                'code':userValidation.get('code')
            }
        blog=userValidation.get('blog')
        for key,value in validation.get('data').items():
            setattr(blog,key,value)  
        db.commit()
        db.refresh(blog)
        return{
            'status':True,
            'message':'Updated sucessfully',
            'code':'UPDATE-20003'
        }    
            
    except Exception as error:
        response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        return{
            'status':False,
            'message':f'{str(error)}',
            'code':'EXCEPTION-300000'
        }
                
            















