from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
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

    #SEC.BUG: les données utilisateurs ne devraient pas être produits ici
    #SEC.DE.BUG.TODO: ne pas retourner les données utilisateur vers le front...
    @jwt_required()
    def get(self):
        usersJSON = list(map(lambda x: x.json(), Utilisateur.query.all()))
        if usersJSON:
            return {'Utilisateurs': usersJSON}, 201
        return {'message': 'Utilisateurs introuvables.'}, 500

    def post(self):
        data = UtilisateurDAO.parser.parse_args()

        if Utilisateur.find_by_email(data['email']):
            return {"message": "Cet email existe déjà."}, 400

        #SEC.BUG: 'role' et 'suspendu' ne devraient pas être mappés ici
        #SEC.DE.BUG.TODO: ne pas générer des comptes admin depuis le front...
        dateBuild = datetime.datetime.now()
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
            dateBuild, 
            dateBuild
            )
        user.save_to_db()

        return {"message": "Le compte utilisateur a bien été créé."}, 201
