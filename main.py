from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from Exception.Project221ossException import Project221ossException
from route.router import api_router

app = FastAPI()


@app.exception_handler(Project221ossException)
async def validation_exception_handler(request, exc: Project221ossException):
    print(exc)
    return JSONResponse(
        status_code=exc.get_code(),
        content=exc.get_json(),
    )

app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

