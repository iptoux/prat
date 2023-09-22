FROM python:3.11.5

LABEL maintainer="iptoux, iptoux@gmail.com"
LABEL version="0.1.0"

WORKDIR /flaskapp

ENV PYTHONUNBUFFERED=1
ENV DOCKER=True

RUN apt update && apt upgrade -y
RUN apt install gnupg ca-certificates git

COPY pyproject.toml pyproject.toml
COPY runner.py runner.py
ADD prat /flaskapp/prat
COPY poetry.lock poetry.lock
COPY README.md README.md
COPY .env.example .env.example

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --without dev
RUN poetry self add poetry-dotenv-plugin

EXPOSE 5000

CMD [".venv/bin/python3","-m","waitress","--listen","0.0.0.0:5000","runner:app"]