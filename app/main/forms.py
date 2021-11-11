from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError



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
                                               message="you must attempt a positive number of putts")])
    # TODO fix this validator
    number_putts_made = IntegerField('putts made', validators=[DataRequired(),
                                                               NumberRange(min=0,
                                                               message="you can not make more putts than you attempt")])
    submit = SubmitField('Submit')

    def validate_putts_made(self):
        pass



