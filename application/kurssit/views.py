from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.kurssit.models import Kurssi
from application.kurssit.forms import CourseForm
from application.auth.models import User
from application.models import enrollments, userinvoices
from application.laskut.models import Invoice


# listaa kaikki kurssit, näytetään kaikille
@app.route("/kurssit", methods=["GET"])
def kurssit_index():
    courses = Kurssi.query.all()
    school_total_courses_offered = User.school_total_courses_offered()
    school_teachers_total = User.school_teachers_total()
    courses_and_teachers = User.courses_and_teachers()
    student_my_courses = User.student_my_courses()
    return render_template("kurssit/list.html", kurssit = courses, 
        school_total_courses_offered=school_total_courses_offered, 
        school_teachers_total=school_teachers_total, 
        courses_and_teachers=courses_and_teachers, 
        student_my_courses=student_my_courses)

# näyttää kurssinlisäyslomakkeen, sallittu vain opettajille
@app.route("/kurssit/addnewcourse/")
@login_required
def kurssit_form():
    return render_template("kurssit/addnewcourse.html", form = CourseForm())

# lisätään kurssi tietokantaan, sallittu vain opettajille
@app.route("/kurssit/", methods=["POST"])
@login_required
def kurssit_create(): # useampi samanniminen kurssi sallittu
    if not current_user.teacher:
        return redirect(url_for("index"))

    form = CourseForm(request.form)
    course = Kurssi(form.name.data, form.start_date.data, form.end_date.data)

    if not form.validate():
        return render_template("kurssit/addnewcourse.html", form = form)

    if not form.validate_dates():
        form.start_date.errors.append("Tarkista päivämäärä")
        form.end_date.errors.append("Tarkista päivämäärä")
        return render_template("kurssit/update.html", form = form)

    course.account_id = current_user.id

    db.session().add(course)
    db.session().commit()
    return redirect(url_for("user", usernimi=current_user.username))

# kurssin deletointi, vain kurssin lisännyt opettaja
@app.route("/delete/<kurssi_id>/", methods=["POST"])
@login_required
def kurssit_delete(kurssi_id):
    deleted_course = Kurssi.query.get(kurssi_id)
    if deleted_course.account_id != current_user.id:
        return "Et voi poistaa tätä kurssia opetusohjelmasta!"

    db.session().delete(deleted_course)
    db.session().commit()

    return redirect(url_for("user", usernimi=current_user.username))

# kurssin muokkaaminen, vain kurssin lisännyt opettaja
@app.route("/modify/<kurssi_id>", methods=["GET"])
@login_required
def kurssit_modify(kurssi_id):
    course = Kurssi.query.get(kurssi_id)
    if course.account_id != current_user.id:
        return "Et voi muokata tätä kurssia!"

    return render_template("kurssit/update.html", form = CourseForm(), kurssi = course)

# kurssin päivitys, sallittu vain opettajalle
@app.route("/kurssit/update/<kurssi_id>", methods=["POST"])
@login_required
def kurssit_update(kurssi_id):
    form = CourseForm(request.form)
    course = Kurssi.query.get(kurssi_id)

    if not course:
        return redirect(url_for("kurssit_index"))

    course.name = form.name.data
    course.start_date = form.start_date.data
    course.end_date = form.end_date.data

    if not form.validate():
        return render_template("kurssit/update.html", form = form, kurssi = course)

    if not form.validate_dates():
        form.start_date.errors.append("Tarkista päivämäärä")
        form.end_date.errors.append("Tarkista päivämäärä")
        return render_template("kurssit/update.html", form = form, kurssi = course)

    db.session().commit()
    return redirect(url_for("user", usernimi=current_user.username))


# opiskelijan kurssi-ilmoittautuminen
@app.route("/enroll/<kurssi_id>/", methods=["POST"])
@login_required
def enroll_course(kurssi_id):
    user = User.query.get(current_user.id)
    course = Kurssi.query.get(kurssi_id)

    course.users.append(user)
    db.session().commit()

    return redirect(url_for("user", usernimi=current_user.username))

# opiskelijan peru ilmoittautuminen
@app.route("/disenroll/<kurssi_id>/")
@login_required
def disenroll_course(kurssi_id):
    user = User.query.get(current_user.id)
    course = Kurssi.query.get(kurssi_id)

    course.users.remove(user)
    db.session().commit()

    return redirect(url_for("user", usernimi=current_user.username))
