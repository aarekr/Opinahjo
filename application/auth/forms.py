from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from application.auth.models import User

# kirjautumislomake
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

# käyttäjätilin rekisteröintilomake
#class RegistrationForm(FlaskForm):
#    username = StringField('Username', validators=[DataRequired()])
#    email = StringField('Email', validators=[DataRequired(), Email()])
#    password = PasswordField('Password', validators=[DataRequired()])
#    password2 = PasswordField(
#        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#    submit = SubmitField('Register')

#    def validate_username(self, username):
#        user = User.query.filter_by(username=username.data).first()
#        if user is not None:
#            raise ValidationError('Please use a different username.')
