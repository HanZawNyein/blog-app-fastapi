from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        schema_extra = {
            "example": {
                "access_token": "lsdjgksafpowueirvkkvnskanvksd",
                "token_type": "bearer"
            }
        }


class TokenData(BaseModel):
    username: str | None = None
