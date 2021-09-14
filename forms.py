from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Regexp

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year = StringField('Rok wydania', validators=[DataRequired()])
    comments = TextAreaField('Komentarz')
    cover = FileField(u'Okładka', validators=[Regexp('^\w+.(jpg|png|gif)$')])
