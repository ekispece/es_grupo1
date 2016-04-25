from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask("pictosoft", static_folder='website', static_url_path='')
mongo = PyMongo(app)
