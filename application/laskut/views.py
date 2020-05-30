from application import app
from flask import render_template, request

@app.route("/laskut/")
def show_invoices():
     return "hello laskut"
#    return render_template("laskut/kaikkilaskut.html")
