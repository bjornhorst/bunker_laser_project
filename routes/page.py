# blueprint_module\page.py

from . import blueprint

@blueprint.route("/test", methods=['GET'])
def hello():
  return 'hello world'
