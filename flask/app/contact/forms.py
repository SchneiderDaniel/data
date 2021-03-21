from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

## contact form

class ContactForm(FlaskForm):

    name = StringField('Name',  [DataRequired()])
    email = StringField('E-Mail', [Email(message=('Not a valid E-Mail address.')),DataRequired()])
    body = TextAreaField('Message',  [DataRequired(),Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


