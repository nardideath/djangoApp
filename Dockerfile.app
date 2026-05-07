FROM python:3.12.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN export CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apt-get update
RUN apt-get -y install sed attr dialog bash bash-doc bash-completion grep nano net-tools iputils-ping sshpass
RUN apt-get -y install libffi-dev gcc python3-dev python3-pip musl-dev libssl-dev cargo make rsync build-essential postgresql-server-dev-all

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
