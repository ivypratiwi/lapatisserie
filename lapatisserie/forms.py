from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email, Regexp


# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    surname = StringField("Your surname", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    phone = StringField("Your phone number", validators=[
                        InputRequired(),
                        Regexp('\d', message="Phone number must be in digit.")])
    address = StringField("Your address", validators=[InputRequired()])
    comment = StringField("Your comment")
    submit = SubmitField("Submit Order")
