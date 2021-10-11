# blueprint_module\page.py
from flask import render_template
from . import blueprint

@blueprint.route("/admin", methods=['GET'])
def admin():
    return render_template('admin/admin.html');
