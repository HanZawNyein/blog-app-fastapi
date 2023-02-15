import uvicorn
from fastapi import FastAPI, Depends
from database.database import Base, engine
from database.middleware import CustomHeaderMiddleware
from blog.main import app as blog_app
from auth.main import app as auth_app

app = FastAPI()

# middleware
app.add_middleware(CustomHeaderMiddleware)

# apps
app.mount("/auth", auth_app)
app.mount("/blog", blog_app)

# DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
