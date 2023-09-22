# PlentyRESTApiTools

[![PRAT CodeCheck](https://github.com/iptoux/prat/actions/workflows/git_action_prat.yml/badge.svg)](https://github.com/iptoux/prat/actions/workflows/git_action_prat.yml)

<p align="center" width="100%">
<img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/iptoux/prat/git_action_prat.yml?style=for-the-badge">
    <img src="https://img.shields.io/github/package-json/v/iptoux/prat?style=for-the-badge" title="GitHub package.json version">
    <img src="https://img.shields.io/github/directory-file-count/iptoux/prat/prat?style=for-the-badge" title="GitHub repo file count (file extension)">
    <img src="https://img.shields.io/github/languages/code-size/iptoux/prat?style=for-the-badge" title="GitHub code size in bytes">
    <img src="https://img.shields.io/github/issues/iptoux/prat?style=for-the-badge" title="GitHub issues">
    <img alt="GitHub License" src="https://img.shields.io/github/license/iptoux/prat?style=for-the-badge" title="GitHub license">
    <img src="https://img.shields.io/github/package-json/keywords/iptoux/prat?style=flat-square" title="GitHub package.json dynamic"> 
</p>

![GitHub](https://img.shields.io/github/license/iptoux/prat)

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

## ToDo (first)

- [ ] #1 
- [ ] https://github.com/iptoux/prat/milestone/1