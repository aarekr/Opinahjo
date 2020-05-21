from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=2)])
    done = BooleanField("Suoritettu") # tämä ei saisi olla opettaja-näkymässä

    class Meta:
        csrf = False
