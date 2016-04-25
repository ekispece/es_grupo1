from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask("pictosoft")
mongo = PyMongo(app)
