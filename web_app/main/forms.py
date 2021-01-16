from typing import Optional
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed
from wtforms.fields.core import StringField

class UploadJavaForm(FlaskForm):
    comments = StringField('Enter customn comments (//, #, ...): ', validators=(Optional()))
    types = StringField('custom types (//, #, ...)', validators=(Optional()))
    remove_tags = StringField('Enter customn modifier (public, private, ...): ', validators=(Optional()))
    java = FileField('.java hochladen', validators=[FileAllowed(['java', 'txt'])])
    submit = SubmitField('Bestätigen')