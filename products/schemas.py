from pydantic import BaseModel
from uuid import uuid4


class Product:
    id: uuid4
    name: str
    description: str
    price: float
    stock: int


class ProductAddModel(BaseModel):
    name: str
    description: str
    price: float
    stock: int
