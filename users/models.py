from database import Base
from sqlalchemy import Sequence,Column,String,Integer
from uuid import uuid4
from sqlalchemy import DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
class UserModel(Base):
    __tablename__='userTable'
    userId = Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid4,nullable=False)
    firstName=Column(String,nullable=False)
    lastName=Column(String,nullable=False)
    email=Column(String,nullable=False)
    phoneNo=Column(String,nullable=False)
    adharNo=Column(String,nullable=False)
    password=Column(String,nullable=False)
    
 




class RefreshTokens(Base):
    __tablename__="RefreshToken"
    TokenId=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid4,nullable=False)
    refreshToken=Column(String,nullable=False)
   