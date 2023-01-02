from flask import Flask, render_template

# Create a Flask Instance 
app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey123"

# Create a Route Decoration
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name = name)

# Create a Route Decoration
@app.route("/buttons")
def buttons():
    return render_template("components/buttons.html")

# Create a Route Decoration
@app.route("/cards")
def cards():
    return render_template("components/cards.html")

# Create a Route Decoration
@app.route("/utilitiesColor")
def utilitiesColor():
     return render_template("utilities/utilitiesColor.html")

# Create a Route Decoration
@app.route("/utilitiesBorder")
def utilitiesBorder():
    return render_template("utilities/utilities-border.html")

# Create a Route Decoration
@app.route("/utilitiesAnimation")
def utilitiesAnimation():
    return render_template("utilities/utilities-animation.html")

# Create a Route Decoration
@app.route("/utilitiesOther")
def utilitiesOther():
    return render_template("utilities/utilities-other.html")


# Create a Route Decoration
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


if __name__ == ("__main__"):
    app.run(debug=True)