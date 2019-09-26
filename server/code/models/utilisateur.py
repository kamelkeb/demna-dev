from db import db


class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'

    idutilisateur = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(30), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    pseudo = db.Column(db.String(30), nullable=False)
    motdepasse = db.Column(db.String(30), nullable=False)
    numtelephone = db.Column(db.String(15))
    image = db.Column(db.String(50))
    role = db.Column(db.Integer, nullable=False)
    suspendu = db.Column(db.Boolean, nullable=False)
    datecreation = db.Column(db.DateTime, nullable=False)
    datemodification = db.Column(db.DateTime, nullable=False)


    def __init__(self, email, nom, prenom, pseudo, motdepasse, numtelephone, image, role, suspendu, datecreation, datemodification):
        self.email = email
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.motdepasse = motdepasse
        self.numtelephone = numtelephone
        self.image = image
        self.role = role
        self.suspendu = suspendu
        self.datecreation = datecreation
        self.datemodification = datemodification

    def json(self):
        return {'email': self.email, 
                'nom': self.nom, 
                'prenom': self.prenom, 
                'pseudo': self.pseudo, 
                'motdepasse': self.motdepasse, 
                'numtelephone': self.numtelephone, 
                'image': self.image, 
                'role': self.role, 
                'suspendu': self.suspendu, 
                'datecreation': self.datecreation, 
                'datemodification': self.datemodification}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(nom=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(idutilisateur=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
