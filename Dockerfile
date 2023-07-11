FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ARG TOKEN
ENV TOKEN=$TOKEN
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt