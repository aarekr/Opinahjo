from application import db

class Lasku(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    numero = db.Column(db.Integer, nullable=False)

    def __init__(self, numero):
        self.numero = numero
        self.maksettu = False
