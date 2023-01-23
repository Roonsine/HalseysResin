from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class UserForm(FlaskForm):
    name = StringField("Name?", validators=[DataRequired()])
    email = StringField("Email?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a form class
class ProductForm(FlaskForm):
    name = StringField("What's the Product Name?", validators=[DataRequired()])
    price = StringField("How much does this cost?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a form class
class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")