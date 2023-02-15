from fastapi import FastAPI
from blog.routes import post

app = FastAPI()

# routers
app.include_router(post.router, prefix="/posts")
