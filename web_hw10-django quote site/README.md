## Usage: choose one from two scenarios:
### 1. First:
  - Run postgres docker container with command:

        docker run --name postg_wh10 -d -h localhost -p 5432:5432 -u postgres -e POSTGRES_PASSWORD=1234567 postgres
  - Make migrations by executing two commands from \hw10\ path

        py manage.py makemigrations
    
        py manage.py migrate
  - Runserver from \hw10\ path:

        py manage.py runserver
  - Visit localhost:8000/
    
### 2. Second:
  - Run postgres docker container with command:

        docker run --name postg_wh10 -d -h localhost -p 5432:5432 -u postgres -e POSTGRES_PASSWORD=1234567 postgres
  - Run mongoDb docker container with command:

        docker run --name mongo_wh10 -d -p 27017:27017 mongo
  - Make migrations by executing two commands from \hw10\ path

        py manage.py makemigrations
    
        py manage.py migrate
  - Create database mongoDb manually with name 'hw10' and first table 'authors'
  - Import authors.json to 'authors' table manually
  - Execute \WEB_HW10\hw10\utils\add_quotes_to_mongo.py for creating and filling the 'quotes' table with quotes.json
  - Execute \WEB_HW10\hw10\utils\migrate_from_mongo.py for migration all data from mongoDb to postgresDb
  - Runserver from \hw10\ path:

        py manage.py runserver
  - Visit localhost:8000/


## Python web #10

У минулій домашній роботі ви виконували скрапінг сайту http://quotes.toscrape.com.
Вам необхідно самостійно реалізувати аналог такого сайту на Django.

## Основне завдання:
  1. Реалізуйте можливість реєстрації на сайті та вхід на сайт.
  2. Можливість додавання нового автора на сайт лише для зареєстрованого користувача.
  3. Можливість додавання нової цитати на сайт із зазначенням автора тільки для зареєстрованого користувача.
  4. Виконайте міграцію бази даних із MongoDB, яка у вас є, у Postgres для вашого сайту. Можна реалізувати кастомним скриптом. (За бажанням можете залишити та працювати з цитатами та авторами в MongoDB, а з користувачами у Postgres)
  5. Можна зайти на сторінку кожного автора без автентифікації користувача
  6. Усі цитати доступні для перегляду без автентифікації користувача

## Додаткова частина:

  1. Реалізуйте пошук цитат за тегами. При натисканні на тег, виводиться список цитат з цим тегом.
  2. Реалізуйте блок "Top Ten tags" та виведення найпопулярніших тегів.
  3. Реалізуйте пагінацію. Це кнопки next та previous
  4. Замість перенесення даних з бази даних MongoDB, реалізуйте можливість скрапінгу даних прямо з вашого сайту по натисканню певної кнопки на формі та наповнення бази даних сайту.
