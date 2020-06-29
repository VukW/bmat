FROM python:3.7-alpine
LABEL maintaner="vykukushkin@gmail.com"

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /django_project
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .