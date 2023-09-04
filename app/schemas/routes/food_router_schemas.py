from fastapi import Query
from pydantic.main import BaseModel


class FoodFiltersSchema(BaseModel):
    name: str | None = Query(default=None, description="Name of food")
    show_deleted: bool = Query(default=False, description="Search for foods deleted too")

    def dict(self, *args, **kwargs) -> dict:
        result = super().dict(*args, exclude={'show_deleted'}, exclude_none=True, **kwargs)

        if not self.show_deleted:
            result['deleted_at'] = None
        return result


class FoodCaloriesReport(BaseModel):
    sum_calories: int
    min_calories: int
    max_calories: int
    abv_calories: int
