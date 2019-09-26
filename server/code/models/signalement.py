from db import db


class Signalement(db.Model):
    __tablename__ = 'signalement'

    idsignalement = db.Column(db.Integer, primary_key=True)
    fkidappelaudon = db.Column(db.Integer, server_default=NULL)
    fkidutilisateursignale = db.Column(db.Integer, server_default=NULL)
    fkidutilisateursignalant = db.Column(db.Integer, db.ForeignKey(u'utilisateur.idutilisateur'), nullable=False)
    commentairesignalant = db.Column(db.String(1024), server_default=NULL)
    statutmoderation = db.Column(db.Integer, nullable=False)
    datecreation = db.Column(db.DateTime, nullable=False)
    datemodification = db.Column(db.DateTime, nullable=False)

    utilisateur = db.relationship(u'Utilisateur')

    def __init__(self, idappelaudon, idutilisateursignale, idutilisateursignalant, commentairesignalant, statutmoderation, datecreation, datemodification):
        self.idappelaudon = idappelaudon
        self.idutilisateursignale = idutilisateursignale
        self.idutilisateursignalant = idutilisateursignalant
        self.commentairesignalant = commentairesignalant
        self.statutmoderation = statutmoderation
        self.datecreation = datecreation
        self.datemodification = datemodification

    def json(self):
        return {'idappelaudon': self.idappelaudon,
                'idutilisateursignale': self.idutilisateursignale,
                'idutilisateursignalant': self.idutilisateursignalant,
                'commentairesignalant': self.commentairesignalant,
                'statutmoderation': self.statutmoderation,
                'datecreation': self.datecreation,
                'datemodification': self.datemodification}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(idsignalement=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
