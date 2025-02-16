from uuid import uuid4
from sqlalchemy import Column, String,Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from  users.models import UserModel

# Base class for model definitions
Base = declarative_base()

class BlogModel(Base):
    __tablename__ = 'blogTable'
    
    blogId = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    articleName = Column(String, nullable=False)
    published = Column(Boolean, nullable=True)
    
