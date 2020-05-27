from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.kurssit.models import Kurssi
from application.kurssit.forms import CourseForm

from application.auth.models import User


# listaa kaikki kurssit
@app.route("/kurssit", methods=["GET"])
def kurssit_index():
    return render_template("kurssit/list.html", kurssit = Kurssi.query.all())

# näyttää kurssinlisäyslomakkeen, sallittu vain opettajille
@app.route("/kurssit/lisaauusikurssi/")
@login_required
def kurssit_form():
    return render_template("kurssit/lisaauusikurssi.html", form = CourseForm())

# opiskelija varaa kurssipaikan
@app.route("/kurssit/<kurssi_id>/", methods=["POST"])
@login_required
def kurssit_enroll(kurssi_id):
    k = Kurssi.query.get(kurssi_id)
    k.enrolled = True
#    k.account_id = current_user.id # opiskelija-kurssi viite
    db.session().commit()
    return redirect(url_for("kurssit_index"))

# lisätään kurssi tietokantaan, sallittu vain opettajille
@app.route("/kurssit/", methods=["POST"])
@login_required
def kurssit_create():
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
