from flask import Flask, render_template, flash, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@Movement1@localhost/Affluent Areas'
app.secret_key = "boobies"
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20), unique=False)

    def __init__(self, password, email):
        self.username = password
        self.email = email

    def __repr__(self):
        return '<USER %r>' % self.username

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/SignUp/')
def sign_Up():
    flash("Flash test")
    return render_template("signup.html")

@app.route('/LogIn/', methods = ['GET','POST'])
def log_In():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            flash(attempted_username)
            flash(attempted_password)

            if attempted_username == 'a@a' and attempted_password == 'a':
                return redirect(url_for('homepage'))
            else:
                error = 'Invalid credentials. Try Again.'
        return render_template("login.html", error=error)

    except Exception as e:
        return render_template("login.html", error=error)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run()
