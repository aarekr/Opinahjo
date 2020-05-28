from flask import render_template
from application import app, db
from application.auth.models import User, Kurssi
from flask_login import login_required, current_user


#from application.kurssit.models import Kurssi


# etusivu
@app.route("/")
def index():
    #user = User.query.all()
    return render_template("index.html") #, user=user)

# käyttäjän henk.koht sivu - Minun kurssit, Minun opetus
@app.route('/user/<usernimi>')
@login_required
def user(usernimi):
    user = User.query.filter_by(username=usernimi).first_or_404()
    teacher_info = User.teacher_info()
#    teacher_my_courses = Kurssi.teacher_my_courses()
    teacher_my_total_courses = User.teacher_my_total_courses()
#    school_total_courses_offered = User.school_total_courses_offered()

    return render_template('user.html', user=user, 
        teacher_info=teacher_info, 
        teacher_my_total_courses=teacher_my_total_courses
    )
