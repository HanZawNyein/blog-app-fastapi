from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    full_name = Column(String)
    hashed_password = Column(String, unique=False)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
