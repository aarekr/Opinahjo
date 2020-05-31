from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.kurssit.models import Kurssi
from application.kurssit.forms import CourseForm
from application.auth.models import User
from application.models import enrollments


# listaa kaikki kurssit
@app.route("/kurssit", methods=["GET"])
def kurssit_index():
    kurssit = Kurssi.query.all()
    school_total_courses_offered = User.school_total_courses_offered()
    school_teachers_total = User.school_teachers_total()
    courses_and_teachers = User.courses_and_teachers()
    student_my_courses = User.student_my_courses()
    return render_template("kurssit/list.html", kurssit = kurssit, 
        school_total_courses_offered=school_total_courses_offered, 
        school_teachers_total=school_teachers_total, 
        courses_and_teachers=courses_and_teachers, 
        student_my_courses=student_my_courses)

# näyttää kurssinlisäyslomakkeen, sallittu vain opettajille
@app.route("/kurssit/lisaauusikurssi/")
@login_required
def kurssit_form():
    return render_template("kurssit/lisaauusikurssi.html", form = CourseForm())

# lisätään kurssi tietokantaan, sallittu vain opettajille
@app.route("/kurssit/", methods=["POST"])
@login_required
def kurssit_create(): # useampi samanniminen kurssi sallittu tarkoituksella
    if not current_user.teacher: # jos ei-opettaja lisäämässä uutta kurssia
        return redirect(url_for("kurssit_index"))

    form = CourseForm(request.form)
    if not form.validate():
        return render_template("kurssit/lisaauusikurssi.html", form = form)

    k = Kurssi(form.name.data)
    k.account_id = current_user.id

    db.session().add(k)
    db.session().commit()
    return redirect(url_for("kurssit_index"))

# opiskelijan kurssi-ilmoittautuminen
@app.route("/ilmoittaudu/<kurssi_id>/", methods=["POST"])
def ilmoittaudu_kurssille(kurssi_id):
    print("**************** opiskelija ilmoittautuu ****************")
    ilm = enrollments
    print("*****kurssi_id: ", kurssi_id)
    print("*****opiske_id: ", current_user.id)
    form = CourseForm(request.form)
    k = Kurssi(form.name.data)
    print("*****k     : ", k.account_id)
    
    
    
#    k.account_id = current_user.id # opiskelija-kurssi viite
#    db.session().commit()

    return redirect(url_for("kurssit_index"))
