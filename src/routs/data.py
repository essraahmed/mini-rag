from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from helpers.config import get_settings, settings


data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1","data"])


@data_router.post("/upload/{project_id}")
async def upload_file(project_id : str, file: UploadFile, app_settings = Depends(get_settings)):
    


    # validate the file properties
  