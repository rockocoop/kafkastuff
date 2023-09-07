FROM python:latest

RUN useradd reconx && mkdir /scripts && chown -R reconx /scripts && chmod -R 755 /scripts

COPY kafka_producer.py /scripts/
COPY requirements.txt /scripts/
RUN cd /scripts && pip install -r requirements.txt 

USER reconx
