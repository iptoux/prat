# PlentyRESTApiTools

WebAplication to control/administrate RESPApi of PlentyMarkets

## Setup/Run

```bash
poetry install
poetry run waitress-serve --threads=1 --listen=0.0.0.0:8080 runner:app
```

## Docker

```bash
docker build --tag 'prat' .
docker run --detach 'prat'
```
