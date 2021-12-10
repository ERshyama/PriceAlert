from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddUserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='Please enter your name')])
    email = StringField('email', validators=[DataRequired('Please enter email')])

class DeleteUserForm(FlaskForm):
    email = StringField('email', validators=[DataRequired('Please enter email')])

class ChooseActionForm(FlaskForm):
    action = StringField('action', validators=[DataRequired('Please Choose your Action')])

# from flask.wtf import Form # , RecaptchaField
#
# # Import Form elements such as TextField and BooleanField (optional)
# from wtforms import TextField, PasswordField # BooleanField
#
# # Import Form validators
# from wtforms.validators import Required, Email, EqualTo
#
#
# # Define the login form (WTForms)
#
# class LoginForm(Form):
#     email    = TextField('Email Address', [Email(),
#                 Required(message='Forgot your email address?')])
#     password = PasswordField('Password', [
#                 Required(message='Must provide a password. ;-)')])