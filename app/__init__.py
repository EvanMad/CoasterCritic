from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager.init_app(app)

from app import views, models
