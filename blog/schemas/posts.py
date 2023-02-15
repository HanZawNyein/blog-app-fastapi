from pydantic import BaseModel
from typing import Optional


class CreatePost(BaseModel):
    title: str
    description: Optional[str]


class Post(CreatePost):
    id: int

    class Config:
        orm_mode = True
