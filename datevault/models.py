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
    