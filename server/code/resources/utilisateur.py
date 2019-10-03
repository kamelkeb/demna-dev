from flask_restful import Resource, reqparse
from models.utilisateur import Utilisateur
import datetime

class UtilisateurDAO(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('nom',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('prenom',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('pseudo',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('motdepasse',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('numtelephone',
                        type=str,
                        required=False,
                        help="Champ facultatif"
                        )
    parser.add_argument('image',
                        type=str,
                        required=False,
                        help="Champ facultatif"
                        )
    parser.add_argument('role',
                        type=int,
                        required=False,
                        help="Champ facultatif"
                        )
    parser.add_argument('suspendu',
                        type=bool,
                        required=False,
                        help="Champ facultatif"
                        )

    def get(self):
        usersJSON = list(map(lambda x: x.json(), Utilisateur.query.all()))
        if usersJSON:
            return {'Utilisateurs': usersJSON}, 201
        return {'message': 'Utilisateurs introuvables.'}, 500

    def post(self):
        data = UtilisateurDAO.parser.parse_args()

        if Utilisateur.find_by_name(data['pseudo']):
            return {"message": "Ce pseudo est déjà pris."}, 400

        user = Utilisateur(
            data['email'], 
            data['nom'], 
            data['prenom'], 
            data['pseudo'], 
            data['motdepasse'], 
            data['numtelephone'], 
            data['image'], 
            data['role'] or 1, 
            data['suspendu'] or False, 
            datetime.datetime.now(), 
            datetime.datetime.now()
            )
        user.save_to_db()

        return {"message": "Le compte utilisateur a bien été créé."}, 201
