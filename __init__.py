from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask Instance 
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

# Create a form class
class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name = name)

@app.route("/buttons")
def buttons():
    return render_template("components/buttons.html")

@app.route("/cards")
def cards():
    return render_template("components/cards.html")

@app.route("/utilitiesColor")
def utilitiesColor():
     return render_template("utilities/utilitiesColor.html")

@app.route("/utilitiesBorder")
def utilitiesBorder():
    return render_template("utilities/utilities-border.html")

@app.route("/utilitiesAnimation")
def utilitiesAnimation():
    return render_template("utilities/utilities-animation.html")

@app.route("/utilitiesOther")
def utilitiesOther():
    return render_template("utilities/utilities-other.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

@app.route("/login")
def login():
    return render_template("pages/login.html")

@app.route("/register")
def register():
    return render_template("pages/register.html")

@app.route("/forgotPassword")
def forgotPassword():
    return render_template("pages/forgotPassword.html")

@app.route("/error")
def error():
    return render_template("pages/error.html")

@app.route("/blank")
def blank():
    return render_template("pages/blank.html")

@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted")
    return render_template("test/name.html", name=name, form=form)

if __name__ == ("__main__"):
    app.run(debug=True)