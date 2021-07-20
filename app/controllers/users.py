from app.models.users import Users
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from . import bp_users
from flask import request


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
    try:
        userModel = Users()
        allUsers = [user for user in userModel.getAllUsers()]
        for document in allUsers:
            document['_id'] = str(document['_id'])
        return {'ok':True, 'data':allUsers, 'message': 'Successfully get all data.'}
    except:
        return {'ok':False, 'message': 'Something wrong.'}

@bp_users.route('/api/vips', methods = ['POST'])
def addvips():
    try:
        name = request.form['name']
        country_of_origin = request.form['country_of_origin']
        eta = request.form['eta']
        photo = request.form['photo']
        attributes = request.form['attributes']
        arrived = False
        userModel = Users()
        userModel.addUser(name, country_of_origin, eta, photo, arrived, attributes)
        return {'ok': True, 'message': 'Successfully saving the data.'}
    except:
        return {'ok':False, 'message': 'Something wrong.'}

@bp_users.route('/api/vips/<user_id>', methods = ['GET'])
def getvip(user_id):
    try:
        userModel = Users(user_id)
        userInfo = userModel.getSelfInformation()
        userInfo['_id'] = str(userInfo['_id'])
        return {'ok':True, 'data':userInfo, 'message': 'Successfully get the data.'}
    except:
        return {'ok':False, 'message': 'Something wrong.'}

@bp_users.route('/api/vips/<user_id>', methods = ['PUT'])
def updatevip(user_id):
    try:
        userModel = Users(user_id)
        name = request.form['name']
        country_of_origin = request.form['country_of_origin']
        eta = request.form['eta']
        photo = request.form['photo']
        attributes = request.form['attributes']
        userModel.updateUser(name, country_of_origin, eta, photo, attributes)
        return {'ok':True, 'message': 'Successfully update the user.'}
    except:
        return {'ok':False, 'message': 'Something wrong.'}

@bp_users.route('/api/vips/<user_id>/arrived', methods = ['PATCH'])
def updatevip(user_id):
    try:
        userModel = Users(user_id)
        arrived = request.form['arrived']
        userModel.updateArrived(arrived)
        return {'ok':True, 'message': 'Successfully update the user.'}
    except:
        return {'ok':False, 'message': 'Something wrong.'}

@bp_users.route('/', methods = ['GET'])
def index():
    return "Hello World!"


