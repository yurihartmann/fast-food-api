from fastapi import APIRouter

from app.routes.v1 import v1_router

app_router = APIRouter()


app_router.include_router(
    router=v1_router
)
