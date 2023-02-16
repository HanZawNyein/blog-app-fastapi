from pydantic import BaseModel
from typing import Optional


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

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": 1,
                "title": "Fast Api",
                "description": """Hello""",
                "owner_id": 1
            }
        }
