FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt