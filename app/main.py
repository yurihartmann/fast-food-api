from fastapi_core.create_app import fast_api_create_app, HelperRoutersEnum

from app.containers.app_container import AppContainer
from app.routes import app_router

container = AppContainer()

app = fast_api_create_app(
    app_router=app_router,
    title="Fast Food API",
    base_path="/api",
    version="0.1.0",
    container=container,
    helper_routers=(
        HelperRoutersEnum.migration,
        HelperRoutersEnum.health_check
    ),
    dependencies=(
        container.drivers.database(),
        container.drivers.cache()
    )
)
