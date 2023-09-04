from fastapi_core.service import Service

from app.models import Food
from app.models.order import Order
from app.models.order_foods import OrderFood
from app.repositories.order_repository.order_repository_abc import OrderRepositoryABC
from fastapi_core.utils.exceptions import EntityNotFoundException

from app.schemas.routes.order_router_schemas import CreateOrderSchema
from app.services.v1.food_service import FoodService


class OrderService(Service):

    def __init__(self, order_repository: OrderRepositoryABC, food_service: FoodService):
        super().__init__(repository=order_repository, pk_field=Order.id)
        self.food_service = food_service

    async def get_by_order_key(self, order_key: str, raise_exception_that_not_exist: bool = True) -> Order:
        if obj := await self.repository.find_one(
            filters={'order_key': order_key},
            relationship_to_load=['foods']
        ):
            return obj

        if raise_exception_that_not_exist:
            raise EntityNotFoundException

    async def make_order(self, create_order: CreateOrderSchema) -> Order:
        order = Order(
            client_name=create_order.client_name
        )

        for order_food in create_order.foods:
            food: Food = await self.food_service.get_by_pk(
                pk=order_food.food_id,
                allow_deleted=False,
                raise_exception_that_not_exist=True
            )

            order.foods.append(
                OrderFood(
                    price=food.price,
                    **order_food.dict()
                )
            )

        order.calculate_total_price()
        return await self.repository.create(order)

    async def finish_order(self, order_key: str) -> Order:
        order = await self.get_by_order_key(order_key=order_key)
        order.finish()
        return await self.repository.create(order)

    async def get_orders_by_client(self, client_name: str) -> list[Order]:
        return await self.repository.find_all(
            filters={
                'client_name': client_name
            },
            relationship_to_load=['foods']
        )
