FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1


WORKDIR /app

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./core /app

