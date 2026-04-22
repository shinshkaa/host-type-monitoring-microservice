FROM python:3.12-slim

ENV TZ=Europe/Moscow

RUN pip3 install prometheus_client

WORKDIR /app/microservice/
COPY *.py /app/microservice/

ENTRYPOINT [ "python3", "main.py" ]
