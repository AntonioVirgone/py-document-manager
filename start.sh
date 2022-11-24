#!/bin/zsh
while getopts ':p:' arg; do
  case $arg in
    p) HTTP_PORT=$OPTARG;;
  esac
done

if [[ -v HTTP_PORT ]]; then
  echo -e "listening on provided port \e[1m$HTTP_PORT\e[0m"
  echo
else
  HTTP_PORT=8080
  echo -e "listening on standard port \e[1m$HTTP_PORT\e[0m: use start.sh -p \e[1mport\e[0m to change it"
  echo
fi

python manage.py runserver $HTTP_PORT