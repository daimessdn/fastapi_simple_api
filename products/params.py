from products.schemas import ProductSuccessResponseModel, ProductErrorResponseModel

responses_param = {
    "create": {
        200: {
            "description": "Success Response",
            "model": ProductSuccessResponseModel,
        },
        400: {
            "description": "Error Input",
            "model": ProductErrorResponseModel,
        },
    },
    "get_by_id": {
        200: {
            "description": "Success Response",
            "model": ProductSuccessResponseModel,
        },
        404: {
            "description": "Product Not Found",
            "model": ProductErrorResponseModel,
        },
    },
    "update": {
        200: {
            "description": "Success Response",
            "model": ProductSuccessResponseModel,
        },
        400: {
            "description": "Error Input",
            "model": ProductErrorResponseModel,
        },
        404: {
            "description": "Product Not Found",
            "model": ProductErrorResponseModel,
        },
    },
    "delete": {
        200: {
            "description": "Success Response",
            "model": ProductSuccessResponseModel,
        },
        404: {
            "description": "Product Not Found",
            "model": ProductErrorResponseModel,
        },
    },
}
