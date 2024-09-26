#!/usr/bin/env bash

set -e

host="mysql-db"


until mysql -h "$host" -u root -proot -e "SELECT 1"; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 5
done

>&2 echo "MySQL is up - executing command"
exec "$@"

