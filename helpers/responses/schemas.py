from pydantic import BaseModel
from typing import Any

# Response model base schema


class SuccessResponseModel(BaseModel):
    success: bool
    status_code: float
    message: str
    data: Any


class ErrorResponseModel(BaseModel):
    success: bool
    status_code: int
    message: str
