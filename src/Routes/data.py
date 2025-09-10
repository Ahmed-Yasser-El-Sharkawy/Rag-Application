from fastapi import FastAPI ,APIRouter ,Depends ,UploadFile ,status
from fastapi.responses import JSONResponse
from helpers.config import get_settings ,settings
from controllers import DataController ,ProjectController, ProcessController
import os
import aiofiles 
from models import ResponseSignal
import logging
from .schemes.data import ProcessRequest

logger = logging.getLogger("uvicorn.error")

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
    new_file_name ,file_id = data_controller.Generate_unique_Filepath(
        orgin_file=file.filename,
        project_id=project_id
    )
    
    file_path=os.path.join(project_dir_path, new_file_name)

    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await out_file.write(chunk)
                

    except Exception as e:
        logger.error(f"File upload failed: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseSignal.FILE_UPLOAD_FAILED}
        )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": ResponseSignal.FILE_UPLOAD_SUCCESS,
            "file_id": file_id
        }
    )
    
@data_router.post("/process/{project_id}")
async def process_endpoint(project_id:str , process_request: ProcessRequest,):
    file_id=process_request.file_id
    chunk_size=process_request.chunk_size
    overlap=process_request.overlap
    do_reset=process_request.do_reset
    
    process_controller=ProcessController(project_id=project_id)
    
    file_content=process_controller.get_file_content(file_id=file_id)
    
    file_chunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap=overlap
    )
    
    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseSignal.FILE_PROCESSING_FAILED}
        )

    return file_chunks
    
    