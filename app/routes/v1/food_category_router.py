from fastapi import APIRouter

food_category_router = APIRouter(prefix='/food/category')


@food_category_router.get(
    path='/'
)
async def get_all_food_categories():
    return "ALL"
