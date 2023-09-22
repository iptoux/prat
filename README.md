<p align="center" width="100%">
<img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/iptoux/prat/build-setup.yml?style=flat-square" title="PRAT Build - Setup">
<img src="https://img.shields.io/github/package-json/v/iptoux/prat?style=flat-square" title="GitHub package.json version">
<img src="https://img.shields.io/github/languages/code-size/iptoux/prat?style=flat-square" title="">
<img src="https://img.shields.io/github/directory-file-count/iptoux/prat/prat?style=flat-square" title="">
<img src="https://img.shields.io/github/issues/iptoux/prat?style=flat-square" title="">
<img src="https://img.shields.io/github/license/iptoux/prat?style=flat-square" title="GitHub package.json version">
    <img src="https://img.shields.io/github/package-json/keywords/iptoux/prat?style=flat-square" title="GitHub package.json dynamic"> 
</p>

---

# PlentyRESTApiTools

Web-Application to control/administrate REST-API of Plenty Markets

## Setup/Run

```bash
# install project requirements
pip3 install poetry

# clone repo, setup app
git clone https://github.com/iptoux/prat.git
poetry install

# starting web application
poetry run waitress-serve --threads=1 --listen=0.0.0.0:8080 runner:app
```

## Docker

```bash
# clone repo
git clone https://github.com/iptoux/prat.git

# building docker image from latest state
docker build --pull --rm -f "Dockerfile" -t prat:v0.1.0 "."

# run docker image/container
docker run --detach 'prat'
```

## ToDo (first)

- [ ] [#1]
- [ ] Add delight to the experience when all tasks are complete :tada: