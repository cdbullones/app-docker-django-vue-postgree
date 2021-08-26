FROM python:3.6-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /code

ADD ./requirements.txt /code

RUN pip install -r requirements.txt

COPY . /code/

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]


