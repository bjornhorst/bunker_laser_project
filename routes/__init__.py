from flask import Blueprint

blueprint = Blueprint('my_blueprint', __name__)

from . import login
from . import page
from . import register
from . import admin