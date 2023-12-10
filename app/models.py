from . import db
from flask_login import UserMixin

# review_association = db.Table(
#     'review_association',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('rollercoaster_id', db.Integer, db.ForeignKey('rollercoaster.id')),
#     db.Column('rating', db.Float),  # Add additional fields as needed
#     db.PrimaryKeyConstraint('user_id', 'rollercoaster_id')
# )

# User and Rollercoaster are a many-to-many relationship. Review is used to bridge the gap between them.


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    # Remove the explicit backref definition
    reviews = db.relationship('Review', lazy=True, back_populates='user')


class Rollercoaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    year = db.Column(db.Integer)
    height = db.Column(db.Float)
    length = db.Column(db.Float)
    manufacturer = db.Column(db.String(100))
    model = db.Column(db.String(100))
    inversions = db.Column(db.Integer)
    speed = db.Column(db.Float)

    reviews = db.relationship('Review', lazy=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rollercoaster_id = db.Column(db.Integer, db.ForeignKey('rollercoaster.id'), nullable=False)
    rating = db.Column(db.Float)
    review_text = db.Column(db.String(400))
    likes = db.Column(db.Integer)

    user = db.relationship('User', backref=db.backref('user_reviews', lazy=True))
    rollercoaster = db.relationship('Rollercoaster', backref=db.backref('coaster_reviews', lazy=True))
