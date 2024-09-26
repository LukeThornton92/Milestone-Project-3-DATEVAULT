import enum
from sqlalchemy import Enum
from datevault import db
from werkzeug.security import generate_password_hash, check_password_hash


class Login(db.Model):
    #schema for the login model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.VARCHAR(50), unique=True, nullable=True)
    password_hash = db.Column(db.VARCHAR(250), unique=False, nullable=True)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=True)
    #partner login details
    partner_user_name = db.Column(db.VARCHAR(50), unique=True, nullable=True)
    partner_password_hash = db.Column(db.VARCHAR(250), unique=False, nullable=True)
    partner_email = db.Column(db.VARCHAR(100), unique=True, nullable=True)

    # Set password method to hash the password before storing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Verify password method to compare the hash with the input
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Partner account
    def set_partner_password(self, partner_password):
        self.partner_password_hash = generate_password_hash(partner_password)

    def check_partner_password(self, partner_password):
        return check_password_hash(self.partner_password_hash, partner_password)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string.
        return self.user_name


# Define an Enum for time options
class TimeOptions(enum.Enum):
    MORNING = "Morning"
    AFTERNOON = "Afternoon"
    EVENING = "Evening"
    ANY = "Any"
    
class BudgetOptions(enum.Enum):
    FREE = "Free"
    CHEAP = "Cheap"
    EXPENSIVE = "Expensive"

class LocationOptions(enum.Enum):
    AT_HOME = "At Home"
    LOCAL = "Local"
    DAY_TRIP = "Day Trip"
    VACATION = "Vacation"
    
class ActivityOptions(enum.Enum):
    RELAXED = "Relaxed"
    MODERATE = "Moderate"
    HIGH = "High"

class Date(db.Model):
    # Schema for the Date Model
    id = db.Column(db.Integer, primary_key=True)
    is_time = db.Column(Enum(TimeOptions), nullable=False)
    is_budget = db.Column(Enum(BudgetOptions), nullable=False)
    is_location = db.Column(Enum(LocationOptions), nullable=False)
    is_dog = db.Column(db.Boolean, nullable=False)
    is_activity = db.Column(Enum(ActivityOptions), nullable=False)
    is_reservation = db.Column(db.Boolean, nullable=False)
    is_indoor = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string.
        return f"<Date id={self.id}, time={self.is_time.value}, budget={self.is_budget.value}, location={self.is_location.value}, dog_friendly={self.is_dog}, activity={self.is_activity.value}, reservation_required={self.is_reservation}, indoor={self.is_indoor}>"

