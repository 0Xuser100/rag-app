from fastapi import APIRouter,FastAPI,Depends,UploadFile,status
from fastapi.responses import JSONResponse
from helpers.config import get_settings,Settings
import os
import aiofiles
from controllers import DataController,ProjectContorller,ProcessController
from models import ResponseSignals
import logging
from .schemes.data import ProccessRequest
# Initialize logger
logger = logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str,file:UploadFile,app_settings:Settings = Depends(get_settings)):
    datacontroller=DataController()
    is_valid,result_signal=datacontroller.validate_uploaded_file(file=file)
    

    if not is_valid:
        
     return JSONResponse(
              status_code=status.HTTP_400_BAD_REQUEST,
              content={"is_valid":is_valid,"signal":result_signal}
              )
    else :
        #project_dir_path=ProjectContorller().get_project_path(project_id=project_id) # path of project directory
        # file_path=os.path.join( # path of file in project directory 
        #     project_dir_path,
        #     file.filename
        # )   
        # Generate a unique filename using the project ID and the original filename
        file_path,file_id=datacontroller.generate_unique_filepath(
           original_filename=file.filename,
           project_id=project_id
           )
        try:
            async with aiofiles.open(file_path, 'wb') as f: 
                while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                        await f.write(chunk)
        except Exception as e:
            logger.error(f"Error while uploading file: {e}")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"signal":ResponseSignals.FILE_UPLOAD_FAILED.value}
            )
    
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"signal":ResponseSignals.FILE_UPLOAD_SUCCESS.value
                     ,"file_id":file_id,
                    }
        )
    
@data_router.post("/process/{project_id}")
async def proccess_endpoint(project_id:str,proccess_request:ProccessRequest):
    file_id=proccess_request.file_id
    chunk_size=proccess_request.chunk_size
    overlap_size=proccess_request.overlap_size

    process_controller=ProcessController(project_id=project_id)
    
    file_content=process_controller.get_file_content(file_id=file_id)
    
    file_chunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size   
)
    
    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal":ResponseSignals.FILE_PROCESSING_FAILED.value}
        )
    return file_chunks
