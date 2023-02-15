from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from datetime import timedelta
from auth.schemas.user import UserSignUp, BaseUser, UserInDB
from auth.utilities.utilities import user as USER
from auth.models.user import User
from auth.schemas.token import Token
from auth.utilities.oauth2 import authenticate_user, create_access_token
from config.ConfSettings import settings
from auth.utilities.oauth2 import get_password_hash, get_current_active_user


router = APIRouter()


    
@router.get("/all", response_model=list[BaseUser], deprecated=True)
async def get_all_users(request: Request):
    return USER.all(request=request)


@router.post("/signup", response_model=BaseUser)
async def signup(request: Request, user: UserSignUp) -> BaseUser:
    user = UserInDB(**user.dict(), is_active=True,
                    hashed_password=get_password_hash(user.password))
    return USER.create(user=user, request=request)


@router.get("/me", response_model=BaseUser)
async def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/{user_id}", response_model=BaseUser)
async def get_user(request: Request, user_id: int,current_user: User = Depends(get_current_active_user)) -> BaseUser:
    user = USER.get_user_by_id(request, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Users doesn't exist."
        )
    return user
