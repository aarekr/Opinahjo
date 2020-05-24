from flask import render_template
from application import app
#from application.forms import RegistrationForm
from application.auth.models import User
from flask_login import login_user, logout_user, current_user

# etusivu
@app.route("/")
def index():
    return render_template("index.html")
