from alembic.config import Config
from alembic import command
from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import Union

def run_alembic_migrations():
    #grab config from the ini and run the alembic upgrade command
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

@asynccontextmanager
async def lifespan(app: FastAPI):
    #run alembic migration before fastapi
    run_alembic_migrations()
    #run fast api
    yield
    #can specify commands after shut down

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}