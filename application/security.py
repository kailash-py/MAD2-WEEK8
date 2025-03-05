# all import and configs related to security
from flask_jwt_extended import JWTManager
from .model import User

jwt = JWTManager() # create an instance of the JWTManager
@jwt.user_identity_loader  # decorator to specify the function that will be used to load the identity of the user
def load(user):
    return user.username

@jwt.user_lookup_loader  # decorator to loads the user object from the database to Token
def user_lookup(_jwt_header, jwt_data):
    identity = jwt_data["sub"]                                     # get the identity of the user from the jwt_data
    return User.query.filter_by(username=identity).one_or_none()    # return the user object if the user exists, otherwise return None