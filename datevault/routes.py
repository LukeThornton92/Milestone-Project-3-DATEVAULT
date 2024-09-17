from flask import render_template, request, redirect, url_for, session
from datevault import app, db
from datevault.models import Login


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Email search
        user_email = Login.query.filter_by(email=email).first()
        # D        
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        print("Signup form submitted")
        signup = Login(
            user_name=request.form.get("user_name"),
            password=request.form.get("SignupPassword"),
            email=request.form.get("email"),
            partner_user_name="",
            partner_password="",
            partner_email=""
        )
        db.session.add(signup)
        db.session.commit()
        print("New user added to the database")
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/add_partner", methods=["GET", "POST"])
def add_partner():
    return render_template("add_partner.html")