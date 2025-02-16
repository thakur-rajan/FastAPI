from fastapi import APIRouter,status,Depends,Response
# from fastapi.responses import JSONResponse
from .schema import createUserSchema,listUserSchema,UpdateUserSchema,LoginUserSchema,User
from database import get_db
# from .models import UserModel
from auth import getCurrentUser
from .api import createUserApi,listUserApi,deleteUserApi,updateUserApi,loginApi
# ,getAccessTokenFromRefreshTokenApi,logoutApi

from sqlalchemy.orm import Session
userRouter=APIRouter(
    prefix="/user/u1",
    tags=['users']
)
@userRouter.post('/login',status_code=status.HTTP_201_CREATED)
def loginRouter(userData:LoginUserSchema,response:Response,db:Session=Depends(get_db)):
    
    return loginApi(userData,response,db)


# @userRouter.post('/refresh',status_code=status.HTTP_200_OK)
# def getAccessTokenFromRefreshToken(request:GetAccessTokenSchema,response:Response,db:Session=Depends(get_db)):
    
#     return getAccessTokenFromRefreshTokenApi(request,response,db)



# @userRouter.post('/logout',status_code=status.HTTP_200_OK)
# def logoutRouter(logoutData:GetAccessTokenSchema,response:Response,db:Session=Depends(get_db)):
    
#     return logoutApi(logoutData,response,db)

@userRouter.post('/create-user',status_code=status.HTTP_201_CREATED)
def createUserRouter(userData:createUserSchema,response:Response,db:Session=Depends(get_db)):
    
    
    return  createUserApi(userData,response,db)
@userRouter.post('/list-user',status_code=status.HTTP_200_OK)
def listUserRouter(userData:listUserSchema,response:Response,db:Session=Depends(get_db)):
    
    return listUserApi(userData,response,db) 


@userRouter.delete('/delete-user',status_code=status.HTTP_204_NO_CONTENT)
def deleteUserRouter(userData:listUserSchema,response:Response,db:Session=Depends(get_db)):
    
    return deleteUserApi(userData,response,db)

@userRouter.patch('/update',status_code=status.HTTP_201_CREATED)
def updateUserRouter(userData:UpdateUserSchema,response:Response,db:Session=Depends(get_db)):
    
    
    return updateUserApi(userData,response,db)







# @userRouter.post('/show-user/',status_code=status.HTTP_200_OK,tags=['user'])
# def showUserRouter(userData:ShowUserSchema,response:Response,db:Session=Depends(get_db)):
    
#     return showUserApi(userData,response,db)


# @userRouter.get('/protected/', status_code=status.HTTP_200_OK)
# def protected_route(current_user: UserModel = Depends(get_current_user)):
#     return {
#         'status': True,
#         'message': 'You are authenticated',
#         'user': current_user.firstName
#     }