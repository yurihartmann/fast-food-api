import typing

from pydantic.main import BaseModel
from sqlmodel import SQLModel, Field, Relationship

if typing.TYPE_CHECKING:
    from app.models import Food

from app.models.order import Order


class OrderFoodBase(SQLModel):
    quantity: int = Field(default=1)
    observation: str = Field(default='')
    price: float = Field()


class OrderFood(OrderFoodBase, table=True):
    __tablename__ = "order_food"

    order_id: str = Field(primary_key=True, foreign_key="order.id")
    food_id: str = Field(primary_key=True, foreign_key="food.id")

    order: 'Order' = Relationship(back_populates="foods")
    food: 'Food' = Relationship(
        back_populates='orders_foods',
        sa_relationship_kwargs={
            'lazy': 'joined'
        }
    )
