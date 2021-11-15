from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from project import app
from . import db
import os
from .models import Video
from .models import User
from werkzeug.utils import secure_filename
admin = Blueprint('admin', __name__)

UPLOAD_FOLDER = 'project/static/videos'
ALLOWED_EXTENSIONS = {'mp4'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin.route("/admin", methods=['GET'])
@login_required
def adminPanel():
    video_data = Video.query.all()
    user_data = User.query.all()
    return render_template('admin/admin.html', video_data=video_data, user_data=user_data);

# @admin.route("/admin/create", methods=['GET'])
# @login_required
# def create():
#     return render_template('admin/create.html');

@admin.route("/admin/edit/video/<id>", methods=['POST'])
@login_required
def edit_video(id):
    video = Video.query.get(id)
    video.title = request.form.get('title')
    db.session.commit()
    return redirect(f'/admin/edit/video/{id}')
    #return render_template('admin/editVideoPunten.html')

@admin.route("/admin/edit/video/<id>", methods=['GET'])
@login_required
def edit_video_get(id):
    video = Video.query.get(id)
    return render_template('admin/editVideoPunten.html', id=id ,title=video.title, beschrijving=video.beschrijving, file=video.href, videoPunten=video.videoPunten)

@admin.route("/admin/video/<id>/punten/edit/", methods=['POST'])
@login_required
def video_punten_edit_post(id):
    videoPunten = request.form.get('punten')
    flash(f'{id} = aangepast')
    return redirect('/admin')


@admin.route("/admin/edit/user/<id>", methods=['POST'])
@login_required
def edit_user(id):
    flash(f"Gelukt! Gegvens zijn aangepast")
    user = User.query.get(id)
    user.name = request.form.get('name')
    db.session.commit()
    return redirect(url_for('admin.adminPanel'))

@admin.route("/admin/create", methods=['POST'])
@login_required
def create_post():
    title = request.form.get('title')
    beschrijving = request.form.get('beschrijving')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template('admin/admin.html', error="Bestand mag niet worden geupload")
        file = request.files.get('file')
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return render_template('admin/admin.html', error="Selecteer een bestand")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = 'videos/' + filename

            new_video = Video(title=title, beschrijving=beschrijving, href=path)
            # add the new video to the database
            db.session.add(new_video)
            db.session.commit()
            return render_template('admin/videoPunten.html', path=path, title=title, beschrijving=beschrijving)


    return render_template('admin/admin.html');

@admin.route("/admin/delete/<id>", methods=['POST'])
@login_required
def delete_video(id):
    flash(f"Gelukt! De video is verwijderd")
    video_id = Video.query.filter_by(id=id).one()
    path = "project/static/"+ video_id.href
    print(path)
    os.remove(path)

    db.session.delete(video_id)
    db.session.commit()
    return redirect(f'/admin')