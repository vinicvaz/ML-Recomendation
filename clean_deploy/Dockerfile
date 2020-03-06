FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        cmake \
        build-essential \
        gcc \
        g++
RUN pip install -r requirements.txt
RUN python db_starter.py

# $PORT is set by heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
