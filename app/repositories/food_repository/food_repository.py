from fastapi_core.repository.repository import Repository
from fastapi_core.database import AsyncSessionManager
from sqlmodel import SQLModel, func, select

from app.models.food import Food
from app.repositories.food_repository import FoodRepositoryABC
from app.schemas.routes.food_router_schemas import FoodCaloriesReport


class FoodRepository(FoodRepositoryABC, Repository):

    def __init__(self, async_session_manager: type[AsyncSessionManager]):
        super().__init__(
            async_session_manager=async_session_manager,
            model=Food
        )

    async def report_of_foods_calories(self) -> FoodCaloriesReport:
        async with self.async_session_manager() as session:
            query = select(
                func.sum(Food.calories),
                func.min(Food.calories),
                func.max(Food.calories),
                func.avg(Food.calories),
            ).select_from(self.model)

            result = await session.execute(query)
            _sum, _min, _max, _avg = result.fetchall()[0]

            return FoodCaloriesReport(
                sum_calories=_sum,
                min_calories=_min,
                max_calories=_max,
                abv_calories=_avg,
            )
