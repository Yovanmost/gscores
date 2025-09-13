#!/bin/bash
# Exit immediately if any command fails
set -e

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

# (Optional) Reset DB – WARNING: this deletes all data!
python manage.py flush --noinput

# Seed students from your CSV
python manage.py seed_students dataset/diem_thi_thpt_2024.csv

# Start the app with Gunicorn, binding to Render’s port
gunicorn gscores.wsgi:application --bind 0.0.0.0:$PORT
