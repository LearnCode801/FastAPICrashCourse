from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALACHEMY_DATABASE_URL ='postgresql://postgres:1234@localhost/fastapi'
# SQLALACHEMY_DATABASE_URL =f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engin=create_engine(SQLALACHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base=declarative_base()


def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()