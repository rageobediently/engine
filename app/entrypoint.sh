#!/usr/bin/env sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres not yet run"

    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "Postgres did run"
fi

# Выполняем миграции
python manage.py migrate

exec "$@"
