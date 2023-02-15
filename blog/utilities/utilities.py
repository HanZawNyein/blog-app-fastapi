from sqlalchemy.orm import Session
from blog.models.posts import Post
from blog.schemas.posts import CreatePost
from database.curd import Curd
from fastapi import Request
# curd = Curd(model=Post)


class Post(Post, Curd):
    _model = Post

    def create(self, request: Request, post: CreatePost):
        return super().create(request, post)


post = Post()
post.all = post.all
post.create = post.create
