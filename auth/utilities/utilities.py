from database.curd import Curd
from fastapi import Request, HTTPException, status

from auth.schemas.user import UserInDB, BaseUser, User as SchemasUser
from auth.models.user import User


class User(Curd):
    _model = User

    def ___response(self, user=None) -> BaseUser:
        if user:
            return SchemasUser(username=user.username,
                               email=user.email,
                               full_name=user.full_name,
                               is_active=user.is_active,
                               is_superuser=user.is_superuser
                               )

    def create(self, request: Request, user: UserInDB):
        if self.get_user_by_email(request, email=user.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email is already Registered."
            )
        if self.get_user_by_username(request, username=user.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username is already Registered."
            )
        user = super().create(request, user)
        return self.___response(user=user)

    def get_user_by_email(self, request: Request, email: str):
        return self.___response(user=request.state.db.query(self._model).filter(self._model.email == email).first())

    def get_user_by_username(self, request: Request, username: str):
        return self.___response(request.state.db.query(self._model).filter(self._model.username == username).first())

    def _get_user_by_username(self, request: Request, username: str):
        return request.state.db.query(self._model).filter(self._model.username == username).first()

    def get_user_by_id(self, request: Request, id: int):
        user = super().get_user_by_id(request, id)
        return self.___response(user)

    def all(self, request: Request, skip: int = 0, limit: int = 100):
        return [self.___response(user) for user in super().all(request, skip=skip, limit=limit)]


user = User()
