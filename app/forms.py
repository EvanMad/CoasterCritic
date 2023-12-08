from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, ValidationError, SelectField, TextAreaField
from wtforms.validators import DataRequired
from .db_manager import *

from . import db
from . import models

class LoginForm(FlaskForm):
    name = FloatField('name', validators=[DataRequired()])
    password = StringField('password', validators=[
        DataRequired()])

class SignupForm(FlaskForm):
    name = FloatField('name', validators=[DataRequired()])
    password = StringField('password', validators=[
        DataRequired()])

class ReviewForm(FlaskForm):
    rating = FloatField('rating', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    rollercoaster = SelectField('rollercoaster', validators=[DataRequired()])
