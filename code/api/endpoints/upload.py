from fastapi import APIRouter, UploadFile, File, HTTPException
import os

from code.utils.file_handling import save_file

router = APIRouter()

UPLOAD_DIRECTORY = "./uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = await save_file(file)
        return {"file_url": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/delete/")
async def delete_file(file_path: str):
    try:
        file_path = delete_file(file_path)
        return {"message": f"File {file_path} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

