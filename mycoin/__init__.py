#coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from config import config

app = Flask(__name__,static_url_path='/static')
config_name = 'default'
app.config.from_object(config[config_name])
toolbar = DebugToolbarExtension(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'

from api import api
app.register_blueprint(api,url_prefix='/api')

from List import List
app.register_blueprint(List,url_prefix='/List')
