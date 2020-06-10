from application import app
from flask import render_template, request
from application.auth.models import User

@app.route("/laskut/")
def show_invoices():
    courses_and_enrollments_count = User.courses_and_enrollments_count()
    student_enrollments_count = User.student_enrollments_count()
    return render_template("laskut/kaikkilaskut.html", 
        courses_and_enrollments_count=courses_and_enrollments_count, 
        student_enrollments_count=student_enrollments_count
    )
