from fastapi import APIRouter, Request
from ..schemas.posts import CreatePost, Post
from ..utilities.utilities import post as POST

router = APIRouter()


@router.get("/", response_model=list[Post])
def read_items(request: Request, skip: int = 0, limit: int = 100):
    items = POST.all(request=request, skip=skip, limit=limit)
    return items


@router.post("/", response_model=Post)
def create_item_for_user(request: Request, post: CreatePost):
    return POST.create(request=request, post=post)
