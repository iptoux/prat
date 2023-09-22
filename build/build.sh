#!/usr/bin/env bash

mkdir dist

echo "Adding build depencies"
poetry self add poetry-bumpversion

echo "Linting source for errors"
poetry run flake8 . > dist/source.lint

echo "Checking source for vulns"
poetry run bandit -r . -c "pyproject.toml" > dist/source.vuln

echo "Building docker image"
docker build --pull --rm -f "Dockerfile" -t prat:v0.1.0 "."