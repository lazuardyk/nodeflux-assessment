from app.models.users import Users
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from . import bp_users


auth = HTTPBasicAuth()

users = {
    "staffname": generate_password_hash("stafftoken")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@bp_users.route('/api/vips', methods = ['GET'])
def getvips():
    userModel = Users()
    allUsers = [user for user in userModel.getAllUsers()]
    for document in allUsers:
        document['_id'] = str(document['_id'])
    return {'ok':True, 'data':allUsers, 'message': 'Successfully get all data.'}

@bp_users.route('/', methods = ['GET'])
def index():
    return "Hello World!"


