import os
from fastapi import APIRouter, HTTPException, File, UploadFile
from typing import Optional

router = APIRouter(tags=['imageProcessing'])

@router.post("/upload_images/")
async def upload_images(zip_file: UploadFile = File(...)):
    if not zip_file.filename.endswith('.zip'):
        raise HTTPException(status_code=400, detail="Можно загрузить только zip-архив")

    content = await zip_file.read()

    # Путь к директории
    directory = 'loadedImages/'

    # Проверка на существование директории
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Сохранение zip-архива
    with open(os.path.join(directory, zip_file.filename), 'wb') as f:
        f.write(content)

    return {"detail": "Файл успешно загружен"}
