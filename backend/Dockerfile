# INSTALL PYTHON IMAGE
FROM python:3.6-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

COPY scripts/start.sh /

RUN pip install -r requirements.txt

COPY . /code/



