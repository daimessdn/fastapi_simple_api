from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from v1.products.schemas import ProductCreateModel, ProductUpdateModel
from v1.products.params import responses_param
from v1.products.services import ProductService

from helpers.responses import responses

from db.main import get_session

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


product_router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

product_service = ProductService()


@product_router.get("/", responses=responses_param["get_all"])
async def get_products(session: AsyncSession = Depends(get_session)):
    """List all products stored on database"""
    products = await product_service.get_all_products(session)
    return responses.get_success_response("Produk berhasil ditampilkan", products)


@product_router.get("/{id}", responses=responses_param["get_by_id"])
async def get_product_by_id(id: str, session: AsyncSession = Depends(get_session)):
    """Obtain certain product stored on database based on product ID"""
    product = await product_service.get_product_by_id(id, session)

    if product:
        return responses.get_success_response("Produk berhasil ditampilkan", product)

    raise responses.get_error_not_found_response("Produk tidak ditemukan")


@product_router.post("/", responses=responses_param["create"])
async def add_products(request: ProductCreateModel, session: AsyncSession = Depends(get_session)):
    """Create new collection of product data and store into database"""

    new_product = await product_service.create_product(request, session)

    return responses.get_success_created_response("Berhasil menambahkan produk", new_product)


@product_router.put("/{id}", responses=responses_param["update"])
async def update_product(id: str, request: ProductUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update certain product data based on product ID with the new data properties"""

    updated_product = await product_service.update_product(id, request, session)

    if updated_product:
        return responses.get_success_response("Produk berhasil diperbarui", updated_product)

    raise responses.get_error_not_found_response("Produk tidak ditemukan")


@product_router.delete("/{id}", responses=responses_param["delete"])
async def delete_product(id: str, session: AsyncSession = Depends(get_session)):
    """Delete certain product data based on product ID"""

    deleted_product = await product_service.delete_product(id, session)

    if deleted_product:
        return responses.get_success_response("Produk berhasil dihapus", None)

    raise responses.get_error_not_found_response("Produk tidak ditemukan")
