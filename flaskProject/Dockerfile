FROM python:3.7-alpine
MAINTAINER Eder Costa

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers
RUN apk add gcc
RUN apk add --no-cache libressl-dev musl-dev libffi-dev

RUN apk del libressl-dev \
        musl-dev \
        libffi-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app
