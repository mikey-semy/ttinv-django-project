# Стартовый образ
FROM python:3.12.1-alpine3.19


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt
RUN pip install --upgrade pip
RUN apk add postgresql-client build-base postgresql-dev libpq-dev
RUN pip install -r /temp/requirements.txt



COPY . /usr/src/ttinv
WORKDIR /usr/src/ttinv
EXPOSE 8000

RUN mkdir -p $WORKDIR/static
RUN mkdir -p $WORKDIR/media

RUN adduser --disabled-password ttinv
USER ttinv

ENTRYPOINT ["/usr/src/ttinv/entrypoint.sh" ]