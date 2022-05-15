FROM python:3.10.4-alpine3.15

COPY ./requirements.txt /source/requirements.txt

RUN : \
    && pip3 install -r /source/requirements.txt \
    && :

COPY . /source/
WORKDIR /source/

CMD uvicorn main:app --host 0.0.0.0 --port 8000
