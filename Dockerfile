# syntax=docker/dockerfile:1
# https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/

FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install pipenv

WORKDIR /serwer

COPY Pipfile /serwer/
RUN pipenv install

COPY . /serwer/

CMD pipenv run python manage.py runserver 0.0.0.0:8080

