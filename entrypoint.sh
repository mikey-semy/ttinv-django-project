#!/bin/sh
echo "RUN ENTRYPOINT"
if [ "$DATABASE" = "postgres" ]
then
    # если база еще не запущена
    echo "База данных ещё не запущена..."
    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "Запущена, продолжаем..."
fi
# Выполняем миграции *удалить создание миграций в дальнейшем
echo "Создаем миграции..."
python manage.py makemigrations
echo "Мигрируем..."
python manage.py migrate
echo "Создаем суперпользователя"
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
python manage.py loaddata business_card/fixtures/ttinv_brands.json
python manage.py loaddata business_card/fixtures/ttinv_benefits.json
python manage.py loaddata business_card/fixtures/ttinv_delivery.json
python manage.py loaddata business_card/fixtures/ttinv_products.json
python manage.py loaddata business_card/fixtures/ttinv_requisites.json

echo "END ENTRYPOINT"
exec "$@"
