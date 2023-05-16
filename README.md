Stack:

Django

GraphQL(graphene)

PostgresQL

nginx

Docker

redis

celery

In order for the project to compile in Docker you need 2 env files.

.env

=========================================================
SECRET_KEY = 'django-insecure-***'

###### # SECRET_KEY you can get using a generator (search in Google)

EMAIL_USER = '***'

###### # EMAIL_USER is for smtp mail, enter your login here and password below

EMAIL_PASSWORD = '***'

DEBUG=1

DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=notion
SQL_USER=notion
SQL_PASSWORD=notion
SQL_HOST=notion_postgres
SQL_PORT=5432
DATABASE=postgres

NGINX_EXTERNAL_PORT=80

========================================================

.env.db

=========================================================
POSTGRES_USER=notion
POSTGRES_PASSWORD=notion
POSTGRES_DB=notion

=========================================================

Docker commands

docker-compose up -d --build

docker-compose -f docker-compose.yml exec notion_project python manage.py makemigrations

docker-compose -f docker-compose.yml exec notion_project python manage.py migrate

docker-compose -f docker-compose.yml exec notion_project python manage.py collectstatic --no-input --clear

docker-compose -f docker-compose.yml exec notion_project python manage.py createsuperuser

docker-compose down -v
