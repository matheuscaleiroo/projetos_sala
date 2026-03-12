from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get["email"] == "adin@email.com" and request.form.get["password"] == "123456":
            return render_template("painel.html")
        return render_template("painel.html")
    else:
        return render_template("login.html")

@app.route("/painel")
def painel():
    return render_template("painel.html")
