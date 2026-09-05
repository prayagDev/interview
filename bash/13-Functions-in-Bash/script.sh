#!/bin/bash

restart_server() {
    echo "Restarting server..."
    echo 'sudo systemctl restart gunicorn'
}

run_migrations() {
    echo "Running migrations..."
    echo 'python manage.py migrate'
}

run_migrations
restart_server

