from os.path import dirname, basename, isfile, join
import glob
from flask import Blueprint

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__  = [ basename(f)[:-3] for f in modules if  isfile(f) and  not f.endswith('__init__.py')]

bp_users = Blueprint('users', __name__, url_prefix='/')