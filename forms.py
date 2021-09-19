from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year = StringField('Rok wydania', validators=[DataRequired()])
    comments = TextAreaField('Komentarz')
    #cover = FileField('Okładka')