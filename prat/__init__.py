#!/usr/bin/env pythpn3
# -*- coding: utf-8 -*-
import os
import plenty_api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prat.config import config
import keyring

from typing import Any
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('prat').version
except DistributionNotFound:
    __version__ = '(local)'

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)

# Laden der Konfiguration basierend auf Umgebungsvariable (z.B., 'development' oder 'production')
config_name = os.environ.get('FLASK_ENV', 'development')

if config_name == 'development':
    dev="DEV_"
else:
    dev=""
if config_name == 'development': 
    dev="DEV_" 
else: 
    dev=""


app.config.update({
    'DB__HOST':     os.environ[f'{dev}DB__HOST'],
    'DB__DBNAME':   os.environ[f'{dev}DB__NAME'],
    'DB__USER':     os.environ[f'{dev}DB__USER'],
    'DB__PASSWORD': os.environ[f'{dev}DB__PASSWORD'],
    'DB__ENGINE':   os.environ[f'{dev}DB__ENGINE'],
    })


app.config.update({'SQLALCHEMY_DATABASE_URI': app.config.get('DB__ENGINE')})
app.debug = os.environ['PRAT_DEBUG']
DEBUG = os.environ['PRAT_DEBUG']
PRAT_API_CONN = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

def main(prat_base_url,prat_login_method,prat_data_format):
    global PRAT_API_CONN
    plenty = plenty_api.PlentyApi(
        base_url=prat_base_url,
        login_method=prat_login_method,
        data_format=prat_data_format
    )

    if 'Authorization' in plenty.creds.keys():
        PRAT_API_CONN = True


@app.context_processor
def utility_processor():
    global PRAT_API_CONN
    return dict(prat_mode=os.environ['FLASK_ENV'], prat_debug=os.environ['PRAT_DEBUG'], prat_conn=PRAT_API_CONN)

# Definieren Sie Ihre Modelle (z.B., Item und Listing) hier mit SQLAlchemy
from prat.models import Item

# Definieren Sie Ihre Routen hier
from prat import routes

# Load Application logic
from prat import runtime

if __name__ == 'prat':
    logging.debug('Open RESTApi connection')
    main(os.environ['PRAT_BASE_URL'], os.environ['PRAT_LOGIN_MODE'], os.environ['PRAT_DATA_OUT'])
    logging.debug('Loading runtime')
    runtime.logic()    
    #app.run()