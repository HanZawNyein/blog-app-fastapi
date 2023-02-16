import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from database.database import Base, engine
from middleware.request_user import RequestUserMiddleware
from blog.main import app as blog_app
from auth.main import app as auth_app
from config.ConfSettings import settings

app = FastAPI()

# middleware
app.add_middleware(RequestUserMiddleware)

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# apps
app.mount("/auth", auth_app)
app.mount("/blog", blog_app)

# DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.HOST, port=8080, reload=True)
