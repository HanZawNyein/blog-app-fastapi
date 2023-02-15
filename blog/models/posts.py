from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


from database.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
