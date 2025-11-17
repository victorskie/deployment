#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status.
set -e
 
# 1. Install dependencies
pip install -r requirements.txt
 
# 2. Run Django static files collection
python manage.py collectstatic --noinput
 
# 3. Apply database migrations
python manage.py makemigrations 
python manage.py migrate