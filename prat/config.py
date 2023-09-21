#!/usr/bin/env pythpn3
# -*- coding: utf-8 -*-

import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRAT_DATA_OUT = 'dataframe'                     # json/dataframe
    PRAT_LOGIN_MODE = 'keyring'                     # keyring (cache pw), direct
    PRAT_PORT = 8080                                # web control port

class DevelopmentConfig(Config):
    PRAT_MODE = 'devel'
    PRAT_BASE_URL = ''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    PRAT_MODE = 'prod'
    PRAT_BASE_URL = ''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://prat:p4ssw0rd@localhost/prat'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}