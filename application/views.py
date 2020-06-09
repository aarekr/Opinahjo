from flask import render_template
from application import app, db
from application.auth.models import User, Kurssi
from flask_login import login_required, current_user


# etusivu
@app.route("/")
def index():
    return render_template("index.html")

# käyttäjän henk.koht sivu - Minun kurssit, Minun opetus
@app.route('/user/<usernimi>')
@login_required
def user(usernimi):
    user = User.query.filter_by(username=usernimi).first_or_404()
    teacher_info = User.teacher_info()
    teacher_my_courses = User.teacher_my_courses()
    student_my_courses = User.student_my_courses()
    all_enrollments = User.all_enrollments()
    student_enrollments_count = User.student_enrollments_count()

    if user.id != current_user.id:
        return "Et voi tarkastella toisen käyttäjän tietoja!"

    return render_template('user.html', user=user, 
        teacher_info=teacher_info, 
        teacher_my_courses=teacher_my_courses, 
        student_my_courses=student_my_courses, 
        all_enrollments=all_enrollments, 
        student_enrollments_count=student_enrollments_count
    )
