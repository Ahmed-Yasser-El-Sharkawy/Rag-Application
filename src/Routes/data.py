from fastapi import FastAPI ,APIRouter ,Depends ,UploadFile ,status
from fastapi.responses import JSONResponse
from helpers.config import get_settings ,settings
from controllers import DataController ,ProjectController
import os
import aiofiles 
from models import ResponseSignal


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str,file:UploadFile,
                      app_settings: settings = Depends(get_settings)):
    
    data_controller = DataController()
    # validate the file properties
    is_valid, result_signal = data_controller.validate_uploader_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": result_signal}
        )

    project_dir_path = ProjectController().get_project_path(project_id)
    new_file_name = data_controller.Generate_unique_File_Name(
        orgin_file=file.filename,
        project_id=project_id
    )
    
    file_path=os.path.join(project_dir_path, new_file_name)

    async with aiofiles.open(file_path, 'wb') as out_file:
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await out_file.write(chunk)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": ResponseSignal.FILE_UPLOAD_SUCCESS}
    )