from fastapi import APIRouter

from v1.products.routes import product_router

v1_router = APIRouter(
    prefix="/v1"
)


v1_router.include_router(product_router)
