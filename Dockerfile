FROM python:3.6.2-slim

USER tracking
WORKDIR /srv/idiet-tracking

COPY requirements.txt .
COPY idiet_tracking .
RUN pip install \
        -r requirements.txt \
        gunicorn

env PYTHONPATH /srv/idiet-tracking
CMD --workers=4 idient_tracking.wsgi:create_app
ENTRYPOINT gunicorn
