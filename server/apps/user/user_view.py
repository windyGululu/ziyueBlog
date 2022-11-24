
from flask import Blueprint
from .model import User

user = Blueprint('User', __name__, url_prefix='/customer/user')



@user.route('/login', methods=['GET'])
def user_login():
    user = User(
        username="nickname",
        age=12,
    )
    user.save() 
    return 'user login'