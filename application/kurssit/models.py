from application import db

class Kurssi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    enrolled = db.Column(db.Boolean, nullable=False) # kurssipaikan varaus
#    done = db.Column(db.Boolean, nullable=False) # suoritettu

#    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
#                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.enrolled = False # kurssipaikka ei varattu
#        self.done = False # suoritettu
