from fastapi import APIRouter

from app.routes.v1.food_router import food_router
from app.routes.v1.order_router import order_router

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(
    router=food_router,
)

v1_router.include_router(
    router=order_router
)
