from db import db


class Role(db.Model):
    __tablename__ = 'role'

    idrole = db.Column(db.Integer, primary_key=True)
    nomrole = db.Column(db.String(80), nullable=False)
    peuxmodutilisateur = db.Column(db.Boolean, nullable=False, server_default=False)
    peuxsupprutilisateur = db.Column(db.Boolean, nullable=False, server_default=False)
    peuxmodappel = db.Column(db.Boolean, nullable=False, server_default=False)
    peuxsupprappel = db.Column(db.Boolean, nullable=False, server_default=False)

    def __init__(self, nomrole, peuxmodutilisateur, peuxsupprutilisateur, peuxmodappel, peuxsupprappel):
        self.nomrole = nomrole
        self.peuxmodutilisateur = peuxmodutilisateur
        self.peuxsupprutilisateur = peuxsupprutilisateur
        self.peuxmodappel = peuxmodappel
        self.peuxsupprappel = peuxsupprappel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
