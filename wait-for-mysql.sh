#!/bin/bash

echo "Waiting for mysql"
until mysql -h"$DB_HOST" -P"$DB_PORT" -uroot -p"$DB_PASSWORD" &> /dev/null
do
  printf "."
  sleep 1
done

echo -e "\nmysql ready"
exec $cmd