FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app/api

COPY ./requirements.txt /app/api/requirements.txt
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install -r /app/api/requirements.txt

COPY ./src /app/api

RUN adduser -D user
USER user

EXPOSE 8001
