from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.auth.models import User
from application.kurssit.models import Kurssi
from application.models import enrollments, userinvoices
from application.laskut.models import Invoice

@app.route("/invoices/")
@login_required
def show_invoices():
    if not current_user.teacher:
        return redirect(url_for("index"))

    courses_and_enrollments_count = User.courses_and_enrollments_count()
    student_enrollments_count = User.student_enrollments_count()
    all_invoices = User.all_invoices()
    return render_template("laskut/allinvoices.html", 
        courses_and_enrollments_count=courses_and_enrollments_count, 
        student_enrollments_count=student_enrollments_count, 
        all_invoices=all_invoices
    )

# opiskelija luo laskun
@app.route("/invoices/create/<kurssi_id>/<user_id>/")
def create_invoice(kurssi_id, user_id):
    print("*****Opiskelija luo laskun")
    print("*****Kurssi_id: ", kurssi_id)
    print("*****User___id: ", user_id)

    course = Kurssi.query.get(kurssi_id)
    invoice = Invoice(kurssi_id)

    invoice.account_id = user_id

    db.session().add(invoice)
    db.session().commit()

    invoice = Invoice.query.get(invoice.id)
    print("*****Laskun numero: ", invoice.id)
    invoice_number = invoice.id

    return render_template("laskut/invoice.html", 
        invoice_number=invoice_number
    )

# opiskelija maksaa laskun
@app.route("/invoices/pay/<invoice_number>/", methods=["POST"])
def pay_invoice(invoice_number):
    print("*****Maksetaan lasku ", invoice_number)
    invoice = Invoice.query.get(invoice_number)
    invoice.paid = True
    print("*****Lasku maksettu: ", invoice.paid)
    db.session().commit()

    return redirect(url_for("index"))
