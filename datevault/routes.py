from flask import render_template
from datevault import app, db
from datevault.models import Login


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
