# Backend

The backend for this web application was built using [Django](https://www.djangoproject.com/). This handles the API related to this web app.

Currently the database that I use is sqlite3, but I might change it to PostgreSQL later on.

Install requirements:

```shell
pip install -r requirements.txt
```

Migrate:

```python
py manage.py migrate
```

Run the server:

```python
py manage.py runserver
```
