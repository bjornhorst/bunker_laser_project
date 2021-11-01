from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import Video
main = Blueprint('main', __name__)
@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/videos' ,methods=["GET"])
@login_required
def videos():
    video_data = Video.query.all()
    #title="test title"
    return render_template('videos.html', video_data=video_data)

@main.route('/parsePython')
@login_required
def parsePython():
    return render_template('parsePython.html', name=current_user.name)