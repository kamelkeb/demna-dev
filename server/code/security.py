from werkzeug.security import safe_str_cmp
from models.utilisateur import Utilisateur


def authenticate(usremail, password):
    user = Utilisateur.find_by_email(usremail)
    # print('Found user : ', user)
    if user and safe_str_cmp(user.motdepasse, password):
        #turnaround with the id attribute expected by flask-jwt
        #(- as used initialy in method UserModel.find_by_id -)#
        user.id = user.email
        return user


def identity(payload):
    # print('Payload : ', payload)
    user_id = payload['identity']
    return Utilisateur.find_by_email(user_id)
