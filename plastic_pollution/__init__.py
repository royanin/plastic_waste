from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import os
from config import basedir


plastic_pollution = Flask(__name__)
plastic_pollution.config.from_object('config')

from plastic_pollution import views

#Setup logging
if not plastic_pollution.debug:
    #Check if log directory already exists, otherwise create:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/plastic_pollution.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    plastic_pollution.logger.addHandler(file_handler)

    plastic_pollution.logger.setLevel(logging.INFO)
    plastic_pollution.logger.info('MITx_search startup...')