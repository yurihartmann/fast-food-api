from fastapi_core.repository.repository import Repository
from fastapi_core.database import AsyncSessionManager

from app.models.order import Order
from app.repositories.order_repository.order_repository_abc import OrderRepositoryABC


class OrderRepository(OrderRepositoryABC, Repository):
    def __init__(self, async_session_manager: type[AsyncSessionManager]):
        super().__init__(
            async_session_manager=async_session_manager,
            model=Order
        )
