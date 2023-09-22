# PlentyRESTApiTools

[![PRAT GitHub Actions](https://github.com/iptoux/prat/actions/workflows/git_action_prat.yml/badge.svg)](https://github.com/iptoux/prat/actions/workflows/git_action_prat.yml)

WebAplication to control/administrate RESPApi of PlentyMarkets

## Setup/Run

```bash
poetry install
poetry run waitress-serve --threads=1 --listen=0.0.0.0:8080 runner:app
```

## Docker

```bash
docker build --pull --rm -f "Dockerfile" -t prat:v0.1.0 "."
docker run --detach 'prat'
```

## ToDo

- [ ] #1 
- [ ] https://github.com/iptoux/prat/milestone/1