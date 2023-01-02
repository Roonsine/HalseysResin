from flask import Flask, render_template

# Create a Flask Instance 
app = Flask(__name__)

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
    return render_template("buttons.html")

# Create a Route Decoration
@app.route("/cards")
def cards():
    return render_template("cards.html")

# Create a Route Decoration
@app.route("/utilitiesColor")
def utilitiesColor():
     return render_template("utilitiesColor.html")

# Create a Route Decoration
@app.route("/utilitiesBorder")
def utilitiesBorder():
    return render_template("utilities-border.html")

# Create a Route Decoration
@app.route("/utilitiesAnimation")
def utilitiesAnimation():
    return render_template("utilities-animation.html")

# Create a Route Decoration
@app.route("/utilitiesOther")
def utilitiesOther():
    return render_template("utilities-other.html")


if __name__ == ("__main__"):
    app.run(debug=True)