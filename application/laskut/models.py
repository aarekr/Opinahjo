from application import db
from application.models import Base

class Invoice(Base):

    kurssi_id = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, kurssi_id):
        self.kurssi_id = kurssi_id
        self.paid = False
