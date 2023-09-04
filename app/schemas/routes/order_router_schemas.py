from pydantic.class_validators import validator
from pydantic.fields import Field
from pydantic.main import BaseModel, ValidationError

from app.models import Food
from app.models.order import OrderBase
from app.models.order_foods import OrderFoodBase


class CreateOrderFoodSchema(BaseModel):
    food_id: str = Field(example='ee9abed4-b011-45ab-b111-edf69219f59f')
    quantity: int = Field(default=1)
    observation: str = Field(default='', example='No onions')

    @validator('quantity')
    def validate_quantity(cls, quantity: int) -> int:
        if quantity < 1:
            raise ValidationError('quantity needs 1 or more')

        return quantity


class CreateOrderSchema(BaseModel):
    client_name: str = Field(example="Lary")
    foods: list[CreateOrderFoodSchema] = Field(min_items=1)


class OrderFoodRead(OrderFoodBase):
    food: Food | None = None


class OrderRead(OrderBase):
    foods: list[OrderFoodRead] | None

