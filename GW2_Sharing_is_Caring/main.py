from alembic.config import Config
from alembic import command
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from typing import Union
from sqlalchemy.orm import Session

from . import crud, models, schemas, database


# Dependency
def get_db():
    db = database.SessionFactory()
    try:
        yield db
    finally:
        db.close()


def run_alembic_migrations():
    # grab config from the ini and run the alembic upgrade command
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # run alembic migration before fastapi
    run_alembic_migrations()
    # run fast api
    yield
    # can specify commands after shut down


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.User, db_session: Session = Depends(get_db)):
    return crud.create_user(db=db_session, user=user)
