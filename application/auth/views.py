from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegistrationForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    # jos käyttäjä on jo kirjautunut => ohjataan Opetustarjonta-sivulle
    if current_user.is_authenticated:
        return redirect(url_for('kurssit_index'))

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
               error = "Käyttäjätunnusta tai salasanaa ei löytynyt")

    login_user(user)
    return redirect(url_for("kurssit_index"))

# uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


# uuden opiskelijatilin rekisteröinti
@app.route("/auth/register")
def user_registration():
    return render_template("auth/newstudentregistration.html", form = RegistrationForm())

# uuden opiskelijan luonti
@app.route("/auth/", methods=["POST"])
def create_student(): # nimi ja käyttäjätunnus käsitelty samana
    form = RegistrationForm(request.form)
    if not form.validate():
        return render_template("auth/newstudentregistration.html", form = form)
    username = request.form.get("username")
    student = True
    teacher = False
    user_role = "STUDENT"
    k = User(username, username, request.form.get("password"), student, teacher, user_role)
    db.session().add(k)
    db.session().commit()

    return redirect(url_for("account_created"))


# uuden opettajatilin rekisteröinti
@app.route("/teacher")
def teacher_registration():
    return render_template("auth/newteacherregistration.html", form = RegistrationForm())

# uuden opettajatilin luonti
@app.route("/teacher", methods=["POST"])
#@login_required #(role="ADMIN")     # tilapäisesti pois käytöstä
def create_teacher(): # nimi ja käyttäjätunnus käsitelty samana
    form = RegistrationForm(request.form)
    if not form.validate():
        return render_template("auth/newteacherregistration.html", form = form)
    username = request.form.get("username")
    student = False
    teacher = True
    user_role = "TEACHER"
    t = User(username, username, request.form.get("password"), student, teacher, user_role)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("account_created"))

# vahvistetaan, että käyttäjätili on luotu
@app.route("/auth/accountcreated")
def account_created():
    return render_template("auth/accountcreated.html")


# opiskelijatilin muokkaus
@app.route("/modifystudent/<student_id>/", methods=["GET"])
@login_required
def modify_student(student_id):
    modified_student = User.query.get(student_id)
    return render_template("auth/updatestudent.html", form = RegistrationForm(), student = modified_student)

# opiskelijatilin päivitys
@app.route("/updatestudent/<student_id>/", methods=["POST"])
@login_required
def update_student(student_id):
    form = RegistrationForm(request.form)
    student = User.query.get(student_id)

    student.username = form.username.data
    student.name = form.username.data

    db.session().commit()
    return redirect(url_for("user", usernimi=current_user.username))

# opiskelijatilin poisto
@app.route("/deletestudent/<student_id>/", methods=["POST"])
@login_required
def delete_student(student_id):
    deleted_student = User.query.get(student_id)

    db.session().delete(deleted_student)
    db.session().commit()

    return redirect(url_for("account_deleted"))

# vahvistetaan, että opiskelijatili on poistettu
@app.route("/auth/accountdeleted")
def account_deleted():
    return render_template("auth/accountdeleted.html")
