from fastapi_core.create_app import fast_api_create_app, CreateAppConfig

from app.containers.app_container import AppContainer
from app.routes import app_router

app = fast_api_create_app(
    app_router=app_router,
    create_app_config=CreateAppConfig(
        title="Fast Food API",
        base_path="/api",
        version="0.1.0",
        container=AppContainer()
    )
)
