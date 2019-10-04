from db import db


class Appelaudon(db.Model):
    __tablename__ = 'appelaudon'

    idappelaudon = db.Column(db.Integer, primary_key=True)
    fkidutilisateur = db.Column(db.Integer, db.ForeignKey(u'utilisateur.idutilisateur'), nullable=False)
    caracterisationbiologique = db.Column(db.String(255), nullable=False)
    quantiteattendue = db.Column(db.Integer, nullable=False)
    lieudecollecte = db.Column(db.String(1024), nullable=False)
    calendriercollecte = db.Column(db.String(1024), nullable=False)
    motifetdescription = db.Column(db.String(1024))
    priorite = db.Column(db.Integer, nullable=False)
    contactsubst = db.Column(db.String(1024))
    statut = db.Column(db.Integer, nullable=False)
    datecreation = db.Column(db.DateTime, nullable=False)
    datemodification = db.Column(db.DateTime, nullable=False)

    utilisateur = db.relationship(u'Utilisateur')

    def __init__(self, fkidutilisateur, caracterisationbiologique, quantiteattendue, lieudecollecte, calendriercollecte, motifetdescription, priorite, contactsubst, statut, datecreation, datemodification):
        self.fkidutilisateur = fkidutilisateur
        self.caracterisationbiologique = caracterisationbiologique
        self.quantiteattendue = quantiteattendue
        self.lieudecollecte = lieudecollecte
        self.calendriercollecte = calendriercollecte
        self.motifetdescription = motifetdescription
        self.priorite = priorite
        self.contactsubst = contactsubst
        self.statut = statut
        self.datecreation = datecreation
        self.datemodification = datemodification

    def json(self):
        return {'fkidutilisateur': self.fkidutilisateur,
                'caracterisationbiologique': self.caracterisationbiologique,
                'quantiteattendue': self.quantiteattendue,
                'lieudecollecte': self.lieudecollecte,
                'calendriercollecte': self.calendriercollecte,
                'motifetdescription': self.motifetdescription,
                'priorite': self.priorite,
                'contactsubst': self.contactsubst,
                'statut': self.statut,
                'datecreation': str(self.datecreation),
                'datemodification': str(self.datemodification)}

    @classmethod
    def find_by_usrid(cls, _usrid):
        return cls.query.filter_by(fkidutilisateur=_usrid).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
