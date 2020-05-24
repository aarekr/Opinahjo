from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegistrationForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    # jos käyttäjä on jo kirjautunut => ohjataan etusivulle
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
               error = "Käyttäjätunnusta tai salasanaa ei löytynyt")

    login_user(user)
    return redirect(url_for("index"))

# uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


# uuden käyttäjätilin rekisteröinti
@app.route("/auth/register")
def user_registration():
    return render_template("auth/newuserregistration.html", form = RegistrationForm())

@app.route("/auth/", methods=["POST"])
def create_user():
    form = RegistrationForm(request.form)
    if not form.validate():
        return render_template("auth/newuserregistration.html", form = form)
    print(request.form.get("username")) # printtaa nimen logiin
    nimi = request.form.get("username") # nimi = käyttäjätunnus
    k = User(nimi, nimi, request.form.get("password"))
    db.session().add(k)
    db.session().commit()

    return redirect(url_for("tili_luotu"))

# vahvistetaan, että käyttäjätili on luotu
@app.route("/auth/accountcreated")
def tili_luotu():
    return render_template("auth/accountcreated.html")