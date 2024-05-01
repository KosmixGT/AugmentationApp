# Образ для Node.js с DockerHub
FROM node:alpine3.18

# Создаём рабочую директорию
WORKDIR /app

COPY vite-version.txt ./

# Устанавливаем зависимости
RUN npm install vite@$(cat vite-version.txt)

# Копируем список зависимостей в package.json и package-lock.json в рабочую директорию
#COPY package*.json ./
COPY package.json ./

# Копируем сборку на сервер
# Здесь вообще должна быть публикация на AWS хостинг
COPY dist/. dist/

# Указываем, что сервер прослушивает порт 5000
EXPOSE 5000

# Задаём базовую команду
ENTRYPOINT ["npm", "run", "preview"]

# Передаём аргументы - порт сервера
CMD ["5000"]