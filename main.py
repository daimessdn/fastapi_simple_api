from fastapi import FastAPI
from uuid import uuid4

from data.products import product_data

from products.schemas import Product, ProductAddModel

from utils import responses

app = FastAPI()


@app.get("/", tags=["Welcome"])
async def hello_world():
    return {"msg": "hello, world!"}


@app.get("/products", tags=["Products"])
async def get_products():
    return responses.get_success_response("Produk berhasil ditampilkan", product_data)


@app.get("/products/{id}", tags=["Products"])
async def get_product_by_id(id: str):
    for item in product_data:
        if item["id"] == id:
            return responses.get_success_response("Produk berhasil ditampilkan", item)
    return responses.get_error_not_found_response("Produk tidak ditemukan")


@app.post("/products", tags=["Products"])
async def add_products(request: ProductAddModel):
    product_to_add = request.model_dump()
    product_to_add["id"] = str(uuid4())

    product_data.append(product_to_add)

    return responses.get_success_response("Berhasil menambahkan produk", product_to_add)
