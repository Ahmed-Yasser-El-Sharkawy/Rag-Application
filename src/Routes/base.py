from fastapi import FastAPI ,APIRouter ,Depends
from helpers.config import get_settings ,settings
import os

Base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@Base_router.get("/")
async def read_root(app_settings: settings = Depends(get_settings)):
    
    App_name=app_settings.APP_Name
    app_version=app_settings.APP_Version
    
    return {
        "App name": App_name,
        "App version": app_version
    }