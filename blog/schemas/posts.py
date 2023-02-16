from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CreatePost(BaseModel):
    title: str
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Fast Api",
                "description": """Hello"""
            }
        }


class PostInDb(CreatePost):
    owner_id: int


class Post(PostInDb):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": 1,
                "title": "Fast Api",
                "description": """Hello""",
                "owner_id": 1,
                "create_date":"2023-02-16T13:49:55.005386"
            }
        }
