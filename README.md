# django-scaffolds

This repo is intended to serve as a basis for new django projects.  By using this scaffolding, you're starting off with:

* Pipenv dependency management
* A decent .gitignore
* Custom user model
* Postgres integration
* Docker integration + some courtesy scripts to assist with listing logs, restarting/rebuilding the container. running unit tests...
* User registration
* Static file mappings
* Template file mappings
* Bootstrap 4 + crispy forms integration

If you want to use allauth for additional authentication or have transactional emails etc, that is left up to you to implement.

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
