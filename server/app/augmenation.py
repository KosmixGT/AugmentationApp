from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import cv2
import numpy as np
import os
import zipfile
import shutil

router = APIRouter(tags=['imageAugmentation'])


def augment_image(image, rotation_angle, noise_sigma, contrast_alpha, brightness_beta):
    # Изменение размера
    # resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)  # изменение размера в 2 раза по каждому измерению

    # Поворот
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D(
        (width / 2, height / 2), rotation_angle, 1)  # поворот на 45 градусов
    rotated = cv2.warpAffine(image, rotation_matrix, (width, height))

    # Добавление шума
    mean = 0
    # sigma = 30
    gauss = np.random.normal(mean, noise_sigma, image.shape)
    noisy = np.clip(rotated + gauss, 0, 255).astype(np.uint8)

    # Изменение яркости и контраста
    # alpha = 1.5  # Коэффициент контрастности
    # beta = 0  # Смещение яркости
    contrast_brightness = cv2.convertScaleAbs(
        noisy, alpha=contrast_alpha, beta=brightness_beta)
    out_image = contrast_brightness
    return out_image


@router.post("/augment_images/")
async def augment_images(rotation_angle: int, noise_sigma: int, contrast_alpha: float, brightness_beta: int, aug_percentage: int):
    # Сначала загрузим изображения из zip-архива
    zip_load_images_path = "loadedImages/"
    load_images_path = "loadedImages/images/"
    save_images_path = "outImages/images/"

    os.makedirs(os.path.dirname(load_images_path), exist_ok=True)
    os.makedirs(os.path.dirname(save_images_path), exist_ok=True)

    # Найдем путь к zip-архиву
    load_zip_path = os.path.join(zip_load_images_path, next(
        f for f in os.listdir(zip_load_images_path) if f.endswith(".zip")))

    with zipfile.ZipFile(load_zip_path, 'r') as zip_ref:
        zip_ref.extractall(load_images_path)

    # Теперь применим аугментацию к изображениям
    images = os.listdir(load_images_path)
    num_images_to_augment = int(len(images) * aug_percentage / 100)

    for image_name in images[:num_images_to_augment]:
        image_path = os.path.join(load_images_path, image_name)
        img = cv2.imread(image_path)
        augmented_img = augment_image(
            img, rotation_angle, noise_sigma, contrast_alpha, brightness_beta)
        cv2.imwrite(os.path.join(save_images_path, image_name), augmented_img)

    # Удалим изначальные изображения
    shutil.rmtree(load_images_path)

    # Теперь упакуем аугментированные изображения в zip-архив и отправим его
    zip_save_images_path = "outImages/"
    os.makedirs(zip_save_images_path, exist_ok=True)
    save_zip_path = os.path.join(zip_save_images_path, "augmented_images.zip")

    with zipfile.ZipFile(save_zip_path, 'w') as zip_ref:
        for image_name in os.listdir(save_images_path):
            zip_ref.write(os.path.join(
                save_images_path, image_name), image_name)

    # Удалим аугментированные изображения
    shutil.rmtree(save_images_path)

    # Отправим zip-архив на клиент
    return FileResponse(save_zip_path, media_type='application/zip', filename='augmented_images.zip')
