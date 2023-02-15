from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from config.ConfSettings import settings
from auth.utilities.utilities import user
from database.database import SessionLocal


class RequestUserMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.db = SessionLocal()
        request.state.user = self.get_user(request)
        response = await call_next(request)
        return response

    def get_user(self, request):
        token = request.headers.get('authorization')
        if token:
            token = token.split(' ')[1]
            try:
                payload = jwt.decode(token, settings.SECRET_KEY,
                                     algorithms=[settings.ALGORITHM])
                username: str = payload.get("sub")
                if username:
                    return user._get_user_by_username(request=request, username=username)
            except JWTError:
                pass
