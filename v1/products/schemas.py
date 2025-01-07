from pydantic import BaseModel

from uuid import uuid4, UUID
from typing import Union, List
from datetime import datetime

from helpers.responses.schemas import SuccessResponseModel, ErrorResponseModel


class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    stock: int

    created_at: datetime
    updated_at: datetime


# Product request models
class ProductCreateModel(BaseModel):
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
    id: UUID

    name: str
    description: str
    price: float
    stock: int

    created_at: datetime
    updated_at: datetime


class ProductSuccessResponseModel(SuccessResponseModel):
    data: Union[
        List[SingleProductResponseModel],
        SingleProductResponseModel,
        None
    ]


class ProductErrorResponseModel(ErrorResponseModel):
    pass
