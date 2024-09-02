import os
from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI", None))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    def _get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    return next(_get_db())

db_dependency = Annotated[Session, Depends(get_db)]