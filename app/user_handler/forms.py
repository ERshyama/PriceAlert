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
