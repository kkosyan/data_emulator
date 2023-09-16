FROM python:3.10
WORKDIR /src/

RUN python3.10 -m venv venv
COPY pyproject.toml .
RUN venv/bin/pip install .
ENV PATH="/opt/cupis/venv/bin:$PATH"
COPY . .
