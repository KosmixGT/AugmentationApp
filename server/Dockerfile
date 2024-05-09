# Уменьшенная версия Debian для Python
FROM python:3.12-slim

# Заполнение поля автора
LABEL Author="Augmentation team"

# Здесь можно указать любую информацию, к примеру тип
LABEL type="Backend-fast-api"

# Обновление пакетов и установка библиотек для OpenCV
RUN apt-get update && apt-get install --no-install-recommends -y libgl1-mesa-glx libglib2.0-0

# Задаём название рабочей директории
WORKDIR /program/app

# Копируем файл с зависимостями в program
COPY ./requirements.txt ..

# Обновляем пакетный менеджер и устанавливаем все зависимости
RUN pip install --upgrade pip
RUN pip install -r ../requirements.txt

# Копируем наше приложение в program/app
COPY ./app .

# Задаём строку подключения к БД из переменных GitLab
ARG DB_CONNECTION
ENV DB_CONNECTION=$DB_CONNECTION

# Обозначаем для пользователя порт, который прослушивается приложением
EXPOSE 5000

# Задаём базовую команду
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port"]

# Задаём передаваемые агрументы
CMD ["5000"]

