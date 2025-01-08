import os
from sqlmodel import Session, create_engine, SQLModel
from fastapi import Depends, FastAPI
from typing import Annotated

sqlite_name= "db.sqlite3"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")  # Valor por defecto: SQLite

engine = create_engine(DATABASE_URL)

def create_all_Tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]