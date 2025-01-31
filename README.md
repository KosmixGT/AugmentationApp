# AugmentationApp

## Групповой проект

- **Название проекта**: «AugmentationApp»

- **Команда**: 
    - Гоголев Денис, 
    - Дробот Максим, 
    - Ивакин Александр, 
    - Мехоношин Константин
- **Цель работы**: создание приложения для аугментации изображений.

## Описание группового проекта

Аугментация данных – методика создания дополнительных данных из уже имеющихся. Используется при решении задач компьютерного зрения, для повышения разнообразия данных и устранения дисбаланса между классами в обучающем наборе данных. 

Идея приложения: пользователь загружает свои изображения в веб-сервис и настраивает параметры аугментации. На переданные данные применяются алгоритмы аугментации: поворот, добавление шума, изменение яркости и контраста. После чего пользователь получает обработанные алгоритмом изображения в zip архиве.

## Техническое задание группового проекта

Для реализации проекта нужно выполнить определенные задачи. Каждая задача требует определенных знаний технологий и была поручена соответствующему исполнителю в группе.

| №   | Задача                          | Стек                | Исполнитель           |
| --- | ------------------------------- | ------------------- | --------------------- |
|  1  | Создание Pipeline               | git                 | Все                   |
|  2  | Разработка и развертывание БД   | PostgreSQL          | Ивакин Александр      |
|  3  | Развертывание Docker            | Docker              | Гоголев Денис         |
|  4  | Разработка FrontEnd             | Vue                 | Все                   |
|  5  | Разработка BackEnd              | FastApi, Python     | Все                   |
|  6  | Разработка сервиса аугментации  | Python              | Дробот Максим         |
|  7  | Сборка и визуализация метрик    | Grafana, Prometheus | Мехоношин Константин  |
|  8  | Запуск на сервере               | Nginx               | Гоголев Денис         |

## Разработка
### 1. Git
Использована технология ветвления **GitFlow**:

 <img src="/images/04_Hotfix_branches.svg" width="600" height="500"> 

*Источник: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow*

**Список веток**:
- **main** - ветка для релизов
- **developer** - отходит от **main**, ветка для разработки
- **feature** - отходит от **developer**, ветка для разработки отдельных функций
- **release** - отходит от **developer** и мерджится в **main**, ветка для доработки текущей версии проекта до релиза
- **fix** - отходит от** main**, ветка для исправления багов в релизе

**Именование коммитов (префиксы)**:
- **feature** - разработка отдельных функций
- **fix** - исправление багов
- **update** - доработка отдельных функций
- **docs** - изменение документации

**gitignore** - использовался для исключения из коммитов установленных зависимостей и конфиденциальных данных

---
### 2. Технология CI/CD
**Этапы pipeline**:
- **build** - сборка docker контейнеров
- **test** - тестирование приложения (unit-тесты)
- **deploy** - запуск контейнеров на сервере

**Использованные теги**:
- **stage/stages** - указание этапов 
- **variables** - переменные
- **script** - выполняемые команды
- **tags** - указание этапов для **job**
- **rules (if, when)** - правила запуска

**Переменные окружения в GitLab**:
- **Docker_HUB_PASSWORD** - пароль от Dockerhub аккаунта для доставки контейнеров на сервер
- **DB_CONNECTION** - строка подключения к базе данных

---
### 3. Технология Docker
Написание *dockerfile* для сборки контейнеров сервера и клиента.

**Использованные теги в dockerfile**:
- **FROM** - указание базового образа
- **LABEL** - описание контейнера
- **RUN** - запуск команд внутри контейнера
- **WORKDIR** - указание рабочей директории внутри контейнера
- **COPY** - копирование файлов в контейнер
- **ARG** - указание параметров для передачи в команду **build**
- **ENV** - указание переменных окружения
- **EXPOSE** - указание, какой порт прослушивается внутри контейнера
- **ENTRYPOINT** - указание базовой команды
- **CMD** - указание команды
- **AS** - применяется для **multi-stage building**

Написание *docker-compose* для запуска приложения на сервере.

**Использованные теги в docker-compose**:
- **version** - указание версии docker-compose
- **services** - список контейнеров
- **image** - указание образа для запуска контейнера
- **ports** - указание проброса портов внутрь контейнера
- **command** - выполняемая при запуске контейнера команда
- **depends_on** - ожидание запуска другого контейнера
- **environment** - переменные окружения
- **volumes** - монтирование разделов внутрь контейнера

**Для оптимизации и безопасности использовались**:
- **multi-stage building** - позволяет скомпилировать приложение в одном контейнере, а результат поместить в другом
- **dockerignore** - блокирует копирование ненужных и конфиденциальных файлов внутрь контейнера

---
### 4. Дополнительные фичи
1. Настройка своего сервера на основе **Debian**
2. Установка своего **shell runner**
3. Настройка проксирования запросов на **Nginx**
4. Настройка развертывания отдельного тестового стенда
5. Настройка мониторинга через **Prometheus** и **Grafana**
