from flask import redirect, render_template, request, url_for

from application import app, db
from application.kurssit.models import Kurssi
from application.kurssit.forms import CourseForm

@app.route("/kurssit", methods=["GET"])
def kurssit_index():
    return render_template("kurssit/list.html", kurssit = Kurssi.query.all())

@app.route("/kurssit/lisaauusikurssi/")
def kurssit_form():
    return render_template("kurssit/lisaauusikurssi.html", form = CourseForm())

@app.route("/kurssit/<kurssi_id>/", methods=["POST"])
def kurssit_set_done(kurssi_id):
    k = Kurssi.query.get(kurssi_id)
    k.done = True
    db.session().commit()
    return redirect(url_for("kurssit_index"))

@app.route("/kurssit/<kurssi_id>/", methods=["POST"])
def kurssit_ilmoittaudu(kurssi_id):
    k = Kurssi.query.get(kurssi_id)
    k.ilmoittautuminen = True
    db.session().commit()
    return redirect(url_for("kurssit_index"))

@app.route("/kurssit/", methods=["POST"])
def kurssit_create():
    form = CourseForm(request.form)
    if not form.validate():
        return render_template("kurssit/lisaauusikurssi.html", form = form)
    k = Kurssi(form.name.data)
    k.done = form.done.data
    db.session().add(k)
    db.session().commit()
    return redirect(url_for("kurssit_index"))
