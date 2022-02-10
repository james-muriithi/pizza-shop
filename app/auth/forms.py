from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError, BooleanField
from wtforms.validators import DataRequired
from ..models import User

class SignupForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired()])
    name = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    remember = BooleanField("Rememember me")
    submit = SubmitField('Sign Up')



