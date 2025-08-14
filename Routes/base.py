from fastapi import FastAPI ,APIRouter
import os

Base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@Base_router.get("/")
async def read_root():
    App_name=os.getenv("APP_Name")
    app_version=os.getenv("APP_Version")
    return {
        "App name": App_name,
        "App version": app_version
    }