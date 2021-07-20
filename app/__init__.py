from flask import Flask

app = Flask(__name__)

from app.controllers import *
from app.controllers import bp_users
app.register_blueprint(bp_users)