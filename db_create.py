from app import db, app
from config import SQLALCHEMY_DATABASE_URI
import os.path

with app.app_context():
    db.create_all()