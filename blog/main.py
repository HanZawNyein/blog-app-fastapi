import uvicorn
from fastapi import FastAPI, Depends
from auth.utilities.oauth2 import get_current_active_user
from .routes import post

app = FastAPI()

app.include_router(post.router, tags=['Post'],
                   dependencies=[
                   Depends(get_current_active_user)])

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
