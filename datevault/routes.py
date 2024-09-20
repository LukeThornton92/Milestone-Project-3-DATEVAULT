from flask import render_template, request, redirect, url_for, session, flash
from datevault import app, db
from datevault.models import Login


@app.route("/")
def home():
    '''
    Creates the Home page
    '''
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    Creates the login page and searches database for email, then checks password.
    '''
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Email search
        user_email = Login.query.filter_by(email=email).first()
        # Password match?
        if user_email and user_email.password == password:
            session['user_id'] = user_email.id
            session['user_name'] = user_email.user_name
            session['partner_user_name'] = user_email.partner_user_name
            return redirect(url_for("home"))
        else:
            # Typo or no account
            flash("Invalid email or password. Please try again.", "danger")
            print("Error, Invalid email")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    '''
    Creates the signup page and updates database with signup info.
    '''
    if request.method == "POST":
        print("Signup form submitted")
        signup = Login(
            # Creates a new user 
            user_name=request.form.get("user_name"),
            password=request.form.get("SignupPassword"),
            email=request.form.get("email"),
            # Blank due to not being populated on form.
            partner_user_name=None,
            partner_password=None,
            partner_email=None
        )
        db.session.add(signup)
        db.session.commit()
        print("New partner added to the account")
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/add_partner", methods=["GET", "POST"])
def add_partner():
    '''
    Creates the signup page for partner and updates database with signup info.
    '''
    if request.method == "POST":
        partner_user_name = request.form.get("partner_user_name")
        partner_password = request.form.get("partner_SignupPassword")
        partner_email = request.form.get("partner_email")
        
        print(f"Partner Username: {partner_user_name}")
        print(f"Partner Password: {partner_password}")
        print(f"Partner Email: {partner_email}")

        if not partner_user_name or not partner_password or not partner_email:
            flash("Please fill out all partner details.", "warning")
            return redirect(url_for("add_partner"))

        user_id = session.get('user_id')
        user = Login.query.get(user_id)
        if user:
            user.partner_user_name = partner_user_name
            user.partner_password = partner_password
            user.partner_email = partner_email
            db.session.commit()
            print("Partner info added")
            return redirect(url_for("login"))
    return render_template("add_partner.html")

@app.route("/logout")
def logout():
    '''
    logs user out, clears session
    '''
    session.clear()
    flash("You have been logged out.","info")
    return redirect(url_for("home"))