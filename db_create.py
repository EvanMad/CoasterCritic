from app import db, app
from config import SQLALCHEMY_DATABASE_URI
import os.path
import csv
from app.models import *
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()

    with open("rollercoaster_data.csv") as f:
        reader = csv.DictReader(f)
        next(reader)
        for row in reader:
            print(row)
            rc = Rollercoaster(
                name = row['name'],
                year = row['year'],
                height = row['height'],
                length = row['length'],
                manufacturer = row['manufacturer'],
                model = row['model'],
                inversions = row['inversions'],
                speed = row['speed']
            )
            db.session.add(rc)
            db.session.commit()
    
    root = User(name="evanwpm", password=generate_password_hash("root", method='pbkdf2:sha256'))
    db.session.add(root)
    db.session.commit()