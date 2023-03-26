FROM python:3.11.2-slim as base

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN-FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

COPY pyproject.toml /usr/src/app/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR /usr/src/app/frontend

COPY docker-entrypoint.sh .

CMD ["./docker-entrypoint.sh"]
