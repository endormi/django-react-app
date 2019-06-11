# Backend

The backend for this web application was built using [Django](https://www.djangoproject.com/). This handles the API related to this web app.

Currently the database that I use is sqlite3, but I might change it to PostgreSQL later on.

Install requirements:

```
pip install -r requirements.txt
```

Migrate:

```
py manage.py migrate
```

Run the server:

```
py manage.py runserver
```

> I used [postman](https://www.getpostman.com/) to test the API

Test API using **Postman's** GET request

```
http://127.0.0.1:8000/api/
```
