# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class UczenForm(FlaskForm):
    id = HiddenField('Uczen id')
    imie = HiddenField('Imie id')
    nazwisko = HiddenField('Nazwisko id')
    klasa = HiddenField('Klasa id')

class DodajForm(FlaskForm):
    id = HiddenField('Uczen id')
    klasa = StringField('Klasa:',
                          validators=[Required(message=blad1)])
    rok_matury = StringField('Rok matury:',
                            validators=[Required(message=blad1)])
    rok_naboru = StringField('Rok naboru:',
                            validators=[Required(message=blad1)])
