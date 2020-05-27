from application import db
from application.models import Base
from application.models import enrollments
from application.kurssit.models import Kurssi

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    student = db.Column(db.Boolean, nullable=False)
    teacher = db.Column(db.Boolean, nullable=False)

    enrollments = db.relationship('Kurssi', secondary=enrollments, lazy='subquery', backref=db.backref('users', lazy=True))

    def __init__(self, name, username, password, student, teacher):
        self.name = name
        self.username = username
        self.password = password
        self.student = student
        self.teacher = teacher

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
