from application import db
from application.models import Base
from application.models import enrollments, userinvoices
from application.kurssit.models import Kurssi
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    student = db.Column(db.Boolean, nullable=False)
    teacher = db.Column(db.Boolean, nullable=False)
    user_role = db.Column(db.String(80))

    enrollments = db.relationship('Kurssi', secondary=enrollments,  backref=db.backref('users', lazy=True))
    userinvoices = db.relationship('Invoice', secondary=userinvoices, backref=db.backref('users', lazy=True))

    def __init__(self, name, username, password, student, teacher, user_role):
        self.name = name
        self.username = username
        self.password = password
        self.student = student
        self.teacher = teacher
        self.user_role = user_role

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_user_role(self):
        return self.user_role

    def roles(self):
        return ["ADMIN"]

    @staticmethod # opettajan näkemä opiskelijalista
    def teacher_info(): # Minun opetus, user.html
        stmt = text("SELECT Account.id, Account.name, Account.student "
                    "FROM Account")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "student":row[2]})

        return response

    @staticmethod # opettajan opettamat kurssit
    def teacher_my_courses(): # Minun opetus, user.html
        stmt = text("SELECT Kurssi.id, Kurssi.name, Kurssi.account_id "
                    "FROM Kurssi "
                    "LEFT JOIN Account ON Account_id = Account.id ")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "teacher":row[2]})

        return response

    @staticmethod # kurssien lkm
    def school_total_courses_offered(): # Opetusohjelma, list.html
        stmt = text("SELECT COUNT(Kurssi.id) FROM Kurssi")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"course_count":row[0]})
        return response

    @staticmethod # opettajien lkm
    def school_teachers_total(): # Opetusohjelma, list.html
        stmt = text("SELECT COUNT(Account.id) FROM Account WHERE Account.teacher = 1")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"teacher_count":row[0]})
        return response

    @staticmethod # yhteenveto: kurssit ja opettajat
    def courses_and_teachers(): # Opetusohjelma, list.html
        stmt = text("SELECT Kurssi.id, Kurssi.name, Kurssi.start_date, Kurssi.end_date, Account.name "
                    "FROM Kurssi, Account "
                    "WHERE Kurssi.account_id = Account.id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "kurssi":row[1], "start_date":row[2], "end_date":row[3], "opettaja":row[4]})
        return response

    @staticmethod # opiskelijan kurssi-ilmoittautumiset
    def student_my_courses(): #  Minun kurssit, user.html
        stmt = text("SELECT Kurssi.id, Kurssi.name, Account.name "
                    "FROM Account, Kurssi, Enrollments "
                    "WHERE Account.id = Enrollments.account_id "
                    "AND Kurssi.id = Enrollments.kurssi_id "
                    "ORDER BY Kurssi.name")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "kurssi":row[1], "student":row[2]})
        return response

    @staticmethod # kaikki opiskelijat, mille kurssille ilmoittautunut, opettaja-id
    def all_enrollments():
        stmt = text("SELECT Account.name, Kurssi.name, Kurssi.account_id "
                    "FROM Kurssi, Account, enrollments "
                    "WHERE Account.id=enrollments.account_id AND Kurssi.id=enrollments.kurssi_id "
                    "ORDER BY Kurssi.name")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"student":row[0], "course":row[1], "teacher":row[2]})
        return response

    @staticmethod # opiskelijat ja heidän ilmoittautumismäärät
    def student_enrollments_count():
        stmt = text("SELECT Account.id, Account.name, COUNT(Kurssi.id), Account.student "
                    "FROM Account "
                    "LEFT JOIN enrollments ON Account.id=enrollments.account_id "
                    "LEFT JOIN Kurssi ON Kurssi.id=enrollments.kurssi_id "
                    "GROUP BY Account.id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "count":row[2], "student":row[3]})
        return response

    @staticmethod # kaikki kurssit ja ilmoittautumismäärät
    def courses_and_enrollments_count():
        stmt = text("SELECT Kurssi.name, COUNT(Account.id) "
                    "FROM Account, Kurssi, enrollments "
                    "WHERE Kurssi.id=enrollments.kurssi_id AND Account.id=enrollments.account_id "
                    "GROUP BY Kurssi.id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"course":row[0], "count":row[1]})
        return response

    @staticmethod # kaikki laskut
    def all_invoices(): # allinvoices.html
        stmt = text("SELECT Invoice.id, Invoice.kurssi_id, Invoice.paid, Invoice.account_id, Account.name "
                    "FROM Invoice, Account "
                    "WHERE Invoice.account_id = Account.id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "kurssi_id":row[1], "paid":row[2], "account_id":row[3], "student_name":row[4]})
        return response
