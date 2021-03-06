FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app

COPY ./backend/ /app/
RUN pip install pip==22.1

RUN pip install -r requirements.txt

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB test_django_db