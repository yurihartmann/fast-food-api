import typing
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from fastapi_core.model import ModelHelpers

if typing.TYPE_CHECKING:
    from app.models.order_foods import OrderFood, OrderFoodRead

from app.utils import factory_uuid4, factory_order_key


class OrderBase(SQLModel):
    client_name: str = Field(index=True)
    order_key: str = Field(default_factory=factory_order_key, index=True)
    total_price: float = Field()

    created_at: datetime = Field(default_factory=datetime.now)
    finished_at: datetime | None = Field(default=None, nullable=True)


class OrderBaseWithId(OrderBase):
    id: str = Field(primary_key=True, default_factory=factory_uuid4)


class Order(ModelHelpers, OrderBaseWithId, table=True):
    __tablename__ = "order"

    foods: list['OrderFood'] = Relationship(
        back_populates='order',
        sa_relationship_kwargs={
            'lazy': 'joined'
        }
    )

    def calculate_total_price(self):
        self.total_price = 0
        for order_food in self.foods:
            self.total_price += order_food.quantity * order_food.price

    def finish(self):
        if self.finished_at:
            return

        self.finished_at = datetime.now()



