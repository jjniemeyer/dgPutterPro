from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("The username {} is already taken".format(username.data))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This email address is already in use")


class EditGoalForm(FlaskForm):
    current_goal = TextAreaField('Set a Goal', validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')


class DrillForm(FlaskForm):
    putt_distance = IntegerField('putting distance (in feet)',
                                 validators=[DataRequired(),
                                             NumberRange(min=1, max=100,
                                                         message="choose a number between 1 and 100 feet")])
    number_attempts = IntegerField('number of attempts',
                                   validators=[DataRequired(),
                                               NumberRange(min=1,
                                               message="you must attempt a postive number of putts")])
    number_putts_made = IntegerField('putts made', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')

    def validate_putts_made(self, number_putts_made, number_attempts):
        if number_putts_made.data > number_attempts.data:
            raise ValidationEror("The number of putts made must be less than or equal to the number attempted")