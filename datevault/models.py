from datevault import db

class Login(db.Model):
    #schema for the login model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.VARCHAR(50), unique=True, nullable=True)
    password = db.Column(db.VARCHAR(250), unique=False, nullable=True)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=True)
    #partner login details
    partner_user_name = db.Column(db.VARCHAR(50), unique=True, nullable=True)
    partner_password = db.Column(db.VARCHAR(250), unique=False, nullable=True)
    partner_email = db.Column(db.VARCHAR(100), unique=True, nullable=True)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string.
        return self.user_name
    