from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from products.routes import product_router
from helpers.responses.responses import Response

app = FastAPI()


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
    return {"msg": "hello, world!"}

app.include_router(product_router)
