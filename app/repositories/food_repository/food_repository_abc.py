from abc import ABC, abstractmethod

from fastapi_core.repository.repository_abc import RepositoryABC

from app.schemas.routes.food_router_schemas import FoodCaloriesReport


class FoodRepositoryABC(RepositoryABC, ABC):

    @abstractmethod
    async def report_of_foods_calories(self) -> FoodCaloriesReport:
        """Not implemented"""
