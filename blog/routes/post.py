from fastapi import APIRouter, Request
from ..schemas.posts import CreatePost, Post
from ..utilities.utilities import post as POST


from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta
# from auth.utilities.utilities import user as USER
from auth.schemas.token import Token
from auth.utilities.oauth2 import authenticate_user, create_access_token,get_current_active_user
from config.ConfSettings import settings

router = APIRouter()


@router.get("/", response_model=list[Post])
def read_items(request: Request, skip: int = 0, limit: int = 100):
    items = POST.all(request=request, skip=skip, limit=limit)
    return items


@router.post("/", response_model=Post)
def create_item_for_user(request: Request, post: CreatePost):
    return POST.create(request=request, post=post)



# @router.post("/token", response_model=Token)
# async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(request, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}