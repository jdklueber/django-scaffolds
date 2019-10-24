# django-scaffolds

## In order for this to work, you need to create a .env file defining the following variables:

```
SECRET_KEY=somesecretkeyhere
DEBUG=True
ALLOWED_HOSTS=localhost

# DB
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
```

It might be worth it to remove the manage.py file, and call django-admin startproject yourprojectname, copy the secret key into your .env file, delete ./yourprojectname, and rename ./project to ./yourprojectname.
