import uuid

from sqlmodel import SQLModel, Field, Relationship
from app.models.food_category import FoodCategory


class FoodBase(SQLModel):
    name: str
    description: str
    calories: float
    price: float

    category: str = Field(foreign_key="food_category.key")


class FoodBaseWithUUID(FoodBase):
    id: str = Field(primary_key=True, default_factory=uuid.uuid4)


class Food(FoodBaseWithUUID):
    __tablename__ = "food"

    category: FoodCategory | None = Relationship(back_populates="heroes")
