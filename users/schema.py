from pydantic import BaseModel,Field
from typing import Optional
   
class createUserSchema(BaseModel):
    firstName:str
    lastName:str
    email:str
    password:str
    phoneNo:str
    adharNo:str


class listUserSchema(BaseModel):
    userId:str
        
class DeleteUserSchema(BaseModel):
    userId:str


class UpdateUserSchema(BaseModel):
    userId:str
    firstName:str
    lastName:str
    email:str
    password:str
    phoneNo:str
    adharNo:str
        
        


class LoginUserSchema(BaseModel):
    userId:str
    password:str
    
    
    
class User(BaseModel):
    firstName:str
    email:str
    password:str  


  
# class GetAccessTokenSchema(BaseModel):
    
#     refreshToken:Optional[str]=Field(None,nullable=True)        
 


# class Token(BaseModel):
#     access_token: str
#     token_type: str


class TokenData(BaseModel):
    userId: str | None = None










    
    
    
    