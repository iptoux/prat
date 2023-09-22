# PlentyRESTApiTools

[![PRAT CodeCheck](https://github.com/iptoux/prat/actions/workflows/git_action_prat.yml/badge.svg)](https://github.com/iptoux/prat/actions/workflows/git_action_prat.yml)

Web-Application to control/administrate REST-API of Plenty Markets

## Setup/Run

```bash
# install project requirements
poetry install

# starting web application
poetry run waitress-serve --threads=1 --listen=0.0.0.0:8080 runner:app
```

## Docker

```bash
# building docker image from latest state
docker build --pull --rm -f "Dockerfile" -t prat:v0.1.0 "."

# run docker image/container
docker run --detach 'prat'
```

## ToDo

- [ ] #1 
- [ ] https://github.com/iptoux/prat/milestone/1