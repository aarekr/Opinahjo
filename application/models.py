from application import db

enrollments = db.Table('enrollments', 
    db.Column('kurssi_id', db.Integer, db.ForeignKey('kurssi.id'), primary_key=True), 
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
)

class Base(db.Model): # Kurssi, User

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
