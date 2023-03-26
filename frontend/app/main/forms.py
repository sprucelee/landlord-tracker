from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import Length


class AddressLookupForm(FlaskForm):
    address = StringField("address", validators=[Length(max=255)])
    submit = SubmitField(label="Lookup")
