from application import db
from application.models import Base

class Kurssi(Base):

    name = db.Column(db.String(144), nullable=False)
    enrolled = db.Column(db.Boolean, nullable=False) # kurssipaikan varaus

#    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
#                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.enrolled = False # kurssipaikka ei varattu
