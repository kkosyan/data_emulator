FROM ubuntu:trusty
FROM python:3.10
WORKDIR /src/

RUN python3.10 -m venv venv
COPY pyproject.toml .
RUN venv/bin/pip install .
ENV PATH="/src/venv/bin:$PATH"
RUN apt-get update && apt-get install -y postgresql
COPY . .
