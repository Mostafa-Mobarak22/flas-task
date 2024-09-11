from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField ,FileField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length
class BoookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(5, 20)])
    description = StringField('Description', validators=[ Length(5, 1000)])
    image = FileField('Image', validators=[DataRequired()])
    number = IntegerField('Number of Pages',validators=[DataRequired()])
    submit = SubmitField('Submit')

