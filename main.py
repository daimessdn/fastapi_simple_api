from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from helpers.responses.responses import Response

from v1.routes import v1_router

app = FastAPI(
    version="1.0",
    title="FastAPI Simple API",
    description="A simple API using FastAPI",
)


@app.exception_handler(Response)
async def exception_handler(request: Request, exc: Response):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "status_code": exc.status_code,
            "message": exc.message,
        }
    )


@app.get("/", tags=["Welcome"])
async def hello_world():
    """Starter API endpoint"""

    return {"msg": "hello, world!"}

app.include_router(v1_router)
