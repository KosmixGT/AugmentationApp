import os
from fastapi import APIRouter, HTTPException, File, UploadFile
from pydantic import BaseModel
from typing import List
import base64

router = APIRouter(tags=['imageProcessing'])

class Image(BaseModel):
    image_base64: str

@router.post("/upload_images/", response_model=List[Image])
async def upload_images(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        content = await file.read()
        encoded_image = base64.b64encode(content).decode('utf-8')
        images.append(Image(image_base64=encoded_image))

        # Путь к директории
        directory = 'loadedImages/'

        # Проверка на существование директории
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Сохранение изображения в файловой системе
        with open(os.path.join(directory, file.filename), 'wb') as f:
            f.write(content)

    return images


