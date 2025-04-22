# 🥗 Lunch Voting Backend

Django REST API for internal service which helps.

## 🚀 Technology stack

* Django Rest Framework
* JWT
* PostgreSQL
* Docker
* Pytest

## Installtion

Download or clone this repo. Then type cd ./lunch_decider and type

docker-compose up --build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser

The application will be running at http://ocalhost:8000