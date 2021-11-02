from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import User




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



