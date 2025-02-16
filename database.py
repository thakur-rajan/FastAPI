from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE_URL= "postgresql://user_blog_manager:user_blog_manager@localhost:5432/user_blog_manager"
engine = create_engine(SQLALCHAMY_DATABASE_URL)
Session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()
def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close_all()