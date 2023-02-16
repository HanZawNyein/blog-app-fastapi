from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class User(BaseUser):
    is_active: bool | None = None
    is_superuser: bool | None = None


class UserSignUp(BaseUser):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "hanzawnyein",
                "email": "hanzawnyineonline@gmail.com",
                "full_name": "Han Zaw Nyein",
                "password": "****",
            }
        }


class UserInDB(User):
    hashed_password: str
