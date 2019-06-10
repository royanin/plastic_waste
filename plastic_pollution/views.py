from flask import render_template, flash, redirect, session, url_for, request, g, json, jsonify, send_from_directory, make_response
from plastic_pollution import plastic_pollution
from urllib.parse import urlencode, quote_plus
import os, re
from config import basedir

@plastic_pollution.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@plastic_pollution.errorhandler(500)
def internal_error(error):
    return render_template('500.html')

@plastic_pollution.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

