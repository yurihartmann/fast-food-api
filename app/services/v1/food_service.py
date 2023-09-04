from loguru import logger
from fastapi_core.service import Service
from fastapi_core.utils.exceptions import EntityNotFoundException
from fastapi_core.cache_driver.cache_driver_abc import CacheDriverABC

from app.models.food import Food
from app.repositories.food_repository import FoodRepositoryABC
from app.schemas.routes.food_router_schemas import FoodCaloriesReport


class FoodService(Service):
    REPORT_CALORIES_CACHE_KEY: str = "report_of_foods_calories"

    def __init__(self, food_repository: FoodRepositoryABC, cache_driver: CacheDriverABC):
        self.food_repository = food_repository
        self.cache_driver = cache_driver
        super().__init__(
            repository=self.food_repository,
            pk_field=Food.id
        )

    @classmethod
    def __generate_key_to_cache_food(cls, pk: str) -> str:
        return f"food_cache_{pk}"

    async def get_report_of_foods_calories(self) -> FoodCaloriesReport:
        if cache := await self.cache_driver.get_dict(key=self.REPORT_CALORIES_CACHE_KEY):
            logger.debug("Using cache for get_report_of_foods_calories")
            return FoodCaloriesReport(**cache)

        report = await self.food_repository.report_of_foods_calories()
        await self.cache_driver.set_dict(key=self.REPORT_CALORIES_CACHE_KEY, data=report.dict())
        return report

    async def delete_cache_report_of_foods_calories(self):
        await self.cache_driver.dump(key=self.REPORT_CALORIES_CACHE_KEY)

    async def get_by_pk(
        self,
        pk: any,
        raise_exception_that_not_exist: bool = True,
        allow_deleted: bool = True,
    ) -> Food:
        filters = {
            self.pk_field: pk,
        }

        if not allow_deleted:
            filters['deleted_at'] = None

        if obj := await self.repository.find_one(filters=filters):
            return obj

        if raise_exception_that_not_exist:
            raise EntityNotFoundException
