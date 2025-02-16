
from datetime import datetime,timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from users.schema import TokenData
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
# from users.models import UserModel
# from sqlalchemy.orm import Session
# from database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bycrypt(password:str):
        return pwd_context.hash(password)
    def verify(plainPassword,hashedPassword):
        return pwd_context.verify(plainPassword,hashedPassword)
    
REFRESH_TOKEN_SECRET="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"   
SECRET_KEY = "09d25e094fa9563b93f709"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/u1/login")

def createAccessToken(data: dict, expires_delta: timedelta = None):
    payload = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    payload.update({"exp": expire})
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# def createRefreshToken(data:dict, expires_delta: timedelta = None):
#     payload = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     payload.update({"exp": expire})
#     refreshToken = jwt.encode(payload,REFRESH_TOKEN_SECRET, algorithm=ALGORITHM)
#     return refreshToken   

# def verifyToken(token,credentialException,refreshToken=False):
#     '''
#     '''
#     try:
#         if not refreshToken:
#             payload = jwt.decode(token,SECRET_KEY, algorithms=ALGORITHM) 
#         else:
#             payload = jwt.decode(token,REFRESH_TOKEN_SECRET, algorithms=ALGORITHM)
#         userId : str = payload.get('sub')
#         if not userId:
#            return payload.get('sub') 
#     except Exception as e:
#         return str(e)
# def getCurrentUser(data:str=Depends(oauth2_scheme),refreshToken=False):
#     '''
#     '''
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Not Authenticated",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     if not refreshToken:
#         return verifyToken(data,credentials_exception)
#     else:
#         return verifyToken(data,credentials_exception,refreshToken=True)









 
def verifyToken(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userId: str = payload.get("sub")
        if not userId :
            raise credentials_exception
        token_data = TokenData(userId=userId)
    except JWTError:
        raise credentials_exception


def getCurrentUser(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verifyToken(token,credentials_exception)















#     user = db.query(UserModel).filter(UserModel.userId == token_data.userId).first()
#     if user is None:
#         raise credentials_exception
#     return user    
