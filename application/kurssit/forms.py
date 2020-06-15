from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SubmitField, validators
from datetime import date

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=2, max=20, message="Kurssin nimen pituuden oltava 2-20 merkkiä")])
    start_date = DateField("Alkaa", default=date.today)
    end_date = DateField("Loppuu", default=date.today)
    submit = SubmitField('Lisää opetusohjelmaan')

    def validate_dates(self):
        result = super(CourseForm, self).validate()
        if (self.start_date.data > self.end_date.data):
            return False
        else:
            return result

    class Meta:
        csrf = False
