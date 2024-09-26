from flask import render_template, request, redirect, url_for, session, flash
from datevault import app, db
from datevault.models import Login
from sqlalchemy import or_


@app.route("/")
def home():
    '''
    Creates the Home page
    '''
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    Creates the login page and searches the database for email, then checks the password.
    '''
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check for main account
        user = Login.query.filter_by(email=email).first()
        # Check_password checks hash password 
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.user_name
            
            # Check if the user has a partner account
            if user.partner_user_name:
                session['partner_user_name'] = user.partner_user_name
            
            return redirect(url_for("home"))
        else:
            # Check for partner account
            partner_user = Login.query.filter_by(partner_email=email).first()
            # Checks partner password hash
            if partner_user and partner_user.check_partner_password(password):
                # If partner account found, set session values
                session['user_id'] = partner_user.id
                session['user_name'] = partner_user.partner_user_name  # Use partner's username
                return redirect(url_for("home"))

        # If neither account was valid
        flash("Invalid email or password. Please try again.", "danger")
        print("Error, Invalid email")
    
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    '''
    Creates the signup page and updates database with signup info. Reviews if user
    is already in database, also hashes password
    '''
    if request.method == "POST":
        print("Signup form submitted")
        # Gets info from form
        user_name=request.form.get("user_name")
        password=request.form.get("SignupPassword")
        email=request.form.get("email")

        # Does this user exist? 
        existing_user = Login.query.filter(or_(Login.email == email,Login.partner_email == email)).first()
        if existing_user:
            flash("Email is alerady registered. Please log in or use another email.","warning")
            return redirect(url_for("signup"))
        signup = Login(
            # Creates a new user
            user_name=user_name,
            email=email,
            # Blank due to not being populated on form.
            partner_user_name=None,
            partner_password_hash=None,
            partner_email=None
        )
        # Hashes password
        signup.set_password(password)
        # Pushes it to Database
        db.session.add(signup)
        db.session.commit()
        print("New partner added to the account")
        flash("Signup successful! Please log in.","success")
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

        if not partner_user_name or not partner_password or not partner_email:
            flash("Please fill out all partner details.", "warning")
            return redirect(url_for("add_partner"))
        
        # existing_partner = Login.query.filter_by(email=partner_email).first()

        user_id = session.get('user_id')
        user = Login.query.get(user_id)
        if user:
            user.partner_user_name = partner_user_name
            user.set_partner_password(partner_password)
            user.partner_email = partner_email
            db.session.commit()
            # Session updates with partner name
            session['partner_user_name'] = partner_user_name

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

@app.route("/new_idea")
def new_idea():
    '''
    Creates the new date idea page
    '''
    return render_template("new_idea.html")

@app.route("/pick_a_date")
def pick_a_date():
    '''
    Creates the page to select a random date.
    '''
    return render_template("pick_a_date.html")