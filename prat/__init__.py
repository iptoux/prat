#!/usr/bin/env pythpn3
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prat.config import config

from typing import Any

app = Flask(__name__)

# Laden der Konfiguration basierend auf Umgebungsvariable (z.B., 'development' oder 'production')
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.context_processor
def utility_processor():
    return dict(prat_mode=app.config.get('PRAT_MODE'), prat_debug=app.config.get('DEBUG'))

# Definieren Sie Ihre Modelle (z.B., Item und Listing) hier mit SQLAlchemy
from prat.models import Item

# Definieren Sie Ihre Routen hier
from prat import routes

# Load Application logic
from prat import runtime

if __name__ == '__main__':
    runtime.logic()
    app.run()