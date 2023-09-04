from fastapi import APIRouter, Depends, Query
from dependency_injector.wiring import Provide, inject

from app.containers.services.v1.order_service_container import OrderServiceContainer
from app.schemas.routes.order_router_schemas import CreateOrderSchema, OrderRead

from app.services.v1.order_service import OrderService

order_router = APIRouter(prefix='', tags=['order'])


@order_router.get(
    path='/order/{order_key}',
    response_model=OrderRead
)
@inject
async def get_order(
    order_key: str,
    order_service: OrderService = Depends(
        Provide[OrderServiceContainer.order_service]
    )
):
    return await order_service.get_by_order_key(
        order_key=order_key
    )


@order_router.get(
    path='/client/orders',
    response_model=list[OrderRead]
)
@inject
async def get_orders_by_client(
    client_name: str = Query(title="Client Name", example="Lary"),
    order_service: OrderService = Depends(
        Provide[OrderServiceContainer.order_service]
    )
):
    return await order_service.get_orders_by_client(
        client_name=client_name
    )


@order_router.post(
    path='/order',
    response_model=OrderRead
)
@inject
async def make_order(
    create_order: CreateOrderSchema,
    order_service: OrderService = Depends(
        Provide[OrderServiceContainer.order_service]
    )
):
    return await order_service.make_order(
        create_order=create_order
    )


@order_router.patch(
    path='/order/{order_key}/finish',
    response_model=OrderRead
)
@inject
async def finish_order(
    order_key: str,
    order_service: OrderService = Depends(
        Provide[OrderServiceContainer.order_service]
    )
):
    return await order_service.finish_order(
        order_key=order_key
    )
