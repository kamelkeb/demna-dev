from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity

# from resources.item import Item, ItemList
from resources.utilisateur import UtilisateurDAO
from resources.appelaudon import AppelaudonDAO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

# api.add_resource(Item, '/item/<string:name>')
api.add_resource(AppelaudonDAO, '/api/appels')
api.add_resource(UtilisateurDAO, '/api/utilisateurs')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
