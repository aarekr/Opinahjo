from application import db
from application.models import Base
from application.models import enrollments
from application.kurssit.models import Kurssi
from sqlalchemy.sql import text

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

    @staticmethod
    def teacher_info():
        stmt = text("SELECT Account.id, Account.name, Account.student FROM Account")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "student":row[2]})

        return response

    @staticmethod
    def teacher_my_total_courses():
        stmt = text("SELECT Kurssi.id, Kurssi.name FROM Kurssi "
                    "LEFT JOIN Account ON Account.id = Account.id ")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def school_total_courses_offered():
        stmt = text("SELECT COUNT(Kurssi.id) FROM Kurssi")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"course_count":row[0]})
        return response
