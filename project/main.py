from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/videos')
@login_required
def videos():
    return render_template('videos.html', name=current_user.name)

@main.route('/parsePython')
@login_required
def parsePython():
    return render_template('parsePython.html', name=current_user.name)