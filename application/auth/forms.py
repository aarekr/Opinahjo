from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, EqualTo
from application.auth.models import User

# userin kirjautumislomake
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    submit = SubmitField('Kirjaudu sisään')

    class Meta:
        csrf = False

# userin rekisteröintilomake
class RegistrationForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Length(min=3, max=10, message="Käyttäjätunnuksen oltava 3-10 merkkiä pitkä")])
    password = PasswordField("Salasana", [validators.Length(min=2, max=20, message="Salasanan oltava 2-20 merkin pituinen")])
    password2 = PasswordField('Toista salasana', [validators.Length(min=2, max=20), EqualTo('password', message="Salasanojen oltava samoja")])
    submit = SubmitField('Luo käyttäjätili')

    def validate_username(self, username):
        k = User.query.filter_by(username=username.data).first()
        if k is not None: # jos käyttäjätili on jo luotu
            raise ValidationError('Valitse eri käyttäjätunnus')

    class Meta:
        csrf = False
