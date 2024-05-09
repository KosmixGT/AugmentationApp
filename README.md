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

Идея приложения: пользователь загружает свои изображения в веб-сервис, настраивает параметры аугментации. После этого данные аугментируются и пользователь получает созданные программой изображения в zip архиве.

## Техническое задание группового проекта

Для реализации проекта нужно выполнить определенные задачи. Каждая задача требует определенных знаний технологий и была поручена соответствующему исполнителю в группе.

| №   | Задача                          | Стек                | Исполнитель           |
| --- | ------------------------------- | ------------------- | --------------------- |
|  1  | Создание Pipeline               | git                 | Ивакин Александр      |
|  2  | Разработка и развертывание БД   | PostgreSQL          | Ивакин Александр      |
|  3  | Развертывание Docker            | Docker              | Гоголев Денис         |
|  4  | Разработка FrontEnd             | Vue                 | Все                   |
|  5  | Разработка BackEnd              | FastApi, Python     | Все                   |
|  6  | Разработка сервиса аугментации  | Python              | Дробот Максим         |
|  7  | Сборка и визуализация метрик    | Grafana, Prometeus  | Мехоношин Константин  |

## Разработка
### 1. Git
Использована технология ветвления **GitFlow**:

 <img src="/images/04_Hotfix_branches.svg" width="600" height="500"> 

Источник: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

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

### 2. Технология CI/CD
**Этапы Pipeline**:
- **build** - сборка docker контейнеров
- **test** - тестирование приложения (unit-тесты)
- **deploy** - запуск контейнеров на сервере

variables

### 3. Технология Docker
dockerfile
dockercompose
dockerignore
