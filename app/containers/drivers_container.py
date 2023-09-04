from dependency_injector import containers, providers

from fastapi_core.database import Database
from fastapi_core.cache_driver.redis_cache_driver import RedisCacheDriver
from fastapi_core.settings import DatabaseSettings


class DriversContainer(containers.DeclarativeContainer):
    database = providers.Singleton(
        Database,
        db_url=DatabaseSettings().get_postgres_async_db_url(),
        db_url_read_only=DatabaseSettings().get_postgres_async_db_url(),
        echo_queries=True
    )

    cache = providers.Singleton(
        RedisCacheDriver,
        password="redis_password",
        namespace_prefix='food_api'
    )
