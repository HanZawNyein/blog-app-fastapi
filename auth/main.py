from fastapi import FastAPI
from database.middleware import CustomHeaderMiddleware
from .routes import auth

app = FastAPI()

# middleware
app.add_middleware(CustomHeaderMiddleware)
app.include_router(auth.router)
