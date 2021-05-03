# Backend

The backend for this web application was built using [Django](https://www.djangoproject.com/).

> Using the PostgreSQL database.

Dependencies:

```sh
django-cors-headers
djangorestframework
psycopg2
testfixtures
```

Install requirements:

```sh
pip install -r requirements.txt
```

Makemigrations:

```sh
python manage.py makemigrations app
```

Migrate:

```sh
python manage.py migrate
```

Run the server:

```sh
python manage.py runserver
```

Running tests:

```sh
python manage.py test app
```
