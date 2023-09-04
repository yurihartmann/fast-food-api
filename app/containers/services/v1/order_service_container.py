from dependency_injector import containers, providers

from app.containers.drivers_container import DriversContainer
from app.repositories.order_repository.order_repository import OrderRepository
from app.services.v1.food_service import FoodService
from app.services.v1.order_service import OrderService


class OrderServiceContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=['app.routes.v1.order_router']
    )

    drivers: DriversContainer = providers.DependenciesContainer()
    food_service: FoodService = providers.Dependency()

    order_repository: OrderRepository = providers.Singleton(
        OrderRepository,
        async_session_manager=drivers.database.provided.factory_async_session_manager
    )

    order_service: OrderService = providers.Singleton(
        OrderService,
        order_repository=order_repository,
        food_service=food_service
    )
