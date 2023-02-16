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


class Post(CreatePost):
    id: int

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id":1,
                "title": "Fast Api",
                "description": """Hello"""
            }
        }
