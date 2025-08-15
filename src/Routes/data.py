from fastapi import FastAPI ,APIRouter ,Depends ,UploadFile ,status
from fastapi.responses import JSONResponse
from helpers.config import get_settings ,settings
from controllers import DataController ,ProjectController
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str,file:UploadFile,
                      app_settings: settings = Depends(get_settings)):
    
    # validate the file properties
    is_valid, result_signal = DataController().validate_uploader_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": result_signal}
        )

    project_dir = ProjectController().get_project_path(project_id)
    return {"is_valid": is_valid, 
            "result_signal": result_signal,
            "project_directory": project_dir}

