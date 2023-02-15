from starlette.middleware.base import BaseHTTPMiddleware
from database.database import SessionLocal


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.db = SessionLocal()
        response = await call_next(request)
        return response
