from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.appelaudon import Appelaudon
import datetime


class AppelaudonDAO(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('fkidutilisateur',
                        type=int,
                        required=True,
                        help="Chaque appel doit avoir un idutilisateur."
                        )
    parser.add_argument('caracterisationbiologique',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('quantiteattendue',
                        type=int,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('lieudecollecte',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('calendriercollecte',
                        type=str,
                        required=True,
                        help="Champ obligatoire!"
                        )
    parser.add_argument('motifetdescription',
                        type=str,
                        required=False,
                        help="Champ facultatif"
                        )
    parser.add_argument('priorite',
                        type=int,
                        required=True,
                        help="Champ obligatoire avec valeur par défaut!"
                        )
    parser.add_argument('contactsubst',
                        type=str,
                        required=False,
                        help="Champ facultatif"
                        )
    parser.add_argument('statut',
                        type=int,
                        required=False,
                        help="Champ obligatoire avec valeur par défaut!"
                        )

    # @jwt_required()
    # def get(self, name):
    #     item = ItemModel.find_by_name(name)
    #     if item:
    #         return item.json()
    #     return {'message': 'Item not found'}, 404

    @jwt_required()
    def get(self):
        aadsJSON = list(map(lambda x: x.json(), Appelaudon.query.all()))
        if aadsJSON:
            return {'Appels aux dons': aadsJSON}, 201
        return {'message': 'Appels aux dons introuvables.'}, 500

    def post(self):
        data = AppelaudonDAO.parser.parse_args()

        dateBuild = datetime.datetime.now()
        aad = Appelaudon( 
                    data['fkidutilisateur'], 
                    data['caracterisationbiologique'], 
                    data['quantiteattendue'], 
                    data['lieudecollecte'], 
                    data['calendriercollecte'], 
                    data['motifetdescription'], 
                    data['priorite'], 
                    data['contactsubst'], 
                    data['statut'], 
                    dateBuild,
                    dateBuild
                    )

        try:
            aad.save_to_db()
        except:
            return {"message": "Une erreur est survenue à l'enregistrement de cet appel."}, 500

        return aad.json(), 201

    def delete(self, id):
        aad = Appelaudon.find_by_id(id)
        if aad:
            aad.delete_from_db()
            return {'message': 'Appel au don supprimé.'}
        return {'message': 'Appel au don introuvable.'}, 404

    def put(self, id):
        data = AppelaudonDAO.parser.parse_args()

        aad = Appelaudon.find_by_id(id)

        if aad:
            aad.caracterisationbiologique = data['caracterisationbiologique']
        else:
            aad = Appelaudon(id, **data)

        aad.save_to_db()

        return aad.json()


# class ItemList(Resource):
#     def get(self):
#         return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
