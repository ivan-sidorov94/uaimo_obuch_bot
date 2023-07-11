FROM python:3.10

WORKDIR /uaimo_obuch_bot

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY . ./uaimo_obuch_bot

RUN pip install --upgrade pip
RUN pip install -r requirements.txt