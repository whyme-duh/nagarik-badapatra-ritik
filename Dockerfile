FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY ./requirements.txt /app/


COPY . /app/

RUN pip install -r requirements.txt && python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the Django application
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

