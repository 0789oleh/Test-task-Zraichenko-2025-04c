# 🥗 Lunch Voting Backend

Django REST API for internal service which helps.

## 🚀 Technology stack

* Django Rest Framework
* JWT
* PostgreSQL
* Docker
* Pytest

## Installtion

Download or clone this repo. Navigate to folder
`cd ./lunch_decider`

To build the application type the
`docker-compose build .`
`docker-compose run web python manage.py migrate`
`docker-compose run web python manage.py createsuperuser`

The application will be running at http://localhost:8000
