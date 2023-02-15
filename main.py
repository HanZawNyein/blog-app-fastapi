import uvicorn
from fastapi import FastAPI
from database.database import Base, engine
from fastapi import FastAPI
from database.middleware import CustomHeaderMiddleware
from blog.routes import post
from auth.routes import auth
from routes.token import router

app = FastAPI()

# middleware
app.add_middleware(CustomHeaderMiddleware)
app.include_router(router, tags=['Token'])
app.include_router(auth.router, tags=['Auth'], prefix="/auth")
app.include_router(post.router, tags=['Post'], prefix="/post")


# DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
