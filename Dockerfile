# Стартовый образ
FROM python:3.12.1-alpine3.19

# Установка рабочего каталога
WORKDIR /usr/src/ttinv

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка необходимых пакетов
RUN apk update \
    && apk add --no-cache postgresql-client build-base postgresql-dev libpq-dev

# Обновление pip и установка зависимостей
RUN pip install --upgrade pip
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

# Копирование исходного кода
COPY . .

# Копирование скрипта entrypoint
COPY entrypoint.sh /usr/src/ttinv/entrypoint.sh
EXPOSE 8000

# Создание директорий для статических и медиафайлов
RUN mkdir -p /usr/src/ttinv/static /usr/src/ttinv/media

# Создание пользователя и установка прав
RUN adduser -D ttinv \
    && chown -R ttinv:ttinv /usr/src/ttinv \
    && chmod +x /usr/src/ttinv/entrypoint.sh

# Переключение на нового пользователя
USER ttinv

# Установка точки входа
ENTRYPOINT ["sh", "/usr/src/ttinv/entrypoint.sh"]
