FROM python:3.8

WORKDIR /usr/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app/requirements.txt /usr/requirements.txt

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /usr/requirements.txt

COPY . /usr/
