# Облегчённый образ для Node.js с DockerHub
# В этом образе мы собираем приложение в статичный сайт
FROM node:alpine3.18 as build-dist

# Задаём рабочую директорию
WORKDIR /app

# Копируем все файлы, в том числе package.json в рабочую директорию
COPY . .

# Устанавливаем зависимости
RUN npm install

# Собираем приложение
RUN npm run build

# Образ для nginx с DockerHub
#FROM nginx:1.25.5-alpine-slim
FROM nginx:latest

# Заполнение поля автора
MAINTAINER "Augmentation team"

# Здесь можно указать любую информацию, к примеру тип
LABEL type="Frontend-vue-vite"

# Копируем сборку с предыдущего этапа на сервер
# Здесь вообще должна быть публикация на AWS хостинг
COPY --from=build-dist /app/dist /usr/share/nginx/html/dist

# Удаляем существующий конфиг сервера
RUN rm /etc/nginx/conf.d/default.conf

# Копируем свой конфиг на сервер
COPY default.conf.template /etc/nginx/templates/

# Указываем порт для сервера
ENV NGINX_PORT=80

# Указываем, что сервер прослушивает порт NGINX_PORT
EXPOSE $NGINX_PORT

