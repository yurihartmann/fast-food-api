from dependency_injector import containers, providers

from app.containers.drivers_container import DriversContainer
from app.containers.services.v1.food_service_container import FoodServiceContainer
from app.containers.services.v1.order_service_container import OrderServiceContainer


class AppContainer(containers.DeclarativeContainer):
    # Drivers
    drivers: DriversContainer = providers.Container(
        DriversContainer
    )

    # V1 CONTAINERS
    food_service_container: FoodServiceContainer = providers.Container(
        FoodServiceContainer,
        drivers=drivers
    )

    order_service_container: OrderServiceContainer = providers.Container(
        OrderServiceContainer,
        drivers=drivers,
        food_service=food_service_container.food_service
    )
