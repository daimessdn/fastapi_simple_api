from pydantic import BaseModel
from uuid import uuid4

from typing import Union, List

from helpers.responses.schemas import SuccessResponseModel, ErrorResponseModel


class Product(BaseModel):
    id: uuid4
    name: str
    description: str
    price: float
    stock: int


# Product request models
class ProductAddModel(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductUpdateModel(BaseModel):
    name: str
    description: str
    price: float
    stock: int


# Product response models
class SingleProductResponseModel(Product):
    id: str

    name: str
    description: str
    price: float
    stock: int


class ProductSuccessResponseModel(SuccessResponseModel):
    data: Union[
        List[SingleProductResponseModel],
        SingleProductResponseModel,
        None
    ]


class ProductErrorResponseModel(ErrorResponseModel):
    pass
