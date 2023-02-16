from sqlalchemy.orm import Session
from blog.models.posts import Post
from blog.schemas.posts import CreatePost, PostInDb
from database.curd import Curd
from fastapi import Request
# curd = Curd(model=Post)


class Post(Curd):
    _model = Post

    def create(self, request: Request, post: CreatePost):
        post = PostInDb(**post.dict(), owner_id=request.state.user.id)
        return super().create(request, post)


post = Post()
post.all = post.all
post.create = post.create
