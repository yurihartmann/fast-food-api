from dependency_injector import containers, providers

from app.containers.drivers_container import DriversContainer
from app.repositories.food_repository.food_repository import FoodRepository
from app.services.v1.food_service import FoodService


class FoodServiceContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=['app.routes.v1.food_router']
    )

    drivers: DriversContainer = providers.DependenciesContainer()

    food_repository: FoodRepository = providers.Singleton(
        FoodRepository,
        async_session_manager=drivers.database.provided.factory_async_session_manager
    )

    food_service: FoodService = providers.Singleton(
        FoodService,
        food_repository=food_repository,
        cache_driver=drivers.cache
    )
