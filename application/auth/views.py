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
    return redirect(url_for("kurssit_index"))


# uuden opiskelijatilin rekisteröinti
@app.route("/auth/register")
def user_registration():
    return render_template("auth/newuserregistration.html", form = RegistrationForm())

# uuden opiskelijan luonti
@app.route("/auth/", methods=["POST"])
def create_user():
    form = RegistrationForm(request.form)
    if not form.validate():
        return render_template("auth/newuserregistration.html", form = form)
    nimi = request.form.get("username") # nimi = käyttäjätunnus
    student = True
    teacher = False
    k = User(nimi, nimi, request.form.get("password"), student, teacher)
    db.session().add(k)
    db.session().commit()

    return redirect(url_for("account_created"))


# uuden opettajatilin rekisteröinti
@app.route("/opettaja")
#@login_required(role="ADMIN")
def teacher_registration():
    return render_template("auth/uudenopettajanrekisterointi.html", form = RegistrationForm())

# uuden opettajan luonti
@app.route("/opettaja", methods=["POST"])
#@login_required(role="ADMIN")
def create_teacher():
    form = RegistrationForm(request.form)
    if not form.validate():
        return render_template("auth/uudenopettajanrekisterointi.html", form = form)
    nimi = request.form.get("username") # nimi = käyttäjätunnus
    student = False
    teacher = True
    t = User(nimi, nimi, request.form.get("password"), student, teacher)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("account_created"))

# vahvistetaan, että käyttäjätili on luotu
@app.route("/auth/accountcreated")
def account_created():
    return render_template("auth/accountcreated.html")
