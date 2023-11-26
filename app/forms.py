from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, ValidationError
from wtforms.validators import DataRequired

from .db_manager import *


class LoginForm(FlaskForm):
    name = FloatField('name', validators=[DataRequired()])
    password = StringField('password', validators=[
        DataRequired()])


class SignupForm(FlaskForm):
    name = FloatField('name', validators=[DataRequired()])
    password = StringField('password', validators=[
        DataRequired()])
