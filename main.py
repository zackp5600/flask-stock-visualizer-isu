from flask import Flask
from flask import render_template


app = Flask(__name__)



@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)

