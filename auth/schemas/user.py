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


class UserInDB(User):
    hashed_password: str
