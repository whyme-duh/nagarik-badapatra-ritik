FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY ./requirements.txt /app/


COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
ENV PORT=10000
EXPOSE 10000

RUN chmod +x build.sh


# Start the Django application
CMD ["/bin/bash", "-c", "./build.sh && python manage.py collectstatic --noinput && gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT"]




