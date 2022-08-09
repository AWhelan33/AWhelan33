from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ



app = Flask(__name__)

app.config['SECRET_KEY'] = '1b064c160927c6c15dc21e1098928560'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///site.db'

db = SQLAlchemy(app)

from appone import routes