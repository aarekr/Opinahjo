from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, validators

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=2)])
    enrolled = BooleanField("Paikka varattu")
    submit = SubmitField('Lisää opetusohjelmaan')

    class Meta:
        csrf = False
