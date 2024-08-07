import aiofiles
import os
from fastapi import UploadFile

UPLOAD_DIRECTORY = "./uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


async def save_file(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    return file_path


async def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
        return file_path
