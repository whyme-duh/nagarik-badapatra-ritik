#!/usr/bin/env bash

set -o errexit


pip install --no-cache-dir -r requirements.txt


python manage.py collectstatic --no-input

python manage.py migrate

python create_super_user.py