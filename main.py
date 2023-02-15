import uvicorn
from fastapi import FastAPI
from database.database import Base, engine
from fastapi import FastAPI
# from blog.routes import post
from database.middleware import CustomHeaderMiddleware
from blog import main

app = FastAPI()

# middleware
app.add_middleware(CustomHeaderMiddleware)

# app
app.mount("/blog", main.app)


@app.get("/")
async def hello_world():
    return {"Hello": "World"}

# DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
