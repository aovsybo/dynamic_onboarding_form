# Описание
Сервис онбординга с учетом выбора пользователя и динамическим отображением вопросов. Приложение позволяет добавлять информацию о своем заведении в анкету с полями, динамически формирующимися на основании предыдущих ответов.

# Используемые технологии
- Python
- Django
- PostgreSQL
- Docker, docker compose
- poetry

# Запуск
Для запуска необходимо:
1. Скопировать к себе приложение:
```shell
git clone https://github.com/aovsybo/dynamic_onboarding_form
```
2. В корень добавить .env файл
3. Запустить docker-контейнер
```shell
docker compose up --build
```

# Пример работы
## Админ-панель
Создаем суперюзера:
```shell
pytohn manage.py createsuperuser
```
Авторизовываемся в админ-панели по адресу:
http://0.0.0.0:8000/admin/
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/b116b161-627b-4898-9ed7-5fbb4ab0c5de)

## Клиентский интерфейс 
