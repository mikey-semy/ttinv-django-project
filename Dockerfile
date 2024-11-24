# Стартовый образ
FROM python:3.12.1-alpine3.19

WORKDIR /usr/src/ttinv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-client build-base postgresql-dev libpq-dev

RUN pip install --upgrade pip
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY . .
COPY entrypoint.sh /usr/src/ttinv/entrypoint.sh
EXPOSE 8000

RUN mkdir -p /usr/src/ttinv/static
RUN mkdir -p /usr/src/ttinv/media

RUN chown -R 1000:1000 /usr/src/ttinv/media
RUN chmod +x /usr/src/ttinv/entrypoint.sh
RUN adduser --disabled-password ttinv
USER ttinv

ENTRYPOINT ["sh", "/usr/src/ttinv/entrypoint.sh"]