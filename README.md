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

Панель добавления объектов:
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/b8c4562e-ca95-4c2d-b588-e75c8546a6b0)

Добавляем типы заведений: <br>
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/ae230496-f042-4c72-b640-a1c43d69fbf2)

Добавляем вопросы для каждого из типов:
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/db248926-53f6-4342-9f8d-22e141efeb4e)

## Клиентский интерфейс 
Переходим по адресу для заполнения формы:
http://0.0.0.0:8000/
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/d500a4c4-3aaa-4884-86c9-df76b429f3d5)

Вводим данные:
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/08bb73e7-602b-47cc-bb31-5c62b898a846)

Получаем список вопросов по данному типу заведения:
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/21d8b00d-266c-4abb-93fe-5bd079ed1cff)

Добавляем:
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/955a12c7-4831-4a95-aab0-2fe5e9fa7d1e)

Получаем список всех заведений:
![image](https://github.com/aovsybo/dynamic_onboarding_form/assets/66824112/53c30a88-b1ac-4adc-ae12-1adebc88c805)



