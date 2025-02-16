from .schema import createUserSchema,listUserSchema,LoginUserSchema,UpdateUserSchema,DeleteUserSchema
from .models import UserModel
from datetime import timedelta
from fastapi import Response,Depends,status
from sqlalchemy.orm import Session
from database import get_db
from auth import createAccessToken,ACCESS_TOKEN_EXPIRE_MINUTES
from .helperfunction import validateUserData,validateListData,validateDeleteData,validateUserExistence,validateUpdateData,validateLoginData
def createUserApi(userData:createUserSchema,response:Response,db:Session):
    try:
        logData=userData.dict()
        validation = validateUserData(logData, db)
        if not validation.get('status'):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                'status': False,
                'message': validation.get('message'),
                'code': validation.get('code')
            }
        validateData=validation.get('data')
        new_user = UserModel(**validateData)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            'status':True,
            'Message':"User Created successful",
            'code':"CREATED-20000"
        }

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {    
            'status': False,
            'message': f"Internal server error: {str(e)}"
        }
    
def listUserApi(userData:listUserSchema,response:Response,db:Session):
    try:
      listData=userData.dict()
      validation=validateListData(listData,db)
      if not validation.get('status'):
          response.status_code = status.HTTP_400_BAD_REQUEST
          return {
          'status': False,
          'message': validation.get('message'),
          'code': validation.get('code')
              }
      lis=[]
      userId=validation.get('userId')
      if userId:
          userDetail=db.query(UserModel).filter(UserModel.userId==userId).all()
      else:   
          userDetail=db.query(UserModel).all()
      for user in userDetail:
          dic={}
          dic['userId']=user.userId
          dic['firstName']=user.firstName
          dic['lastName']=user.lastName
          dic['email']=user.email
          dic['phoneNo']=user.phoneNo
          dic['adhaarNo']=user.adharNo
          dic['password']=user.password
          lis.append(dic) 
      return {
          'status':True,
          'message':'Data found successfully',
          'code':'USERDETAIL-20001',
          'data':lis
      }  
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {    
            'status': False,
            'message': f"Internal server error: {str(e)}"
        }
        
def updateUserApi(userData:UpdateUserSchema,response:Response,db:Session=Depends(get_db)):
    try:
        updateData=userData.dict()
        validation=validateUpdateData(updateData,db)
        if not validation.get('status'):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return{
                'status':False,
                'message':validation.get('message'),
                'code':validation.get('code')
            }
        userId=validation.get('userId') 
        user=db.query(UserModel).filter(UserModel.userId==userId).first()
        if not user:
            return{
                'status':False,
                'message':'User not found',
                'code':'USERUPDATE-30000'
            }
        for key,value in validation.get('data'):
              setattr(user, key, value) 
        db.commit()
        db.refresh(user)         
        return {
            'status': True,
            'message': 'User updated successfully',
            'code': 'UPDATED-20002'
        }           
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            'status': False,
            'message': f"Internal server error: {str(e)}"
        }



def deleteUserApi(userData:DeleteUserSchema,response:Response,db:Session):
    try:
        deleteData=userData.dict()
        validation=validateDeleteData(deleteData,db)
           
        if not validation.get('status'):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return{
                'status':False,
                'message':validation.get('message'),
                'code':validation.get('code')
            }
        # print("000000000000000000000000000000000")    
        userId=validation.get('userId') 
        if userId:
            userDetail=db.query(UserModel).filter(UserModel.userId==userId).first()
            db.delete(userDetail)
            db.commit()
            return{
            'status':True,
            'message':'Deleted successful',
            'code':'DELETE-20003'
            }
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {    
            'status': False,
            'message': f"Internal server error: {str(e)}"
        } 
        

def updateUserApi(userData: UpdateUserSchema, response: Response, db: Session):
    try:
        updateData = userData.dict()
        
        
        validation = validateUpdateData(updateData, db)
        if not validation.get('status'):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                'status': False,
                'message': validation.get('message'),
                'code': validation.get('code')
            }

     
        userId = updateData.get('userId')
        userValidation = validateUserExistence(userId, db)
        if not userValidation.get('status'):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                'status': False,
                'message': userValidation.get('message'),
                'code': userValidation.get('code')
            }

        user = userValidation.get('user')
        
        for key, value in validation.get('data').items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)

        return {
            'status': True,
            'message': 'User updated successfully',
            'code': 'UPDATED-20003'
        }

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            'status': False,
            'message': f"Internal server error: {str(e)}"
        }
def loginApi(userData:LoginUserSchema,response:Response,db:Session):
     try:
        loginData=userData.dict()
        validation=validateLoginData(loginData,db)
        # print("RRRRRRRRRRRRRRrrrrrrrrrrrrrrrrr")
        if not validation.get('status'):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return{
                'status':False,
                'message':validation.get('message'),
                'code':validation.get('code')
            }
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = createAccessToken(
                      data={"sub": validation.get('userId')}, expires_delta=access_token_expires)
        return {'access_token':access_token, 
                'token_type':"bearer"}
     except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            'status': False,
            'message': f" {str(e)}"
        }          
# def getAccessTokenFromRefreshTokenApi(request:GetAccessTokenSchema,response:Response,db:Session):
    
#     data=request.dict()
    
#     if not data.get('refreshToken') or str(data.get('refreshToken')).isspace():
#         return{
#             'status':False,
#             'message':'somrthing went wrong',
#             'code':'REFRESHTOKEN-40000'
#         } 
#     refreshToken=data.get('refreshToken')
#     result=getCurrentUser(refreshToken,refreshToken=True)
#     accessToken=createAccessToken({'sub':result},ACCESS_TOKEN_EXPIRE_MINUTES)
#     return{
#         'status':True,
#         'message':'Access token granted',
#         'accessToken':accessToken
#     }    


# def logoutApi(logout:GetAccessTokenSchema,response:Response,db:Session):
#     data=logout.dict()
#     if not data.get('refreshToken') or str(data.get('refreshToken')).isspace() or len(str(data.get('refreshToken')).strip())==0:
#         return{
#             'status':False,
#             'message':'Refresh Token reqiuered',
#             'code':'REFRESHTOKEN-400001'
#         }
#     try:   
#        refreshToken=db.query(RefreshTokens).filter(RefreshTokens.refreshToken==str(data.get('refreshToken')).strip())    
#     except Exception as error:
#         return {
#             'status':False,
#             'message':f'{str(error)}',
#             'code':'EXCEPTION-400002'
#         }
#     if not refreshToken.first():
#         response.status_code = status.HTTP_400_BAD_REQUEST
#         return {
#             "status" : False,
#             'message' :'Logout Failed',
#             "code" : 'LOGOUT-400003'
#         }  
#     try:
#         refreshToken.delete(synchronize_session=False)
#         db.commit()
#     except Exception as errors:
#         return {
#                 "status" : False,
#                 "message" : str(errors),
#                 "code" :'REFRESHTOKEN-40004'
#             } 
#     return{
#         'status':True,
#         'message':'Logout successfull'
#     }         
             























# def updateUserApi(userData: UpdateUserSchema, response: Response, db: Session):
#     try:
#         updateData = userData.dict()
        
#         # Validate the update data
#         validation = validateUserData(updateData, db)
#         if not validation.get('status'):
#             response.status_code = status.HTTP_400_BAD_REQUEST
#             return {
#                 'status': False,
#                 'message': validation.get('message'),
#                 'code': validation.get('code')
#             }
        
#         # Get the user ID to perform the update
#         userId = updateData.get('userId')
#         user = db.query(UserModel).filter(UserModel.userId == userId).first()

#         # Check if user exists
#         if not user:
#             response.status_code = status.HTTP_404_NOT_FOUND
#             return {
#                 'status': False,
#                 'message': 'User not found',
#                 'code': 'USERNOTFOUND-400020'
#             }
        
#         # Update user details
#         for key, value in validation.get('data').items():
#             setattr(user, key, value)

#         # Commit changes to the database
#         db.commit()
#         db.refresh(user)

#         return {
#             'status': True,
#             'message': 'User updated successfully',
#             'code': 'UPDATED-20003'
#         }

#     except Exception as e:
#         response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#         return {
#             'status': False,
#             'message': f"Internal server error: {str(e)}"
#         }      
           
# def login_user_api(login: LoginUserSchema, response: Response, db: Session):
#     logData = login.dict()
#     user = db.query(UserModel).filter(UserModel.userId == logData['userId']).first()
#     if not user:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {
#             'status': False,
#             'message': 'User not found',
#             'code': 'USER_NOT_FOUND'
#         }
#     if not Hash.verify(logData['password'], user.password):
#         response.status_code = status.HTTP_401_UNAUTHORIZED
#         return {
#             'status': False,
#             'message': 'Incorrect password',
#             'code': 'INCORRECT_PASSWORD'
#         }
#     access_token = create_access_token(data={"sub": str(user.userId)})
#     return {
#         'status': True,
#         'message': 'Login successful',
#         'code': 'LOGIN_SUCCESS',
#         'access_token': access_token,
#         'token_type': 'bearer'
    # }

# def loginUserApi(login:LoginUserSchema,response:Response,db:Session):
#            logData=login.dict()
#            validation=validateLoginData(logData,db)
#            if not validation.get('status'):
#                response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
#                return{
#                    'status':False,
#                    'message':validation.get('message'),
#                    'code':validation.get('code')
#                }
#            userData=validation.get('Data')
#            userId=validation.get('userId')
#            acessToken=createAccessToken({'sub':str(userId)},15)
#            return acessToken
                
# def userUpdateApi(userData:UpdateUserSchema,response:Response,db:Session):
#     try:
#         logData=userData.dict()
#         validation=validateUpdateData(logData,db)
#         if not validation.get('status'):
#             response.status_code=status.HTTP_400_BAD_REQUEST
#             return{
#                 'status':False,
#                 'message':validation.get('message'),
#                 'code':validation.get('code')
#             }
        
#         validateData=validation.get('data')
#         # userId=validation.get('userId')
#         user = db.query(UserModel).filter(UserModel.userId ==validation.get('userId')).first()
#         if user:
#             print("================================================")
#             for key, value in validateData.items():
#                 setattr(user, key, value)
#             db.commit()
#             db.refresh(user)
#         # user=db.query(UserModel).filter(UserModel.userId==userId).first()
#         # if UserModel.userId==userId:
#         #     user=UserModel(**validateData) 
#         #     # db.add(user)
#         #     user.firstName=validateData['firstName']
#         #     user.lastName=validateData['lastName']
#         #     user.email=validateData['email']
#         #     user.phoneNo=validateData['phoneNo']
#         #     user.adharNo=validateData.get('adharNo')
#         #     db.commit()
#         #     db.refresh(user)
#             return{
#             'status':True,
#             'message':'User Updated successfully',
#             'code':'UPDATED-20003'
#         }
                                     
#     except Exception as error:
#         return{
#             'status':False,
#             'message':f"Internal server error or {str(error)}",
#             'code':'UPDATEAPI-20004'
#         }      







# def loginUserApi(userData:LoginUserSchema,response:Response,db:Session):
#     try:
#         logData=userData.dict()
#         validation=validateLoginData(logData,db)
#         if not validation.get('status'):
#             response.status_code=status.HTTP_400_BAD_REQUEST
#             return{
#                 'status':validation.get('status'),
#                 'message':validation.get('message'),
#                 'code':validation.get('code')
#             }
            
    
    
