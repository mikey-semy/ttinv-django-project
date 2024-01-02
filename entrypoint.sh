#!/bin/sh
echo "RUN ENTRYPOINT"
if [ "$DATABASE" = "postgres" ]
then
    # если база еще не запущена
    echo "Рано..."
    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "Пора!"
fi
# Выполняем миграции *удалить создание миграций в дальнейшем
echo "MAKE MIGRATIONS"
python manage.py makemigrations
echo "MIGRATE"
python manage.py migrate
echo "END ENTRYPOINT"

exec "$@"
