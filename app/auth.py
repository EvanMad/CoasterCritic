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


@auth.route('/login', methods=["POST"])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.password, password):
        flash('wrong')
        return redirect(url_for('auth.login'))
    login_user(user)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html', form=SignupForm())


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first()
    print(user)
    if user:
        flash("user exists")
        return redirect(url_for('auth.signup'))
    new_user = User(name=name, password=generate_password_hash(
        password, method='pbkdf2:sha256'))

    db.session.add(new_user)
    db.session.commit()
    flash("added to db")
    return redirect(url_for('auth.login'))

@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
