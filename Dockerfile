FROM python:3.10-slim

MAINTAINER Dmitriy Begishev 'mintdragon@yandex.ru'

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y

EXPOSE 8000

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

WORKDIR .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
