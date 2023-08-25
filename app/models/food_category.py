import typing
import uuid

from fastapi_core.model import ModelMixin
from sqlmodel import Field, SQLModel, Relationship

if typing.TYPE_CHECKING:
    from app.models.food import Food


class FoodCategoryBase(SQLModel):
    name: str
    description: str


class FoodCategoryWithKey(FoodCategoryBase):
    key: str = Field(primary_key=True, default_factory=uuid.uuid4)


class FoodCategory(FoodCategoryBase, ModelMixin):
    __tablename__ = "food_category"

    foods: list["Food"] = Relationship(back_populates="category")


class CreateFood(FoodCategoryBase):
    pass


class CreateUpdate(FoodCategoryBase):
    pass
