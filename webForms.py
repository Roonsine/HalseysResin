from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    expenseSource = StringField("What is the source of this expense?", validators=[DataRequired()])
    expenseAmount = StringField("What is the amount?", validators=[DataRequired()])
    expenseDate = DateField("When did this expense Occur?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class IncomeForm(FlaskForm):
    incomeSource = StringField("What is the source of this income?", validators=[DataRequired()])
    incomeAmount = StringField("What is the amount?", validators=[DataRequired()])
    incomeDate = DateField("When did this income Occur?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    name = StringField("Name?", validators=[DataRequired()])
    email = StringField("Email?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ProductForm(FlaskForm):
    name = StringField("What's the Product Name?*", validators=[DataRequired()])
    price = StringField("How much does this cost?*", validators=[DataRequired()])
    size = StringField("Whats the size?*", validators=[DataRequired()])
    submit = SubmitField("Submit")

class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
