from fastapi import FastAPI
from app.routes.router import api_router
from app.settings.app_config import AppConfig


config = AppConfig()

app = FastAPI(
    title="Code Challenge API",
    openapi_url=f"{config.get_root_path()}/openapi.json",
    root_path=config.get_root_path(),
)

app.include_router(api_router)
