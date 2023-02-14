from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm



# Create the extension
db = SQLAlchemy()
# Create a Flask Instance 
app = Flask(__name__)
# Add Database
# Old SQLite DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# New MySQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/users'
# initialize the app with the extension
db.init_app(app)
# Secret Key!
app.config['SECRET_KEY'] = "secretkey123"


# Create a Model
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    price = db.Column(db.String(10))
    size = db.Column(db.String(10))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expenseSource = db.Column(db.String(20), nullable=False, unique=True)
    expenseAmount = db.Column(db.String(20))
    expenseDate = db.Column(db.String(20))

    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a Model
class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    incomeSource = db.Column(db.String(20), nullable=False, unique=True)
    incomeAmount = db.Column(db.String(20))
    incomeDate = db.Column(db.String(20))

    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name

# All models go above this
with app.app_context():
    db.create_all()

class ExpenseForm(FlaskForm):
    expenseSource = StringField("What is the source of this expense?", validators=[DataRequired()])
    expenseAmount = StringField("What is the amount?", validators=[DataRequired()])
    expenseDate = StringField("When did this expense Occur?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class IncomeForm(FlaskForm):
    incomeSource = StringField("What is the source of this income?", validators=[DataRequired()])
    incomeAmount = StringField("What is the amount?", validators=[DataRequired()])
    incomeDate = StringField("When did this income Occur?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    name = StringField("Name?", validators=[DataRequired()])
    email = StringField("Email?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ProductForm(FlaskForm):
    name = StringField("What's the Product Name?", validators=[DataRequired()])
    price = StringField("How much does this cost?", validators=[DataRequired()])
    size = StringField("Whats the size?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user/user.html", user_name = name)

@app.route('/income/add', methods=['GET', 'POST'])
def AddIncome():
    incomeSource = None
    incomeAmount = None
    incomeDate = None
    form = IncomeForm()
    if form.validate_on_submit():
        if db.session.query(Income).filter_by(incomeAmount=incomeAmount):
            income = Income(incomeSource = form.incomeSource.data, incomeAmount = form.incomeAmount.data, incomeDate = form.incomeDate.data)
            db.session.add(income)
            db.session.commit()
        incomeSource = form.incomeSource.data
        incomeAmount = form.incomeAmount.data
        incomeDate = form.incomeDate.data
        form.incomeSource.data = ''
        form.incomeAmount.data = ''
        form.incomeDate.data = ''
        flash('Income Added')
    our_income = Income.query.order_by(Income.incomeDate)
    return render_template("test/add_income.html", form=form, incomeAmount=incomeAmount, incomeSource=incomeSource, incomeDate=incomeDate, our_income=our_income)

@app.route('/expense/add', methods=['GET', 'POST'])
def AddExpense():
    expenseSource = None
    expenseAmount = None
    expenseDate = None
    form = ExpenseForm()
    if form.validate_on_submit():
        if db.session.query(Expense).filter_by(expenseAmount=expenseAmount):
            expense = Expense(expenseSource = form.expenseSource.data, expenseAmount = form.expenseAmount.data, expenseDate = form.expenseDate.data)
            db.session.add(expense)
            db.session.commit()
        expenseSource = form.expenseSource.data
        expenseAmount = form.expenseAmount.data
        expenseDate = form.expenseDate.data
        form.expenseAmount.data = ''
        form.expenseAmount.data = ''
        form.expenseDate.data = ''
        flash('Expense Added')
    our_expense = Expense.query.order_by(Expense.expenseDate)
    return render_template("test/add_expense.html", form=form, expenseAmount=expenseAmount, expenseSource=expenseSource, expenseDate=expenseDate, our_expense=our_expense)

@app.route('/products/add', methods=['GET', 'POST'])
def AddProduct():
    name = None
    price = None
    size = None
    form = ProductForm()
    if form.validate_on_submit():
        if db.session.query(Products).filter_by(name=name):
            product = Products(name=form.name.data, price=form.price.data, size = form.size.data)         
            db.session.add(product)
            db.session.commit()
        name = form.name.data
        price = form.price.data
        size = form.size.data
        form.name.data = ''
        form.price.data = ''
        form.size.data = ''
        flash("Product Added")
    our_products = Products.query.order_by(Products.date_added)
    return render_template("test/add_product.html", form = form, name=name,our_products=our_products, price=price, size = size)

@app.route('/user/add', methods=['GET', 'POST'])
def AddUser(): 
    name = None
    form = UserForm()
    if form.validate_on_submit():
        if db.session.query(Users).filter_by(name=name):
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User Added")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("user/add_user.html", name=name, form=form, our_users=our_users)

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