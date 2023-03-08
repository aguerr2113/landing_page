from wtforms import Form, StringField,PasswordField, validators,SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm

class SigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Sign In')

class SignupForm(Form):
    name = StringField('Name',[
        validators.InputRequired()
        ])
    email = StringField('Email',[
        validators.InputRequired(),
        validators.Email()
        ])
    password = PasswordField(
        'Password',[
        validators.InputRequired(),
        validators.Length(min=8, max=20),
        validators.EqualTo('confirm_password', message='Passwords do not match')
    ])
    confirm_password = PasswordField('Confirm Password')