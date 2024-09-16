from flask import render_template, request, redirect, url_for
from datevault import app, db
from datevault.models import Login


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        signup = Login(
            user_name=request.form.get("user_name") 
            password=request.form.get("SignupPassword"),
            email=request.form.get("email"),
            partner_user_name="",
            partner_password="",
            partner_email=""
        )
        db.session.add(signup)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/add_partner", methods=["GET", "POST"])
def add_partner():
    return render_template("add_partner.html")