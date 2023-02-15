from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST:str
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    TOKEN_URL:str

    class Config:
        env_file = ".env"


settings = Settings()
