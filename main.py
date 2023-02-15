import uvicorn
from fastapi import FastAPI
from database.database import Base, engine
from middleware.request_user import RequestUserMiddleware
from blog.main import app as blog_app
from auth.main import app as auth_app
from config.ConfSettings import settings
app = FastAPI()

# middleware
app.add_middleware(RequestUserMiddleware)

# apps
app.mount("/auth", auth_app)
app.mount("/blog", blog_app)

# DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=8080)
