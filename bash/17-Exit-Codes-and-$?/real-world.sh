#!/bin/bash

echo 'git pull origin main'

if [ $? -ne 0 ]; then
    echo "Git pull failed. Deployment stopped."
    exit 1
fi

echo 'pip install -r requirements.txt'

if [ $? -ne 0 ]; then
    echo "Dependency installation failed."
    exit 1
fi

echo 'python manage.py migrate'

if [ $? -ne 0 ]; then
    echo "Migration failed."
    exit 1
fi

echo 'sudo systemctl restart gunicorn'

echo "Deployment successful!"

