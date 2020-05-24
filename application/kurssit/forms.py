from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=2)])
    enrolled = BooleanField("Paikka varattu") # mun lisäys
#    done = BooleanField("Suoritettu") # tämä ei saisi olla opettaja-näkymässä

    class Meta:
        csrf = False