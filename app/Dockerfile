FROM python:3.10-slim

MAINTAINER Dmitriy Begishev 'mintdragon@yandex.ru'

RUN apt-get update -y

# RUN apt-get install -y python-pip python-dev

COPY . /app

WORKDIR /app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "main.py"]

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

# FROM python:3.10-slim
#
# WORKDIR /
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt --no-cache-dir
# COPY . .
# CMD ["uvicorn", "src/main:app", "--host", "0.0.0.0"]