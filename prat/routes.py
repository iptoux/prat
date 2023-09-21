#!/usr/bin/env pythpn3
# -*- coding: utf-8 -*-

from prat import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Implementieren Sie die Logik für die Items-Seite
    return render_template('dashboard.html')

@app.route('/items')
def items():
    # Implementieren Sie die Logik für die Items-Seite
    pass

@app.route('/listings')
def listings():
    # Implementieren Sie die Logik für die Listings-Seite
    pass

@app.route('/search/<int:item_id>')
def search(item_id):
    # Implementieren Sie die Logik für die Suche nach item_id
    pass