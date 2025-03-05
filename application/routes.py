from flask import current_app as app, jsonify, request
from .model import User
from flask_jwt_extended import create_access_token,  jwt_required, current_user

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).one_or_none()