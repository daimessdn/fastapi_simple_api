from fastapi import APIRouter

auth_router = APIRouter(
    prefix="auth",
    tags=["Auth"],
)


@auth_router.post("/sign_up")
async def sign_up():
    pass
