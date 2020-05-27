from application import db
from application.models import Base
from application.models import enrollments

class Kurssi(Base):

    name = db.Column(db.String(144), nullable=False)
    enrolled = db.Column(db.Boolean, nullable=False)  # kurssipaikan varaus
    completed = db.Column(db.Boolean, nullable=False) # kurssi suoritettu

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    enrollments = db.relationship('User', secondary=enrollments, lazy='subquery', backref=db.backref('kurssit', lazy=True))

    def __init__(self, name):
        self.name = name
        self.enrolled = False
        self.completed = False
