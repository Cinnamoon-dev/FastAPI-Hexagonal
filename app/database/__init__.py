import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URI', None))
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