from flask import render_template
from application import app
from application.auth.models import User
from flask_login import login_required, current_user


# etusivu
@app.route("/")
def index():
    return render_template("index.html")

# käyttäjän henk.koht sivu
@app.route('/user/<usernimi>')
@login_required
def user(usernimi):
    user = User.query.filter_by(username=usernimi).first_or_404()
#    posts = [
#        {'author': user, 'body': 'Test post 1'},
#        {'author': user, 'body': 'Test post 2'}
#    ]
    return render_template('user.html', user=user)
