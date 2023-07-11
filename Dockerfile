FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /bot
COPY . /bot


RUN pip install --upgrade pip
RUN pip install -r requirements.txt