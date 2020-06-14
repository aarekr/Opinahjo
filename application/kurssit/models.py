from application import db
from application.models import Base
from application.models import enrollments
from sqlalchemy.sql import text

class Kurssi(Base):

    name = db.Column(db.String(144), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
