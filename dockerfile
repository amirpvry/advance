FROM python:3.12.1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1


WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./core /app

