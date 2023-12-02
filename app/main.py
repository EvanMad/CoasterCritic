from flask import Blueprint, render_template, redirect, url_for, flash, request
from . import db
from flask_login import login_required, current_user
from . import models

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # Redirect to view_profile with current_user.id as user_id
    return redirect(url_for('main.view_profile', user_id=current_user.id))

@main.route('/rollercoaster/<rc_id>')
def rollercoaster_page(rc_id):
    #rc = get_coaster(rc_id)
    rc = models.Rollercoaster.query.filter_by(id=rc_id).first()
    print(rc.name)
    return render_template('rollercoaster.html', rc=rc, user=user, rollercoaster=rollercoaster)


@main.route('/404')
def four_o_four():
    return render_template('404.html')

@main.route('/review/<review_id>')
def review_page(review_id):
    db_query = (
        db.session.query(models.Review, models.Rollercoaster, models.User)
        .join(models.Rollercoaster, models.Review.rollercoaster_id == models.Rollercoaster.id)
        .join(models.User, models.Review.user_id == models.User.id)
        .filter(models.Review.id == review_id)
        .all()
    )[0]
    review = db_query[0]
    if review:
        rollercoaster = db_query[1]
        user = db_query[2]
        return render_template('review.html', review=review, user=user, rollercoaster=rollercoaster)
    return redirect(url_for('main.four_o_four'))

@main.route('/profile/<user_id>')
def view_profile(user_id):
    user = models.User.query.get(user_id)
    if user:
        # Use a join to fetch reviews along with associated rollercoaster data
        db_query = (
            db.session.query(models.Review, models.Rollercoaster)
            .join(models.Rollercoaster, models.Review.rollercoaster_id == models.Rollercoaster.id)
            .filter(models.Review.user_id == user_id)
            .all()
        )
        return render_template('profile.html', user=user, reviews=db_query)
    else:
        return redirect(url_for('main.four_o_four'))


@main.route('/add_review', methods=['POST'])
def add_review():
    pass