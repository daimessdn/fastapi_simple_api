from fastapi import APIRouter
from uuid import uuid4

from v1.products.schemas import ProductAddModel, ProductUpdateModel
from v1.products.params import responses_param
from data.products import product_data

from helpers.responses import responses

product_router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@product_router.get("/")
async def get_products():
    """List all products stores on dummy database"""

    return responses.get_success_response("Produk berhasil ditampilkan", product_data)


@product_router.get("/{id}", responses=responses_param["get_by_id"])
async def get_product_by_id(id: str):
    """Obtain certain product stores on dummy database based on product ID"""

    for item in product_data:
        if item["id"] == id:
            return responses.get_success_response("Produk berhasil ditampilkan", item)

    raise responses.get_error_not_found_response("Produk tidak ditemukan")


@product_router.post("/", responses=responses_param["create"])
async def add_products(request: ProductAddModel):
    """Create new collection of product data and store into dummy database"""

    product_to_add = {
        "id": str(uuid4()),

        **request.model_dump()
    }

    product_data.append(product_to_add)

    return responses.get_success_created_response("Berhasil menambahkan produk", product_to_add)


@product_router.put("/{id}", responses=responses_param["update"])
async def update_product(id: str, request: ProductUpdateModel):
    """Update certain product data based on product ID with the new data properties"""

    product_to_update = request

    for item_index, item in enumerate(product_data):
        if item["id"] == id:
            item = {
                "id": id,

                **product_to_update.model_dump()
            }
            product_data[item_index] = item

            return responses.get_success_response("Produk berhasil diperbarui", item)

    raise responses.get_error_not_found_response("Produk tidak ditemukan")


@product_router.delete("/{id}", responses=responses_param["delete"])
async def delete_product(id: str):
    """Delete certain product data based on product ID"""

    for item_index, item in enumerate(product_data):
        if item["id"] == id:
            del product_data[item_index]

            return responses.get_success_response("Produk berhasil dihapus", None)

    raise responses.get_error_not_found_response("Produk tidak ditemukan")
