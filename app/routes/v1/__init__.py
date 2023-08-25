from fastapi import APIRouter

from app.routes.v1.food_category_router import food_category_router

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(
    router=food_category_router,
)
