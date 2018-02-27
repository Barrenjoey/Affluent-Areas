from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/SignIn/')
def sign_In():
    return render_template("signIn.html")

if __name__ == "__main__":
    app.run()
