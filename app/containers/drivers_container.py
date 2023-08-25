from dependency_injector import containers, providers

from fastapi_core.database import Database

from fastapi_core.app_settings import DatabaseSettings


class DriversContainer(containers.DeclarativeContainer):
    database = providers.Singleton(
        Database,
        db_url=DatabaseSettings().get_postgres_async_db_url(),
        db_url_read_only=DatabaseSettings().get_postgres_async_db_url(),
        echo_queries=True
    )

    # cache = providers.Singleton(RedisCacheDriver)
