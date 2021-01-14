from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed

class UploadJavaForm(FlaskForm):
    java = FileField('.java hochladen', validators=[FileAllowed(['java', 'txt'])])
    submit = SubmitField('Bestätigen')