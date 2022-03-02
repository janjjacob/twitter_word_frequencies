from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, SubmitField

class mostCommonWordsFromUserForm(FlaskForm):
    username = StringField('Username')
    count = IntegerField('Count', [validators.NumberRange(min=1)])
    send = SubmitField('send')