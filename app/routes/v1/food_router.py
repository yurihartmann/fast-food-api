from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params

from app.containers.services.v1.food_service_container import FoodServiceContainer
from app.models import Food
from app.models.food import CreateFoodSchema, UpdateFoodSchema
from app.schemas.routes.food_router_schemas import FoodFiltersSchema, FoodCaloriesReport
from app.services.v1.food_service import FoodService

food_router = APIRouter(prefix='/food', tags=['food'])


@food_router.get(
    path='/',
    response_model=Page[Food]
)
@inject
async def get_all_foods(
    params: Params = Depends(),
    food_filters: FoodFiltersSchema = Depends(),
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.get_paginated(
        params=params, filters=food_filters.dict()
    )


@food_router.get(
    path='/calories/report',
    response_model=FoodCaloriesReport
)
@inject
async def get_all_foods(
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.get_report_of_foods_calories()


@food_router.delete(
    path='/calories/report/cache',
)
@inject
async def get_all_foods(
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.delete_cache_report_of_foods_calories()


@food_router.get(
    path='/{food_id}',
    response_model=Food
)
@inject
async def get_all_foods(
    food_id: str,
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.get_by_pk(
        pk=food_id
    )


@food_router.post(
    path='/',
    response_model=Food
)
@inject
async def create_food(
    create_food_schema: CreateFoodSchema,
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.create(
        obj=Food(**create_food_schema.dict())
    )


@food_router.put(
    path='/{food_id}',
    response_model=Food
)
@inject
async def update_food(
    food_id: str,
    update_food_schema: UpdateFoodSchema,
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.update(
        pk=food_id, obj_update=update_food_schema
    )


@food_router.delete(
    path='/{food_key}',
    status_code=HTTPStatus.OK
)
@inject
async def soft_delete_food(
    food_key: str,
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.soft_delete(pk=food_key)


@food_router.delete(
    path='/{food_key}',
    status_code=HTTPStatus.OK
)
@inject
async def soft_delete_food(
    food_key: str,
    food_service: FoodService = Depends(
        Provide[FoodServiceContainer.food_service]
    )
):
    return await food_service.soft_delete(pk=food_key)