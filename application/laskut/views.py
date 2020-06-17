from application import app
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.auth.models import User

@app.route("/invoices/")
@login_required
def show_invoices():
    if not current_user.teacher:
        return redirect(url_for("index"))

    courses_and_enrollments_count = User.courses_and_enrollments_count()
    student_enrollments_count = User.student_enrollments_count()
    return render_template("laskut/allinvoices.html", 
        courses_and_enrollments_count=courses_and_enrollments_count, 
        student_enrollments_count=student_enrollments_count
    )
