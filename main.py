from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from route.router import api_router

app = FastAPI()

app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

