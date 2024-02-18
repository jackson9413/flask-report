from flask_wtf import FlaskForm
from wtforms import StringField, SelectionField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    type = SelectionField('Type', validators = [DataRequired()], choices = [('income', 'income'), ('expense', 'expense')])
    category = SelectionField('Category', validators = [DataRequired()], choices = [('rent', 'rent'), ('salary', 'salary'), ('investment', 'investment'), ('side_hustle', 'side_hustle')])
    amount = IntegerField("Amount", validators=[DataRequired()])
    submit = SubmitField("Generate Report")

