from flask import Blueprint, render_template
from flask_login import login_required
from . import db

admin = Blueprint('admin', __name__)

@admin.route("/admin", methods=['GET'])
@login_required
def adminPanel():
    return render_template('admin/admin.html');
