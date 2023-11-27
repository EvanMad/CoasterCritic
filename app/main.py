from flask import Blueprint, render_template
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
    return render_template('profile.html', name=current_user.name)

@main.route('/rollercoaster/<rc_id>')
def rollercoaster_page(rc_id):
    #rc = get_coaster(rc_id)
    rc = models.Rollercoaster.query.filter_by(id=rc_id).first()
    print(rc.name)
    return render_template('rollercoaster.html', rc=rc)