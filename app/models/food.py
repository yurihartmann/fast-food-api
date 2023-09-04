from sqlmodel import SQLModel, Field, Relationship
from fastapi_core.model import ModelMixin

from app.models.order_foods import OrderFood
from app.utils import factory_uuid4


class FoodBase(SQLModel):
    name: str = Field(index=True, schema_extra={'example': 'Cheddar Burger'})
    description: str = Field(schema_extra={'example': 'Bread, Cheddar and Burger'})
    calories: float = Field(schema_extra={'example': 350})
    price: float = Field(index=True, schema_extra={'example': 9.90})


class FoodBaseWithUUID(FoodBase):
    id: str = Field(primary_key=True, default_factory=factory_uuid4)


class Food(ModelMixin, FoodBaseWithUUID, table=True):
    __tablename__ = "food"

    orders_foods: list['OrderFood'] = Relationship(back_populates='food')


class CreateFoodSchema(FoodBase):
    pass


class UpdateFoodSchema(FoodBase):
    pass
