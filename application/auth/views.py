from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    # jos käyttäjä on jo kirjautunut => ohjataan etusivulle
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))

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
@app.route("/auth/newuser")
def kayttajan_rekisterointi():
    return render_template("auth/newuser.html")

@app.route("/auth/", methods=["POST"])
def luo_kayttaja():
    print(request.form.get("name")) # printtaa nimen logiin
    nimi = request.form.get("name") # nimi = käyttäjätunnus
    k = User(nimi, nimi, request.form.get("salasana"))
    db.session().add(k)
    db.session().commit()

    return redirect(url_for("index"))
