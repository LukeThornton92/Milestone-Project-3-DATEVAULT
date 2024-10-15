from flask import render_template, request, redirect, url_for, session, flash
from datevault import app, db
from datevault.models import Login, Date, TimeOptions, BudgetOptions, LocationOptions, ActivityOptions
from sqlalchemy import or_
from sqlalchemy.sql.expression import func


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
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        email = request.form.get("email").lower()
        password = request.form.get("password")

        if not email or not password:
            flash("Email or password cannot be blank.", "warning")
            return redirect(url_for("login"))

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
                session['partner_user_name'] = "partner"
                return redirect(url_for("home"))

        # If neither account was valid
        flash("Invalid email or password. Please try again.", "danger")
        # print("Error, Invalid email")
    
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    '''
    Creates the signup page and updates database with signup info. Reviews if user
    is already in database, also hashes password
    '''

    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        # print("Signup form submitted")
        # Gets info from form
        user_name=request.form.get("user_name")
        password=request.form.get("SignupPassword")
        email=request.form.get("email").lower()
        confirm_password=request.form.get("ConfirmSignupPassword")

        if not email or not password or not user_name or not confirm_password:
            flash("Please ensure all fields are populated", "warning")
            return redirect(url_for("signup"))

        if not email or not password:
            flash("Email and password cannot be blank.", "warning")
            return redirect(url_for("login"))

        # User name already taken? 
        existing_username = Login.query.filter(Login.user_name == user_name).first()
        if existing_username:
            flash("Username is already taken. Please try another!","warning")
            return redirect(url_for("signup"))            

        if password != confirm_password:
            flash("Passwords didn't match! Please try again.", "warning")
            return redirect(url_for("signup"))

        # Does this user exist? 
        existing_user = Login.query.filter(or_(Login.email == email,Login.partner_email == email)).first()
        if existing_user:
            flash("Email is already registered. Please log in or use another email.","warning")
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
        # print("New partner added to the account")
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
        partner_email = request.form.get("partner_email").lower()
        confirm_password = request.form.get("confirm_partner_SignupPassword")

        if not partner_user_name or not partner_password or not partner_email:
            flash("Please fill out all partner details.", "warning")
            return redirect(url_for("add_partner"))
        
        if partner_password != confirm_password:
            flash("Passwords didn't match! Please try again.", "warning")
            return redirect(url_for("add_partner"))
        
        existing_user = Login.query.filter(or_(Login.email == partner_email,Login.partner_email == partner_email)).first()
        if existing_user:
            flash("User account already exists!","warning")
            return redirect(url_for("add_partner"))


        user_id = session.get('user_id')
        user = Login.query.get(user_id)
        if user:
            user.partner_user_name = partner_user_name
            user.set_partner_password(partner_password)
            user.partner_email = partner_email
            db.session.commit()
            # Session updates with partner name
            session['partner_user_name'] = partner_user_name

            # print("Partner info added")
            return redirect(url_for("home"))
    return render_template("add_partner.html")

@app.route("/logout")
def logout():
    '''
    logs user out, clears session
    '''
    session.clear()
    flash("You have been logged out.","info")
    return redirect(url_for("home"))

@app.route("/new_idea", methods=["GET", "POST"])
def new_idea():
    '''
    Creates the new date idea page
    '''

    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    if request.method == "POST":
        # print(request.form)
        name=request.form.get("name")
        is_time=request.form.get("is_time")
        # Checks to see if valid entry, protects database. Also converts is_time to a string.
        if is_time in TimeOptions.__members__:
            selected_time=TimeOptions[is_time]
        else:
            flash("Invalid Time Selection! How did you do that?","error")
            return redirect(url_for('new_idea'))
        is_budget=request.form.get("is_budget")
        # Checks to see if valid entry, protects database. Also converts is_budget to a string.
        if is_budget in BudgetOptions.__members__:
            selected_budget=BudgetOptions[is_budget]
        else:
            flash("Invalid Budget Selection! How did you do that?","error")
            return redirect(url_for('new_idea'))
        is_location=request.form.get("is_location")
        # Checks to see if valid entry, protects database. Also converts is_location to a string.
        if is_location in LocationOptions.__members__:
            selected_location=LocationOptions[is_location]
        else:
            flash("Invalid Location Selection! How did you do that?","error")
            return redirect(url_for('new_idea'))
        is_activity=request.form.get("is_activity")
        # Checks to see if valid entry, protects database. Also converts is_activity to a string.
        if is_activity in ActivityOptions.__members__:
            selected_activity=ActivityOptions[is_activity]
        else:
            flash("Invalid Activity Selection! How did you do that?","error")
            return redirect(url_for('new_idea'))
        is_dog = "is_dog" in request.form # Returns True if checked, wont return anything if not which equals False
        # print(f"Is Dog: {is_dog}")  # Debugging line
        is_reservation = "is_reservation" in request.form
        is_indoor = "is_indoor" in request.form
        notes=request.form.get("notes")

        # Creates a new_date object
        new_date = Date(
            name=name,
            is_time=selected_time,
            is_budget=selected_budget,
            is_location=selected_location,
            is_dog=is_dog,
            is_activity=selected_activity,
            is_reservation=is_reservation,
            is_indoor=is_indoor,
            notes=notes,
            owner_id=session.get('user_id')
        )
        db.session.add(new_date)
        db.session.commit()

        flash("New date idea added successfully! Add another!", "success")
        return redirect(url_for("new_idea"))
    
    return render_template("new_idea.html", time_options=TimeOptions, budget_options=BudgetOptions, location_options=LocationOptions, activity_options=ActivityOptions)

@app.route("/pick_a_date",  methods=["GET", "POST"])
def pick_a_date():
    '''
    Creates the page to select a random date.
    '''

    if 'user_id' not in session:
        return redirect(url_for('home'))

    # Any dates in the table? Jinja2 uses this.
    user_id = session.get('user_id')
    # print(user_id) #debugging
    no_date_check = Date.query.filter_by(owner_id=user_id).first()
    # print(no_date_check)

    random_date = None

    if request.method == "POST":
        is_time = request.form.get("is_time")
        is_budget = request.form.get("is_budget")
        is_location = request.form.get("is_location")
        is_activity = request.form.get("is_activity")
        is_dog = request.form.get("is_dog") == "yes"
        is_reservation = request.form.get("is_reservation") == "yes"
        is_indoor = request.form.get("is_indoor") == "yes"

        # Debugging, booleans only return False
        # print(f"is_dog: {is_dog}, is_reservation: {is_reservation}, is_indoor: {is_indoor}")

        query = Date.query # Builds query

        filters = []

        if is_time:
            filters.append(Date.is_time == is_time)
        if is_budget and is_budget != "Any":
            filters.append(Date.is_budget == is_budget)
        if is_location and is_location != "Any":
            filters.append(Date.is_location == is_location)
        if is_activity and is_activity != "Any":
            filters.append(Date.is_activity == is_activity)
        if is_dog:
            filters.append(Date.is_dog == True)
        if is_reservation:
            filters.append(Date.is_reservation == True)
        if is_indoor:
            filters.append(Date.is_indoor == True)
        if user_id:
            filters.append(Date.owner_id == user_id)
        # Final line of query, unpacks list and adds all filters to query
        if filters:
            query = query.filter(*filters)


        result = query.all()

        #print(filters) 

        # Gets count of how many dates match
        result_count = query.count()

        if result_count == 0:
            flash("No dates found matching your criteria!", "error")
        else:
            random_date = query.order_by(func.random()).first()

    return render_template("pick_a_date.html", no_date_check=no_date_check,  time_options=TimeOptions, budget_options=BudgetOptions, location_options=LocationOptions, activity_options=ActivityOptions, random_date=random_date) # no_date_check is passed to the html so jinja works!

@app.route("/view_all", methods =["GET", "POST"])
def view_all():
    '''
    displays all dates, best way of editing and deleting saved dates 
    '''

    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user_id=session.get('user_id')
        
    if not user_id:
        flash("You need to log in to view your dates!", "error")
        return redirect(url_for('login'))
        
    all_dates = Date.query.filter_by(owner_id=user_id).all()
    
    # Debugging
    #print(f"User ID: {user_id}")
    #print(f"All dates: {all_dates}")

    
    return render_template("view_all.html", all_dates=all_dates)


@app.route("/edit_date/<int:date_id>", methods=["GET", "POST"])
def edit_date(date_id):

    if 'user_id' not in session:
        return redirect(url_for('home'))

    date = Date.query.get_or_404(date_id) #finds record 

    # time_options = [(time.name, time.value) for time in TimeOptions]

    if request.method == "POST":
        # Update all the fields with new form data
        date.date_name = request.form.get("date_name")
        date.is_time = request.form.get("is_time")
        date.is_budget = request.form.get("is_budget")
        date.is_location = request.form.get("is_location")
        date.is_activity = request.form.get("is_activity")
        date.is_dog = request.form.get("is_dog") == "yes"
        date.is_reservation = request.form.get("is_reservation") == "yes"
        date.is_indoor = request.form.get("is_indoor") == "yes"
        date.notes = request.form.get("notes")

        # Update db
        db.session.commit()

        flash("Date idea updated successfully!", "success")
        return redirect(url_for("view_all"))

    return render_template("edit_date.html", time_options=TimeOptions, budget_options=BudgetOptions, location_options=LocationOptions, activity_options=ActivityOptions, date=date)

@app.route("/delete_date/<int:date_id>")
def delete_date(date_id):
    date = Date.query.get_or_404(date_id) #finds record 
    db.session.delete(date)
    db.session.commit()
    flash("Date idea deleted successfully!", "success")
    return redirect(url_for("view_all"))

@app.route("/delete_user_confirm")
def delete_user_confirm():
    """Displays a confirmation page before deleting the user."""

    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user_id = session.get('user_id')
    
    if user_id is None:
        # Redirect to login if user_id is not found
        flash("You need to be logged in to delete your account.", "danger")
        return redirect(url_for("login"))

    return render_template("delete_user.html", user_id=user_id)

@app.route("/confirm_delete_user", methods=["POST"])
def confirm_delete_user():
    """Deletes the user after confirmation."""
    user_id = session.get('user_id')
    user_to_delete = Login.query.get_or_404(user_id)
    # Clear the session
    session.clear()
    # Delete the user from the database
    db.session.delete(user_to_delete)
    db.session.commit()
    
    flash("User deleted successfully!", "success")
    return redirect(url_for("home"))

'''
@app.route('/your_saved_dates')
def your_saved_dates():
    page = request.args.get('page', 1, type=int)  # Get the page number from the query string, default to 1
    per_page = 9  # Display 9 dates per page
    all_dates = Date.query.filter_by(owner_id=session.get('user_id')).paginate(page=page, per_page=per_page)  # Paginate the query for the logged-in user
    return render_template('your_saved_dates.html', all_dates=all_dates)  # Ensure your template name is correct
'''
@app.route("/404")
def not_found():
    '''
    Creates the 404 page
    '''
    return render_template("404.html")