from flask import Blueprint, render_template, redirect, url_for, flash, request
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import *
from .models import *
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html', form=LoginForm())

# Handles login form POST requests
@auth.route('/login', methods=["POST"])
def login_post():

    # Gather form data from form request
    name = request.form.get('name')
    password = request.form.get('password')

    # Find if user exists in database, check credentials, then handle acordingly
    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.password, password):
        flash('Wrong username and/or password, please try again')
        return redirect(url_for('auth.login'))
    login_user(user)
    return redirect(url_for('main.profile'))

# Handle signup form GET requests, returns signup form page
@auth.route('/signup')
def signup():
    return render_template('signup.html', form=SignupForm())

# Handle signup POST requests from form
@auth.route('/signup', methods=['POST'])
def signup_post():
    # Gather form data
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first()
    # Check user exists
    if user:
        flash("User already exists, please signup with a different username")
        return redirect(url_for('auth.signup'))
    # Add user to db
    new_user = User(name=name, password=generate_password_hash(
        password, method='pbkdf2:sha256'))
    db.session.add(new_user)
    db.session.commit()
    flash("added to db")
    return redirect(url_for('auth.login'))

# Log user out using flask_login()
@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
