from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:myps@gardunov.duckdns.org:7504/augmentationdb")
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()