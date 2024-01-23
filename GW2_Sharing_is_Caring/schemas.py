# Pydantic Models go here

from pydantic import BaseModel


class User(BaseModel):
    id: int
    api_key: str
    user_name: str

    class Config:
        orm_mode = True
